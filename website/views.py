from flask import Blueprint, render_template, request, redirect, url_for
from .models import Item
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html") 

@views.route('/listings')
def listings():
    items = Item.query.all()

    context = {
        "inventory": items
    }

    return render_template("listings.html", context=context)

@views.route('/new-listing', methods =["POST", "GET"])
def post_listings():
    if request.method == "POST":
        name = request.form.get('input_name')
        item_name = request.form.get('input_item_name')
        description = request.form.get('input_description')

        obj = Item(name=name, item_name=item_name, description=description)

        user_exists = db.session.query(Item.name).filter_by(name=obj.name).first() is not None

        if not user_exists:
            db.session.add(obj)
            db.session.commit()

        users = Item.query.all()

        context = {
            "inventory": users
        }
        return render_template("listings.html", context=context)

    if request.method == "GET":
        return render_template("create_listings.html")

@views.route('/delete/<id>')
def delete(id):

    item = Item.query.get(id)

    try:
        db.session.delete(item)
        db.session.commit()

    except:
        print("Sorry, there was some error in deleting records")
    
    context = {
        "inventory": Item.query.all() 
    }
    
    return render_template("listings.html", context=context)

@views.route('/update/<id>', methods =["POST", "GET"])
def update(id):

    if request.method == 'POST':
        name = request.form.get('input_name')
        item_name = request.form.get('input_item_name')
        description = request.form.get('input_description')

        record = Item.query.get(id)
        record.name = name
        record.item_name = item_name
        record.description = description

        db.session.commit()
        context = {
            "inventory": Item.query.all() 
        }

        return render_template('listings.html', context=context)

    item = Item.query.get(id)

    return render_template('update_listings.html', context=item)
