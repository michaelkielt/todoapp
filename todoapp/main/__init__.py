from flask import Flask

from main.routes import main
from ..extensions import mongo

def create_app():
    app = Flask(__name__)

    app.config['MONGO_URL'] = 'mongodb+srv://michaelkielt:1234@cluster0.elzid.mongodb.net/todoappretryWrites=true&w=majority'

    mongo.init_app(app)

    app.register_blueprint(main)

    return app