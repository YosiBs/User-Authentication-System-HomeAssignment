from backend.app import app
from backend.utils.extensions import db
from backend.app import app
from backend.utils.extensions import db
from backend.models import UserModel

with app.app_context():
    db.drop_all()
    db.create_all()
    print("✅ Database reset.")
    print("✅ Database and tables created.")

    # print all the table names
    print("📋 Tables:", db.metadata.tables.keys())

    # print all the users
    users = UserModel.query.all()
    print("📋 Users:")
    for user in users:
        print(user.__dict__)