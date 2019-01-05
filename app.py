#!/usr/bin/python3
from flask import Flask, json, jsonify
from models import session, Category, Item


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/api')
def api():
    data = session.query(Category).all()
    return jsonify([d.serialize() for d in data])


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
