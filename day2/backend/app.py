from flask import Flask, render_template, request, redirect
from flask_restful import Api
from flask_security import Security

def init_app():
    init_app = Flask(__name__)
    init_api = Api(init_app)
    from config import configurations
    init_app.config.from_object(configurations)

    from models import user_datastore
    Security(init_app, user_datastore)

    from models import db, About
    db.init_app(init_app)

    from routes.test import test_api
    init_app.register_blueprint(test_api)

    from routes.cars import cars_bp
    init_app.register_blueprint(cars_bp)

    from routes.security import security_bp
    init_app.register_blueprint(security_bp)

    from routes.cars import cars_crud
    init_api.add_resource(cars_crud, '/api/cars')

    return init_app, init_api

app, api = init_app()



if __name__ == "__main__":
    app.run()
