from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship(
        'ItemModel',
        back_populates = 'store',   # Connected with ItemModel.store

        # Returns a query object instead of a list.
        # - With "dynamic", store.items is not loaded immediately.
        # - You can run store.items.all(), store.items.count(),
        #   or store.items.filter_by(...) to query only when needed.
        # - Useful when a store has many items (avoids loading all at once).
        lazy='dynamic'
    )

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]} #fetched item

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
