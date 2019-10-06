from flask import Flask, escape, request


app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return 'Hello, from Flask!'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello {}'.format(name)