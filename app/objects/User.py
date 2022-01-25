class User :
    __slots__ = ['db', 'username', 'full_name', 'age', 'email', 'phone_number', 'bio', 'privacy_status']


    #TODO change name of the function ro conver_users_db_form_to_dict
    @staticmethod
    def convert_users_data_db_form_to_dict(db_data) :
        for user in db_data :
            yield {
                'username' : user[0],
                'full_name' : user[1],
                'email' : user[2],
                'phone_number' : user[3],
                'age' : user[4],
                'bio' : user[5],
                'privacy_status' : user[6],
            }


    @staticmethod
    def convert_messages_data_db_form_to_dict(db_data) :
        for message in db_data :
            yield {
                    'from' : message[0],
                    'content' : message[1],
            }


    @staticmethod
    def convert_friend_requests_data_db_form_to_dict(db_data) :
        for request in db_data :
            yield {
                    'from' : request[0],
            }

    def __init__(self, user_data:dict, db) :
        self.db = db
        self.username = user_data.get('username', None)
        self.full_name = user_data.get('full_name', None)
        self.age = user_data.get('age', None)
        self.email = user_data.get('email', None)
        self.phone_number = user_data.get('phone_number', None)
        self.bio = user_data.get('bio', None)
        self.privacy_status = user_data.get('privacy_status', None)

#count the number of friends
    def friend_following_count(self) :
        cur = self.db.cursor()
        cur.execute(f'SELECT COUNT(*) FROM `vertices` WHERE `from` = "{self.username}"')
        res = cur.fetchall()
        return res[0][0]
        
    def friend_follower_count(self) :
        cur = self.db.cursor()
        cur.execute(f'SELECT COUNT(*) FROM `vertices` WHERE `to` = "{self.username}"')
        res = cur.fetchall()
        return res[0][0]

#send a friend request to someone 
    def friend_request_send(self, to) :
        cur = self.db.cursor()
        cur.execute(f'INSERT INTO `friend_requests` VALUES (0, "{self.username}", "{to}", 0)')
        self.db.commit()

#craete a vertex and update the friend_request status to 1 -> means that is accepted
    def friend_request_accept(self, to) :
        cur = self.db.cursor()
        cur.execute(f'INSERT INTO `vertices` VALUES (0, "{self.username}", "{to}")')
        self.db.commit()

        cur.execute(f'UPDATE `friend_requests` SET `status` = 1 WHERE `from` = "{self.username}" AND `to` = "{to}" ')
        self.db.commit()

#update the friend_request status to 2 -> means a request that is rejected
    def friend_request_reject(self, to) :
        cur = self.db.cursor()
        cur.execute(f'UPDATE `friend_requests` SET `status` = 2 WHERE `from` = "{self.username}" AND `to` = "{to}" ')
        self.db.commit()

    def friend_requests_get(self) :
        cur = self.db.cursor()
        cur.execute(f'SELECT `from` FROM `friend_requests` WHERE `to` = "{self.username}" AND `status` = 0')
        res = cur.fetchall()
        return res


    def messages_get(self) :
        cur = self.db.cursor()
        cur.execute(f'SELECT `from`, `content` FROM `messages` WHERE `to` = "{self.username}" AND `status` = 0')
        res = cur.fetchall()
        return res


#send a messege to someone
    def messege_send(self, to, text) :
        cur = self.db.cursor()
        cur.execute(f'INSERT INTO `messages` VALUES (0, "{self.username}", "{to}", "{text}", 0)')
        self.db.commit()


# select some users randomly
    def user_random_pick(self, count) :
        cur = self.db.cursor()
        cur.execute(f'select `username`, `full_name`, `email`, `phone_number`, `age`, `bio`, `privacy_status` from users, vertices where users.privacy_status=0 and vertices.from!="{self.username}" and vertices.to!=users.username order by rand() limit {count} ')
        res = cur.fetchall()
        return res

