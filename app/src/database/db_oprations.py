from hashlib import md5




class Db : 
    __slot__ = ['db']

    def __init__(self, db) :
        self.db = db

    #get all users data
    def user_login(self, username: str, password: str) :
        cur = self.db.cursor()
        password = md5(password.encode('utf8')).hexdigest()
        cur.execute(f'SELECT `username`, `full_name`, `email`, `phone_number`, `age`, `bio`, `privacy_status` FROM `users` WHERE `username` = "{username}" AND `password` = "{password}" ')
        res = cur.fetchall()
        return res

    def user_get_data(self, username: str) :
        cur = self.db.cursor()
        cur.execute(f'SELECT `username`, `full_name`, `email`, `phone_number`, `age`, `bio`, `privacy_status` FROM `users` WHERE `username` = "{username}" ')
        res = cur.fetchall()
        return res

    #add user for registering a user
    def user_add(self, user_data:dict) -> bool:
        cur = self.db.cursor()
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
        self.db.commit()
        return True


    def send_message(self, from_: str, to: str, title: str, message: str) -> None:
        cur = self.db.cursor()
        cur.execute(f'INSERT INTO `messages` VALUES (0, "{from_}", "{to}", "{title}", "{message}") ')
        self.db.commit()



    #craete a vertex and update the friend_request status to 1 -> means that is accepted
    def friend_request_accept(self, from_, to) :
        cur = self.db.cursor()
        cur.execute(f'UPDATE `friend_requests` SET `status` = 1 WHERE `from` = "{from_}" AND `to` = "{to}" ')
        self.db.commit()

        cur = self.db.cursor()
        cur.execute(f'INSERT INTO `vertices` VALUES (0, "{from_}", "{to}")')
        self.db.commit()

    #update the friend_request status to 2 -> means a request that is rejected
    def friend_request_reject(self, from_, to) :
        cur = self.db.cursor()
        cur.execute(f'UPDATE `friend_requests` SET `status` = 2 WHERE `from` = "{from_}" AND `to` = "{to}" ')
        self.db.commit()


    def friend_request_send(self, from_, to) :
        cur = self.db.cursor()
        cur.execute(f'INSERT INTO `friend_requests` VALUES (0, "{from_}", "{to}", 0)')
        self.db.commit()

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
