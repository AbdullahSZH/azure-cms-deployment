from FlaskWebProject import db, app
from FlaskWebProject.models import User, Post

with app.app_context():
    # Drop all existing tables (optional)
    # db.drop_all()

    # Create all tables
    db.create_all()

    # Optional: add a test user
    if not User.query.filter_by(username="admin").first():
        test_user = User(username="admin")
        test_user.set_password("admin123")  # Make sure password meets your criteria
        db.session.add(test_user)
        db.session.commit()
        print("Test user 'admin' added.")
    else:
        print("User 'admin' already exists.")

    print("Database initialized successfully.")
