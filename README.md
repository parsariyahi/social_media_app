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

```bash
pip install -r requirements.txt
```

### for the fist time, uncomment these lines in app/app.py to initialize database tables
```python
app = Flask(__name__)
app.secret_key = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

""" 
uncomment these lines,
to create the database tables
"""
db.drop_all(app=app)
db.create_all(app=app)
```

```bash
python app/app.py
```