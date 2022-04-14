DBMS='mysql'
DB_HOST='localhost'
DB_NAME='pars_messenger'
DB_USER='prrh'
DB_PASSWORD='parsa1981'
"""
:pattern <dbms>://<username>:<password>@host/<database name>
"""
SQLALCHEMY_DATABASE_URI=f"{DBMS}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SECRET_KEY = '3PVj9PQaadsffasdfm6'
