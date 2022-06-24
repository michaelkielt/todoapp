from crypt import methods
from pickletools import read_string1
from flask import Blueprint, redirect, render_template, url_for, request
from mainapp.extensions import mongo

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template ('index.html')

@main.route('/add_todo', methods=['POST'])
def add_todo():
    todos_collection = mongo.db.todos
    todo_item = request.form.get('new_todo')
    todos_collection.insert_one({'text' : todo_item, 'complete' : False})
    return redirect(url_for('main.index'))