#!/usr/bin/python3
from flask import Flask, jsonify, render_template, url_for, \
    request, redirect, flash
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
    items = session.query(Category).\
        filter_by(name=name).\
        all()
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


# Create new item
@app.route('/catalog/<name>/new',
           methods=['GET', 'POST'])
def new(name):
    # Determine current sequence number for id column
    sql = "SELECT pg_catalog.setval(pg_get_serial_sequence('items', 'id'), \
        MAX(id)) FROM items"
    result = session.execute(sql)
    for row in result:
        id = row[0] + 1
    # For a post request, create new item in database and redirect to home page
    if request.method == 'POST':
        new_item = Item(id=id,
                        title=request.form['name'],
                        description=request.form['description'],
                        cat_id=request.form['cat_id'])
        session.add(new_item)
        session.commit()
        flash('New item created')
        # TODO: consider redirecting to items not index
        return redirect(url_for('items',
                                name=name))
    # For a get request, render the form
    else:
        return render_template('new.html',
                               title=title,
                               name=name)


# Delete existing item
@app.route('/catalog/<name>/<description>/delete',
           methods=['GET', 'POST'])
def delete(name, description):
    delete_item = session.query(Item).filter_by(title=description).one()
    # For a post request, delete item and redirect to items page
    if request.method == 'POST':
        session.delete(delete_item)
        session.commit()
        flash('Item deleted')
        return redirect(url_for('items',
                                name=name))
    # For a get request, render the page
    else:
        return render_template('delete.html',
                               name=name,
                               description=description,
                               item=delete_item)


# JSON api endpoint
@app.route('/catalog/api')
def catalogAPI():
    data = session.query(Category).all()
    return jsonify([d.serialize() for d in data])


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
