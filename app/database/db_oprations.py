from hashlib import md5


#get all users data
def user_get_data(db, username: str, password: str) :
    cur = db.cursor()
    password = md5(password.encode('utf8')).hexdigest()
    cur.execute(f'SELECT `username`, `full_name`, `email`, `phone_number`, `age`, `bio`, `privacy_status` FROM `users` WHERE `username` = "{username}" AND `password` = "{password}" ')
    res = cur.fetchall()
    return res

#add user for registering a user
def user_add(db, user_data:dict) -> bool:
    cur = db.cursor()
    username = user_data.get('username', None)
    if not username :
        return False
        #TODO raise an error here
    full_name = user_data.get('full_name', None)
    email = user_data.get('email', None)
    phone_number = user_data.get('phone_number', None)
    age = int(user_data.get('age', None))
    bio = user_data.get('bio', None)
    privacy_status = int(user_data.get('privacy_status', None))
    password = user_data.get('password', '') 
    password = md5(password.encode('utf8')).hexdigest()

    cur.execute(f'INSERT INTO `users` VALUES (0, "{username}", "{full_name}", "{email}", "{phone_number}", {age}, "{bio}", {privacy_status}, "{password}") ')
    db.commit()
    return True


def send_message(db, from_: str, to: str, title: str, message: str) -> None:
    cur = db.cursor()
    cur.execute(f'INSERT INTO `messages` VALUES (0, "{from_}", "{to}", "{title}", "{message}") ')
    db.commit()

#data = {
#        "username" : "mmd",
#        "full_name" : "mmd por",
#        "age" : 20,
#        "email" : "mmd@gmail.com",
#        "phone_number" : "09123456986",
#        "bio" : "bad bitch",
#        "privacy_status" : 1, 
#        "password" : "mmd1234",
#        }
#
#user_add(mydb, data)
#user = user_get_data(mydb, "mmd", "mmd1234")
#print(user)
