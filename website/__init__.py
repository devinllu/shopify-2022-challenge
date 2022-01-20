from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

from .views import views
from .models import Item

app = Flask(__name__)

def create_app():

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')

    create_database()
    create_fake_data(app)
    test_db()
    return app

@app.before_first_request
def create_database():
    db.create_all(app=app)

def test_db():
    with app.app_context():
        users = Item.query.all()

        print(f'Length: {len(users)}')


def create_fake_data(app):
    a1 = Item(description="160kg, 60 bucks, note: this is automatic, default fake data", name="Devin", item_name="Fridge")
    a2 = Item(description="Black mask, need to sell! note: this is automatic, default fake data", name="Joe", item_name="Mask")
    a3 = Item(description="Charizard rare pokemon card, $100k note: this is automatic, default fake data", name="John", item_name="Pokemon Cards")
    a4 = Item(description="10kg chair, wooden, brown note: this is automatic, default fake data", name="Amelia", item_name="Chair")

    lst = [a1, a2, a3, a4]

    for entries in lst:
        with app.app_context():
            exists = db.session.query(Item.name).filter_by(name=entries.name).first() is not None
            if not exists:
                db.session.add(entries)
                db.session.commit()