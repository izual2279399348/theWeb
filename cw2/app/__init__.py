# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 06:05:36 2019

@author: Thinkpad
"""

import logging
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request as req
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

app = Flask(__name__)
app.config.from_object('config.development')
csrf.init_app(app)
db = SQLAlchemy(app)
@app.after_request
def log_response(resp):
    app.logger.info("{} {} {}\n{}".format(req.method, req.url, req.data, resp))
    return resp

from app import pages

app.register_blueprint(pages.Pages.blueprint)
app.logger.setLevel(logging.NOTSET)