#!/usr/bin/python3
from flask import Flask, json, jsonify, send_file, send_from_directory
from models import session, Category, Item


app = Flask(__name__)


@app.route('/')
def index():
    return send_file('index.html')


@app.route('/static/<path:path>')
def resources(path):
    return send_from_directory('static', path)


@app.route('/catalog/api')
def catalog():
    data = session.query(Category).all()
    return jsonify([d.serialize() for d in data])


@app.route('/catalog/api/<int:id>/items')
def category(id):
    data = session.query(Category).filter_by(id=id).all()
    return jsonify([d.serialize() for d in data])


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
