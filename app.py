from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, User, create_initial_user
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

#Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Interstellar101_@localhost/healthtracker'

#Initialize the Database
# db = SQLAlchemy(app)
db.init_app(app)  # Initialize db with the app


# Create tables and an initial user in the database
with app.app_context():
    db.create_all()  # Create all tables
    create_initial_user()  # Create a test user if not exists

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
