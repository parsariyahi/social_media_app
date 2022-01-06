import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database="pars_messenger",
  user="prrh",
  password="parsa1981",
)

#get all users data
def user_get_data(db, username) :
    cur = db.cursor()
    cur.execute(f'SELECT * FROM `users` WHERE `username` = "parsa" ')
    res = cur.fetchall()
    return res

#add user for registering a user
def user_add(db, user_data:dict) :
    cur = db.cursor()
    username = user_data.get('username', None)
    full_name = user_data.get('full_name', None)
    age = user_data.get('age', None)
    email = user_data.get('email', None)
    phone_number = user_data.get('phone_number', None)
    bio = user_data.get('bio', None)
    privacy_status = user_data.get('privacy_status', None)
    password = user_data.get('password', None)

    cur.execute(f'INSERT INTO `users` VALUES (0, "{username}", "{full_name}", "{age}", "{email}", "{phone_number}", "{bio}", "{privacy_status}", "{password}") ')
    db.commit()



user = user_get_data(mydb, 'mina')

print(user)


data = {
        "username" : "ali",
        "full_name" : "ali por",
        "age" : 20,
        "email" : "ali@gmail.com",
        "phone_number" : "09123456758",
        "bio" : "bad bitch",
        "privacy_status" : 0, 
        "password" : "ali1234",
        }

user_add(mydb, data)
