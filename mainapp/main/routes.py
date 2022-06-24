from flask import Blueprint, redirect, render_template, url_for, request
from mainapp.extensions import mongo
from bson.objectid import ObjectId

main = Blueprint('main', __name__)


@main.route('/')
def index():
    todos_collection = mongo.db.todos
    todos = todos_collection.find()
    return render_template('index.html', todos=todos)

@main.route('/add_todo', methods=['POST'])
def add_todo():
    todos_collection = mongo.db.todos
    todo_item = request.form.get('new-todo')
    todos_collection.insert_one({'text' : todo_item, 'complete' : False})
    return redirect(url_for('main.index'))

@main.route('/complete_todo/<oid>')
def complete_todo(oid):
    todos_collection = mongo.db.todos
    todo_item = todos_collection.find_one({'_id' : ObjectId(oid)})
    todo_item['complete'] = True
    todos_collection.save(todo_item)
    return redirect(url_for('main.index'))
   
