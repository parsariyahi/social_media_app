from flask import Flask, render_template, request
import mysql.connector
import database.db_oprations as db


conn = mysql.connector.connect(
  host="localhost",
  database="pars_messenger",
  user="prrh",
  password="parsa1981",
)


app = Flask(__name__)


@app.route("/login")
def index() :
    return render_template("login.html")


@app.route("/register")
def register() :
    return render_template("register.html")

@app.route("/profile", methods=["GET","POST"])
def profile() :
    if request.form.get('register', None) and not request.form.get('login', None) :
        return 'register'
    if request.form.get('login', None) and not request.form.get('register', None) :
        username = request.form['username']
        password = request.form['password']
        
        user = db.user_get_data(conn, username, password)
        
        return user
    return render_template("login.html")

if __name__ == "__main__" :
    app.run()
