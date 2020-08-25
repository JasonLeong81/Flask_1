from flask import Blueprint, render_template, request, redirect, url_for
from . import DB
from .models import Comment

main = Blueprint('main',__name__)

@main.route('/')
def index():
    comment = Comment.query.all()
    return render_template('index.html',comment=comment)

@main.route('/sign')
def Sign():
    # return 'Sign Up'
    return render_template('sign.html')

@main.route('/sign_post',methods=['POST'])
def sign_post():
    name = request.form.get('name')
    comment = request.form.get('comment')
    new_comment = Comment(name=name,comment_text=comment)
    DB.session.add(new_comment)
    DB.session.commit()
    return redirect(url_for('main.index'))
    # return f'Name: {name} Comment: {comment}'


