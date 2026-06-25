from flask import Blueprint, request
from flask_restful import Resource
from models import db, cars

cars_bp = Blueprint('cars', __name__)

@cars_bp.route('/cars', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_cars():
    if request.method == 'POST':
        data = request.get_json()
        new_car = cars(model=data['model'], fuel=data['fuel'])
        db.session.add(new_car)

        db.session.commit()
        return {"message": "Car added successfully!"}, 201

    elif request.method == 'GET':
        all_cars = cars.query.all()
        if not all_cars:
            return {"message": "No cars found!"}, 404
        return {"cars": [{"id": car.id, "model": car.model, "fuel": car.fuel} for car in all_cars]}, 200

    elif request.method == 'PUT':
        data = request.get_json()
        car_to_update = cars.query.get(data['id'])
        if car_to_update:
            if 'model' in data:
                car_to_update.model = data['model']
            if 'fuel' in data:
                car_to_update.fuel = data['fuel']
            db.session.commit()
            return {"message": "Car updated successfully!"}, 200
        else:
            return {"message": "Car not found!"}, 404

    elif request.method == 'DELETE':
        data = request.get_json()
        car_to_delete = cars.query.get(data['id'])
        if car_to_delete:
            db.session.delete(car_to_delete)
            db.session.commit()
            return {"message": "Car deleted successfully!"}, 200
        else:
            return {"message": "Car not found!"}, 404
# -------------------------------------------------------------------------------------------------
# 
#     
# @cars_bp.route('/cars', methods=['POST', 'GET', 'PUT', 'DELETE'])

class cars_crud(Resource):
    # if request.method == 'POST':
    def post(self):
        data = request.get_json()
        new_car = cars(model=data['model'], fuel=data['fuel'])
        db.session.add(new_car)

        db.session.commit()
        return {"message": "Car added successfully!"}, 201

    # elif request.method == 'GET':
    def get(self):
        all_cars = cars.query.all()
        if not all_cars:
            return {"message": "No cars found!"}, 404
        return {"cars": [{"id": car.id, "model": car.model, "fuel": car.fuel} for car in all_cars]}, 200

    # elif request.method == 'PUT':
    def put(self):
        data = request.get_json()
        car_to_update = cars.query.get(data['id'])
        if car_to_update:
            if 'model' in data:
                car_to_update.model = data['model']
            if 'fuel' in data:
                car_to_update.fuel = data['fuel']
            db.session.commit()
            return {"message": "Car updated successfully!"}, 200
        else:
            return {"message": "Car not found!"}, 404

    # elif request.method == 'DELETE':
    def delete(self):
        data = request.get_json()
        car_to_delete = cars.query.get(data['id'])
        if car_to_delete:
            db.session.delete(car_to_delete)
            db.session.commit()
            return {"message": "Car deleted successfully!"}, 200
        else:
            return {"message": "Car not found!"}, 404