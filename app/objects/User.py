class User :
    __slots__ = ['db', 'username', 'full_name', 'age', 'email', 'phone_number', 'bio', 'privacy_status']


    @staticmethod
    def convert_db_data_to_dict(db_data) :
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
    def friend_request_send(self, from_, to) :
        cur = self.db.cursor()
        cur.execute(f'INSERT INTO `friend_requests` VALUES (0, "{from_}", "{to}", 0)')
        self.db.commit()

#craete a vertex and update the friend_request status to 1 -> means that is accepted
    def friend_request_accept(self, from_, to) :
        cur = self.db.cursor()
        cur.execute(f'INSERT INTO `vertices` VALUES (0, "{from_}", "{to}")')
        self.db.commit()

        cur.execute(f'UPDATE `friend_requests` SET `status` = 1 WHERE `from` = "{from_}" AND `to` = "{to}" ')
        self.db.commit()

#update the friend_request status to 2 -> means a request that is rejected
    def friend_request_reject(self, from_, to) :
        cur = self.db.cursor()
        cur.execute(f'UPDATE `friend_requests` SET `status` = 2 WHERE `from` = "{from_}" AND `to` = "{to}" ')
        self.db.commit()

#send a messege to someone
    def messege_send(self, from_, to, text) :
        cur = self.db.cursor()
        cur.execute(f'INSERT INTO `messeges` VALUES (0, "{from_}", "{to}", "{text}")')
        self.db.commit()

                                #TODO use self.username instead of from_

# select some users randomly
    def user_random_pick(self, count) :
        cur = self.db.cursor()
        cur.execute(f'select `username`, `full_name`, `email`, `phone_number`, `age`, `bio`, `privacy_status` from users, vertices where users.privacy_status=0 and vertices.from!="{self.username}" and vertices.to!=users.username order by rand() limit {count} ')
        res = cur.fetchall()
        return res
