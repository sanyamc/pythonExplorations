from flask import Flask, escape, request
from blueprints.page import page

def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(page)

    return app

app = create_app()

# @app.route('/')
# def hello():
#     name = request.args.get("name", "World")
#     return 'Hello, from Flask!'

# @app.route('/hello/<name>')
# def hello_name(name):
#     return 'Hello {}'.format(name)