from starter_code.db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    # Define this method as a class method, so it can be called on the class itself (not on an instance)
    # Example: Item.find_by_name("pen")
    def find_by_name(cls, name):
        # 'cls' refers to the class (e.g., Item) where this method is defined
        # 'cls.query' gives access to the SQLAlchemy query object for the table mapped to this class
        # 'filter_by(name=name)' adds a WHERE condition to filter rows where the 'name' column matches the argument
        # 'first()' returns the first matching record or None if no match is found
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
