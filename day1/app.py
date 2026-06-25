from flask import Flask, render_template, request, redirect
from flask_restful import Api
from flask_security import Security

app = Flask(__name__)
api = Api(app)
from config import configurations
app.config.from_object(configurations)

from models import user_datastore
Security(app, user_datastore)

from models import db, About
db.init_app(app)

from routes.test import test_api
app.register_blueprint(test_api)


from routes.cars import cars_bp
app.register_blueprint(cars_bp)

from routes.cars import cars_crud
api.add_resource(cars_crud, '/api/cars')

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
