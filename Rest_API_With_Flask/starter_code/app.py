import os

from flask import Flask
from flask_restful import Api

from .resources.item import Item, ItemList

# Create the Flask application instance
app = Flask(__name__)

# Enable debug mode (auto-reloads on code changes and shows detailed error pages)
app.config['DEBUG'] = True

# Set the database URI
# Use the value from the environment variable DATABASE_URL if available
# Otherwise, default to a local SQLite database file 'data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')

# Disable SQLAlchemy's event system that tracks object changes (saves memory and improves performance)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the Flask-RESTful API with the Flask app
api = Api(app)

# Add the Item resource to the API
# The endpoint will be /item/<name>, for example: /item/pen
api.add_resource(Item, '/item/<string:name>')


if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
