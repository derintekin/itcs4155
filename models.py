from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

def create_initial_user():
    # Create a user if the table is empty
    if User.query.count() == 0:  # Check if there are existing users
        new_user = User(username='testuser', email='test@example.com', password='testpassword')
        db.session.add(new_user)
        db.session.commit()