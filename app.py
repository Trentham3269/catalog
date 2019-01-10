#!/usr/bin/python3
from flask import Flask, jsonify, render_template, url_for
from models import session, Category, Item
from sqlalchemy import desc


app = Flask(__name__)


# Define app title for templates
title = 'Catalog App'


# Return all categories and most recent 10 items added
@app.route('/')
def index():
    categories = session.query(Category).all()
    items = session.query(Item.title, Category.name).\
        join(Category).\
        order_by(Item.id.desc()).\
        limit(10).\
        all()
    return render_template('index.html',
                           title=title,
                           categories=categories,
                           items=items)


# Return items for specific category
@app.route('/catalog/<name>/items')
def items(name):
    categories = session.query(Category).all()
    items = session.query(Category).filter_by(name=name).all()
    count = session.query(Item.title, Category.name).\
        join(Category).\
        filter_by(name=name).\
        count()
    return render_template('items.html',
                           title=title,
                           name=name,
                           categories=categories,
                           items=items,
                           count=count)


# Return description of individual item
@app.route('/catalog/<name>/<description>')
def item(name, description):
    item = session.query(Category.name, Item.title, Item.description).\
        join(Item).\
        filter_by(title=description).\
        one()
    return render_template('item.html',
                           title=title,
                           name=name,
                           description=description,  
                           item=item)


# JSON api endpoint
@app.route('/catalog/api')
def catalogAPI():
    data = session.query(Category).all()
    return jsonify([d.serialize() for d in data])


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
