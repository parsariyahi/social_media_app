# basic Web social media app

## about the project

this project is based on instagram logic

its a web app written with Flask

this project is a personal student learning project

## written with

- [python](https://www.python.org)
- [flask](https://flask.palletsprojects.com)
- [nicepage](https://www.nicepage.com)
- [mysql](https://www.mysql.com)

## how to use

### install the requirements
```bash
pip install -r requirements.txt
```

### put your database params in [app/src/consts/CONSTS.py](https://github.com/parsariyahi/social_media_app/blob/master/app/src/consts/CONSTS.py) and edit the SECRET_KEY const
```python
"""
this project is using mysql
but because of SQLAlchemy
you can use your favorite dbms
"""

DBMS='<your db provider>' 
DB_HOST='<your host>'
DB_NAME='<your db name>'
DB_USER='<your user>'
DB_PASSWORD='<your users password>'

"""
:pattern <dbms>://<username>:<password>@host/<database name>
"""

#this will create engine pattern for SQLAlchemy
SQLALCHEMY_DATABASE_URI=f"{DBMS}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SECRET_KEY = '<some random strings>'
```

### for the fist time, uncomment these lines in [app/app.py](https://github.com/parsariyahi/social_media_app/blob/master/app/app.py) to initialize database tables
```python
app = Flask(__name__)
app.secret_key = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

""" 
uncomment these lines,
to create the database tables
"""
db.drop_all(app=app) #<--- this
db.create_all(app=app) #<--- this
```

### then run this command
```bash
python app/app.py
```