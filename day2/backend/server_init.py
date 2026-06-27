from models import db
from app import init_app

app, _ = init_app()

def create_roles():
    from models import user_datastore, db
    roles = ['admin', 'customer', 'manager']
    for role in roles:
        user_datastore.find_or_create_role(name=role)
    db.session.commit()
    return 'Roles created successfully!'

def create_admin():
    from models import user_datastore, db
    from hashing import ph
    if user_datastore.find_user(id=1) is None:
        user = user_datastore.create_user(
            email='admin@abc.com',
            password=ph.hash('admin')
        )
        user_datastore.add_role_to_user(user, 'admin')
        db.session.commit()
        return 'Admin user created successfully!'
    return 'Admin user already exists!'

with app.app_context():
    db.create_all()
    create_roles()
    create_admin()