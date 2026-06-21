from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite2"


db = SQLAlchemy(app)

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/about")
def about():
    details = db.session.query(About).all()
    return render_template("about.html", details=details)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        number = request.form.get("phone")
        return f"Thank you for your message, we will call you at {number}!"
    if request.method == "GET":
        return render_template("contact.html")
    
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form.get("name")
        new_entry = About(name=name)
        db.session.add(new_entry)
        db.session.commit()
        return redirect("/about")
    if request.method == "GET":
        return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)
