from flask import Blueprint, redirect, render_template, url_for, request
from mainapp.extensions import mongo
from bson.objectid import ObjectId

main = Blueprint('main', __name__)

def index():
    """
    Renders the main index page with a list of todos.

    Returns:
        str: Rendered HTML template.
    """
    todos_collection = mongo.db.todos
    todos = todos_collection.find()
    return render_template('index.html', todos=todos)

def add_todo():
    """
    Adds a new todo item to the database.

    Returns:
        redirect: Redirects to the main index page.
    """
    todos_collection = mongo.db.todos
    todo_item = request.form.get('new-todo')
    todos_collection.insert_one({'text': todo_item, 'complete': False})
    return redirect(url_for('main.index'))

def complete_todo(oid):
    """
    Marks a specific todo item as complete.

    Args:
        oid (str): Object ID of the todo item.

    Returns:
        redirect: Redirects to the main index page.
    """
    todos_collection = mongo.db.todos
    todos_collection.find_one_and_update({"_id": ObjectId(oid)}, {"$set": {"complete": True}})
    return redirect(url_for('main.index'))

def delete_completed():
    """
    Deletes all completed todo items.

    Returns:
        redirect: Redirects to the main index page.
    """
    todos_collection = mongo.db.todos
    todos_collection.delete_many({'complete': True})
    return redirect(url_for('main.index'))

def delete_all():
    """
    Deletes all todo items.

    Returns:
        redirect: Redirects to the main index page.
    """
    todos_collection = mongo.db.todos
    todos_collection.delete_many({})
    return redirect(url_for('main.index'))

