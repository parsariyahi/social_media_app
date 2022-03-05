from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from objects.User import User
import database.db_oprations as db

conn = mysql.connector.connect(
   host="localhost",
   database="pars_messenger",
   user="root",
   password="",
)


"""
if we have error in our opration 
we will pass that error with get method 
this function will get the error code
"""
def get_error() :
    return int(request.args.get('error', 0))


app = Flask(__name__)


"""
our index page and login page are the same
"""
@app.route("/")
@app.route("/login")
def index() :
    context = { 'error' : get_error() }
    return render_template("login.html", context=context)

@app.route("/register")
def register() :
    context = { 'error' : get_error() }
    return render_template("register.html", context=context)

@app.route("/profile", methods=["GET","POST"])
def profile() :
    context = {}
    
    """
    check if user is registering or logining
    """

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

        """
        if user can not register
        this will redirect user to register page
        with an error code in get method
        """
        try :
            db.user_add(conn, new_user)
        except :
            return redirect(url_for('register', error=1))


        """
        delete password from new_user var and make a object from User class
        """

        del new_user['password']
        context['user'] = User(new_user, conn)

        return render_template("profile/index.html", context=context)

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
                'privacy_status' : user[0][6],
            }

            """
            context['user'] is an object of User class
            we send object itself to profile/main.html
            so we can do user oprations easier
            """

            context['user'] = User(user, conn)
            return render_template("profile/index.html", context=context)

        """
        if user was not found
        this will redirect user with an error code with get method
        """
        return redirect(url_for('index', error=1))

    return render_template("login.html", context=context)

if __name__ == "__main__" :
    app.debug = True
    app.run()
