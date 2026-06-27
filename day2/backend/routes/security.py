from flask import Blueprint, request
from models import db, user_datastore
from hashing import ph

security_bp = Blueprint('security_apis', __name__)

@security_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data['email'] or not data['password'] or not data['role']:
        return {"message": "Email and password are required!"}, 400
    if '@' not in data['email']:
        return {"message": "Invalid email format!"}, 400
    
    if user_datastore.find_user(email=data['email']):
        return {"message": "Email already exists!"}, 400
    
    user = user_datastore.create_user(email=data['email'], password=ph.hash(data['password']))

    if data.get('role') == 'manager':
        user_datastore.add_role_to_user(user, 'manager')
        user_datastore.deactivate_user(user)
    elif data.get('role') == 'customer':
        user_datastore.add_role_to_user(user, 'customer')

    db.session.commit()

    return {"message": "User registered successfully!"}, 201

@security_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data['email'] or not data['password']:
        return {"message": "Email and password are required!"}, 400
    
    user = user_datastore.find_user(email=data['email'])
    if not user:
        return {"message": "Invalid email or password!"}, 401
    
    try:
        ph.verify(user.password, data['password'])
    except Exception:
        return {"message": "Invalid email or password!"}, 401

    if not user.active:
        return {"message": "Contact administrator!"}, 403


    return {"message": "Login successful!", "user_id": user.id, "authToken": user.get_auth_token()}, 200