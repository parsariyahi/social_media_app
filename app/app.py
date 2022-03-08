from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector
from objects.User import User
import database.db_oprations as db


HOST = 'localhost'
DATABASE = 'pars_messenger'
USER = 'prrh'
PASSWORD = 'parsa1981'

conn = mysql.connector.connect(
   host=HOST,
   database=DATABASE,
   user=USER,
   password=PASSWORD,
)



"""
if we have error in our opration 
we will pass that error with get method 
this function will get the error code
"""
def get_error() :
    return int(request.args.get('error', 0))


app = Flask(__name__)
app.secret_key = '3PVj9PQam6'

"""
index page and login page are the same
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
        session['username'] = new_user['username']

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
            session['username'] = context['user']

            return render_template("profile/index.html", context=context)

        """
        if user was not found
        this will redirect user with an error code with get method
        """
        return redirect(url_for('index', error=1))

    return render_template("login.html", context=context)


@app.route("/msg/send", methods=['GET', 'POST'])
def msg_send() :
    if request.form.get('msg_send', None) :
        user = session.get('username', None)
        if user :
            to = request.form.get('username', None)
            title = request.form.get('title', None)
            message = request.form.get('message', None)

            if to and title and message :
                user.message_send(to, title, message)
                context = { 'user' : user }

                render_template("profile/index.html", context=context)

    render_template("login.html", context = {})
    


if __name__ == "__main__" :
    app.debug = True
    app.run()
