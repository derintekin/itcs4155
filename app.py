from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, User, create_initial_user
import time
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key


#Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Interstellar101_@localhost/healthtracker'

#Initialize the Database
# db = SQLAlchemy(app)
db.init_app(app)  # Initialize db with the app


# Create tables and an initial user in the database
with app.app_context():
    db.create_all()  # Create all tables
    # create_initial_user() 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/userlogin')
def userlogin():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Fetch the user from the database
        user = User.query.filter_by(username=username).first()
        
        # Check if user exists and password matches
        if user and user.password == password:  # Ideally, use hashed passwords in production
            # flash('Login successful!', 'success')
            # time.sleep(2)
            return redirect(url_for('home'))  # Redirect to a dashboard or another page after successful login
        else:
            flash('Invalid username or password', 'error') 
            # return redirect(url_for('userlogin'))
    return render_template('login.html')

@app.route('/habit')
def habit_tracking():
    return render_template('habit.html')

@app.route('/nutrition')
def nutrition_tracking():
    return render_template('nutrition.html')

@app.route('/fitness')
def fitness_tracking():
    return render_template('fitnesstracker.html')

@app.route('/guide')
def fitness_guide():
    return render_template('fitnessguide.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
