from flask import render_template,request,url_for,abort
from . import main
from flask_login import login_required,current_user


@main.route('/')
def index():
  
  return render_template('index.html')