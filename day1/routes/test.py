from flask import render_template, request, redirect, Blueprint
from models import db, About
# from app import app

test_api = Blueprint("test_api", __name__)

@test_api.route("/")
def hello():
    return {"msg": "Hello, World!"}

# @app.route("/")
# def hello():
#     return "Hello, World!"

@test_api.route("/about")
def about():
    details = db.session.query(About).all()
    print(details)
    details_list = [{"id": detail.id, "name": detail.name} for detail in details]
    return {"msg": "About Page", "details": details_list}

@test_api.route("/contact", methods=["POST"])
def contact():
    if request.method == "POST":
        number = request.json.get("phone")
        return {"msg": f"Thanks for submitting your contact number: {number}"}
    # if request.method == "GET":
    #     return render_template("contact.html")
    
@test_api.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        name = request.json.get("name")
        new_entry = About(name=name)
        db.session.add(new_entry)
        db.session.commit()
        return {"msg": f"Added {name} to the database."}, 201
    # if request.method == "GET":
    #     return render_template("add.html")