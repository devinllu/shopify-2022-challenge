from sqlalchemy.sql.expression import desc
from . import db
from sqlalchemy.sql import func

class Item(db.Model):
    name = db.Column(db.String(26), primary_key=True)
    description = db.Column(db.String(160), nullable=False)
    item_name = db.Column(db.String(50), nullable=False)

    def __init__(self, name, description, item_name):
        self.name = name
        self.description = description
        self.item_name = item_name