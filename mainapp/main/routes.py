from pickletools import read_string1
from flask import Blueprint, render_template
from mainapp.extensions import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template ('index.html')