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


def set_context_profile(user: User) -> dict :
    """ This is just for Dont repeat your self 
    and its not a primary function
    """
    return {
        'recomendation' : user.user_recomendation(3),
        'requests' : user.friend_request_get(3),
        'messages' : user.message_get(3),
        'following_count': user.friend_following_count(),
        'follower_count': user.friend_follower_count(),
    }


def get_error() :
    """ If we have error in our opration 
    we will pass that error with get method 
    this function will get the error code
    """
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

    if session['user'] :
        user = User(session['user'], conn)
        context = set_context_profile(user)
        return render_template("profile/index.html", context=context)
    
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
        user = User(new_user, conn)

        """
        in session we store the user information without password
        """
        session['user'] = new_user

        context = set_context_profile(user)

        return render_template("profile/index.html", context=context)

    if request.form.get('login', None) and not request.form.get('register', None) :
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        user = db.user_login(conn, username, password)

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

            session['user'] = user
            user = User(user, conn)

            context = set_context_profile(user)

            return render_template("profile/index.html", context=context)

        """
        if user was not found
        this will redirect user with an error code with get method
        """
        return redirect(url_for('index', error=1))

    """
    the 5 is a code number for ' user not found '
    """
    context = {'error': 5}
    return render_template("login.html", context=context)


@app.route("/msg/send", methods=['POST'])
def msg_send() :
    if request.form.get('msg_send', None) :
        user = session.get('user', None)
        if user :
            to = request.form.get('username', None)
            title = request.form.get('title', None)
            message = request.form.get('message', None)

            if to and title and message :
                db.send_message(conn, user['username'], to, title, message)

                return redirect(url_for('profile'))

    return render_template("login.html", context = {})


@app.route("/req/accept/", methods=['GET'])
def request_accept() :
    req_username = request.args.get('req_username', '')
    if req_username :
        db.friend_request_accept(conn, req_username, session['user']['username'])

        return redirect(url_for('profile'))

@app.route("/req/reject/", methods=['GET'])
def request_reject() :
    req_username = request.args.get('req_username', '')
    if req_username :
        db.friend_request_reject(conn, req_username, session['user']['username'])

        return redirect(url_for('profile'))

@app.route("/req/send/", methods=['GET'])
def request_send() :
    req_username = request.args.get('req_username', '')
    if req_username :
        db.friend_request_send(conn, session['user']['username'], req_username)

        return redirect(url_for('profile'))

if __name__ == "__main__" :
    app.debug = True
    app.run()
