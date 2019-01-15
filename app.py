#!/usr/bin/python3
from flask import Flask, jsonify, render_template, url_for, \
    request, redirect, flash, make_response, session as login_session
from models import session, Category, Item
from sqlalchemy import desc
import random
import string
import json
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import requests


app = Flask(__name__)


client_id = json.loads(
    open('client_secret.json', 'r').read())['web']['client_id']
application_name = 'Catalog App'


# Return all categories and most recent items added
@app.route('/')
def index():
    categories = session.query(Category).all()
    count = session.query(Category).count()
    items = session.query(Item.title, Category.name).\
        join(Category).\
        order_by(Item.id.desc()).\
        limit(count).\
        all()
    return render_template('index.html',
                           title=application_name,
                           categories=categories,
                           items=items)


@app.route('/login')
def login():
    state = ''.join(random.choice(string.ascii_uppercase + string.
                    digits) for x in range(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/connect',
           methods=['POST'])
def connect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(
            json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorisation code
    code = request.data

    try:
        # Upgrade the authorisation code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secret.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorisation code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={}'
           .format(access_token))
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1].decode())
    # Abort if there is an error in the access token
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app
    if result['issued_to'] != client_id:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()
    login_session['name'] = data['name']

    output = ''
    output += '<h3>Welcome, '
    output += login_session['name']
    output += '!</h3>'
    flash('You are now logged in as {}'.format(login_session['name']))
    return output


@app.route('/logout')
def disconnect():
    access_token = login_session.get('access_token')
    print('access token is...{}'.format(access_token))
    if access_token is None:
        print('Access Token is None')
        response = make_response(json.dumps(
            'Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print('In gdisconnect access token is {}'.format(access_token))
    print('User name is: ')
    print(login_session['name'])
    url = 'https://accounts.google.com/o/oauth2/revoke?token={}'.format(
        login_session['access_token'])
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print('result is ')
    print(result)
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['name']
        response = make_response(json.dumps(
            'Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps(
            'Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


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
                           title=application_name,
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
                           title=application_name,
                           name=name,
                           description=description,
                           item=item)


# Create new item
@app.route('/catalog/<name>/new',
           methods=['GET', 'POST'])
def new(name):
    # Require user login
    if 'name' not in login_session:
        return redirect('/login')
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
        return redirect(url_for('items',
                                name=name))
    # For a get request, render the form
    else:
        return render_template('new.html',
                               title=application_name,
                               name=name)


# Edit existing item
@app.route('/catalog/<name>/<description>/edit',
           methods=['GET', 'POST'])
def edit(name, description):
    # Require user login
    if 'name' not in login_session:
        return redirect('/login')
    edit_item = session.query(Item).\
        filter_by(title=description).\
        one()
    # For a post request, edit item and redirect to items page
    if request.method == 'POST':
        if request.form['title']:
            edit_item.title = request.form['title']
        session.add(edit_item)
        session.commit()
        flash('Item updated')
        return redirect(url_for('items',
                                name=name))
    # For a get request, render the form
    else:
        return render_template('edit.html',
                               title=application_name,
                               name=name,
                               description=description,
                               item=edit_item)


# Delete existing item
@app.route('/catalog/<name>/<description>/delete',
           methods=['GET', 'POST'])
def delete(name, description):
    # Require user login
    if 'name' not in login_session:
        return redirect('/login')
    delete_item = session.query(Item).\
        filter_by(title=description).\
        one()
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
                               title=application_name,
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
