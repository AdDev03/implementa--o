from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '21aceda4d8254352b47a4b407cd54c7f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/tcc'

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)