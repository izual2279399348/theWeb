# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:21:12 2019

@author: Thinkpad
"""

from flask import render_template, Blueprint, request, redirect
from app.forms import LoginForm,RegisterForm,ForgotForm,EditForm,BookForm
from app import db
from .models import User
from .models import Book
from .models import BookRecommanded

class Pages():

    blueprint = Blueprint('pages', __name__)
    theEmail = ''
    the_flag = False
    user_ = User.query.order_by('name').first()
    book_ = Book.query.order_by('bookname').first()
    a=0
    @blueprint.route('/')
    def home():
        return render_template('pages/home.html',flag=Pages.the_flag)


    @blueprint.route('/about',methods=['GET','POST'])
    def about():
        users_ = User.query.all()
        if Pages.the_flag == False:
            return redirect('/')
        for user in users_:
            if Pages.user_.name == user.name:
                books = Book.query.order_by('bookname').filter(Book.username==user.name)
                return render_template('pages/about.html',user=Pages.user_,books=books)
        return redirect('/about')


    @blueprint.route('/login',methods=['GET','POST'])
    def login():
        if Pages.the_flag == True:
            return redirect('/')
        form = LoginForm(request.form)
        users_ = User.query.all()
        for user in users_:
            if form.name.data == user.name:
                if form.password.data == user.password:
                    if form.validate_on_submit():
                        Pages.user_ = user
                        Pages.the_flag = True
                        return redirect('/about')
        return render_template('forms/login.html', form=form)
    
    
    @blueprint.route('/logout',methods=['GET','POST'])
    def logout():
        Pages.the_flag = False
        return redirect('/')


    @blueprint.route('/register',methods=['GET','POST'])
    def register():
        if Pages.the_flag == True:
            return redirect('/')
        form = RegisterForm(request.form)
        users_ = User.query.all()
        for user in users_:
            if form.name.data == user.name:
                return render_template('forms/register.html', form=form)
        if form.validate_on_submit():
            t = User(name = form.name.data,email = form.email.data,password = form.password.data)
            db.session.add(t)
            db.session.commit()
            return redirect('/login')
        return render_template('forms/register.html', form=form)

    @blueprint.route('/forgetUser',methods=['GET','POST'])
    def forgetUser():
        users_ = User.query.all()
        users = []
        for user in users_:
            if user.email == Pages.theEmail:
                users.append(user)
        return render_template('pages/user_list_1.html',
                           title='All Student',
                           users=users)


    @blueprint.route('/forgot',methods=['GET','POST'])
    def forgot():
        if Pages.the_flag == True:
            return redirect('/')
        form = ForgotForm(request.form)
        if form.validate_on_submit():
            Pages.theEmail = form.email.data
            email = form.email.data
            users = User.query.all()
            for user in users:
                if user.email == email:
                    return redirect('/forgetUser')
        return render_template('forms/forgot.html', form=form)


    @blueprint.route('/Users',methods=['GET','POST'])
    def showUser():
        users = User.query.order_by('name').all()
        return render_template('pages/user_list.html',
                           title='All Student',
                           users=users)

    @blueprint.route('/edit_user/<name>',methods=['GET','POST'])
    def edit_user(name):
        user1_ = User.query.get(name)
        form = EditForm()
        if form.validate_on_submit():
            t = user1_
            t.name = form.name.data
            t.email = form.email.data
            t.password = form.password.data
            db.session.commit()
            users_ = User.query.all()
            for user in users_:
                if form.name.data == user.name:
                    if form.password.data == user.password:
                        Pages.user_ = user
                        Pages.the_flag = True
            return redirect('/about')
        return render_template('pages/edit_user.html',title='Edit Student',form=form)


    @blueprint.route('/delete_user/<name>',methods=['GET','POST'])
    def delete_user(name):
        user = User.query.get(name)
        db.session.delete(user)
        db.session.commit()
        return redirect('/Users')
    
    @blueprint.route('/add_book',methods=['GET','POST'])
    def add_book():
        form = BookForm(request.form)
        users_ = User.query.all()
        books_ = Book.query.all()
        for user in users_:
            if Pages.user_.name == user.name:
                if form.validate_on_submit():
                    t = Book(bookname = form.book.data,author = form.author.data,username = Pages.user_.name,evaluation = form.evaluation.data)
                    for book in books_:
                        if book.bookname == form.book.data:
                            return redirect('/add_book')
                    db.session.add(t)
                    db.session.commit()
                    return redirect('/about')
        return render_template('forms/add_book.html', form=form)
    
    
    @blueprint.route('/delete_book/<name>',methods=['GET','POST'])
    def delete_book(name):
        book = Book.query.get(name)
        db.session.delete(book)
        db.session.commit()
        return redirect('/about')
    
    
    @blueprint.route('/edit_book',methods=['GET','POST'])
    def edit_book():
        books = Book.query.order_by('bookname').all()
        return render_template('pages/book_list.html',
                           title='All Book',
                           books=books)
        
        
    @blueprint.route('/add_recommanded_book',methods=['GET','POST'])
    def add_recommanded_book():
        form = BookForm(request.form)
        users_ = User.query.all()
        books_ = BookRecommanded.query.all()
        for user in users_:
            if Pages.user_.name == user.name:
                if form.validate_on_submit():
                    t = BookRecommanded(bookname = form.book.data,author = form.author.data,evaluation = form.evaluation.data)
                    for book in books_:
                        if book.bookname == form.book.data:
                            return redirect('/add_recommanded_book')
                    db.session.add(t)
                    db.session.commit()
                    return redirect('/recommanded')
        return render_template('forms/add_book.html', form=form)
    
    @blueprint.route('/recommanded',methods=['GET','POST'])
    def recommanded():
        books = BookRecommanded.query.order_by('bookname').all()
        return render_template('pages/recommanded.html',
                           title='All Books',user=Pages.user_,
                           books=books)
        
        
    @blueprint.route('/delete_recommanded_book/<name>',methods=['GET','POST'])
    def delete_recommanded_book(name):
        book = BookRecommanded.query.get(name)
        db.session.delete(book)
        db.session.commit()
        return redirect('/recommanded')
        
    
    
    
    
    
    
    
    
    
