from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from models import User
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

#Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/healthtracker'

#Initialize the Database
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
