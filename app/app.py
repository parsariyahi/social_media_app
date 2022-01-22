from flask import Flask, render_template, request, redirect, url_for
from objects.User import User
import mysql.connector
import database.db_oprations as db

#our mysql connection
conn = mysql.connector.connect(
  host="localhost",
  database="pars_messenger",
  user="prrh",
  password="parsa1981",
)


app = Flask(__name__)


@app.route("/")
@app.route("/login")
def index() :
    error = int(request.args.get('error', 0))
    context = {
            'error' : error
            }
    return render_template("login.html", context=context)


@app.route("/register")
def register() :
    context = {}
    return render_template("register.html", context=context)

@app.route("/profile", methods=["GET","POST"])
def profile() :
    context = {}
    if request.form.get('register', None) and not request.form.get('login', None) :
        new_user = {
                'username' : request.form.get('username', None),
                'full_name' : request.form.get('full_name', None),
                'email' : request.form.get('email', None),
                'phone_number' : request.form.get('phone_number', None),
                'age' : request.form.get('age', None),
                'bio' : request.form.get('bio', None),
                'privacy_status' : request.form.get('privacy_status', None),
                'password' : request.form.get('password', None),
            }

        db.user_add(conn, new_user)

        del new_user['password']
        context['user'] = User(new_user, conn)
        return render_template("profile/main.html", context=context)

    if request.form.get('login', None) and not request.form.get('register', None) :
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        user = db.user_get_data(conn, username, password)

        if user :
            user = {
                'username' : user[0][0],
                'full_name' : user[0][1],
                'email' : user[0][2],
                'phone_number' : user[0][3],
                'age' : user[0][4],
                'bio' : user[0][5],
                'privacy_status' : user[0][5],
            }
            context['user'] = User(user, conn)
            #context['user'] = user
            return render_template("profile/main.html", context=context)

        return redirect(url_for('index', error=1))

    return render_template("login.html", context=context)

if __name__ == "__main__" :
    app.run()