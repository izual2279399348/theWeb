# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:21:39 2019

@author: Thinkpad
"""

from app import db



class User (db.Model):
    name = db.Column(db.String(250), primary_key=True)
    email = db.Column(db.String(250), index=True)
    password = db.Column(db.String(250), index=True)
    
    
class Book (db.Model):
    bookname = db.Column(db.String(250), primary_key=True)
    author = db.Column(db.String(250), index=True)
    username = db.Column(db.String(250), index=True)
    evaluation = db.Column(db.String(250), index=True)
    
    
    
class BookRecommanded (db.Model):
    bookname = db.Column(db.String(250), primary_key=True)
    author = db.Column(db.String(250), index=True)
    evaluation = db.Column(db.String(250), index=True)