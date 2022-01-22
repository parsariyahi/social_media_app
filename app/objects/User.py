class User :
    __slots__ = ['db', 'username', 'full_name', 'age', 'email', 'phone_number', 'bio', 'privacy_status']

    def __init__(self, user_data:dict, db) :
        self.db = db
        self.username = user_data.get('username', None)
        self.full_name = user_data.get('full_name', None)
        self.age = user_data.get('age', None)
        self.email = user_data.get('email', None)
        self.phone_number = user_data.get('phone_number', None)
        self.bio = user_data.get('bio', None)
        self.privacy_status = user_data.get('privacy_status', None)

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
    def friend_request_send(self, db, from_, to) :
        cur = db.cursor()
        cur.execute(f'INSERT INTO `friend_requests` VALUES (0, "{from_}", "{to}", 0)')
        db.commit()

#craete a vertex and update the friend_request status to 1 -> means that is accepted
    def friend_request_accept(self, db, from_, to) :
        cur = db.cursor()
        cur.execute(f'INSERT INTO `vertices` VALUES (0, "{from_}", "{to}")')
        db.commit()

        cur.execute(f'UPDATE `friend_requests` SET `status` = 1 WHERE `from` = "{from_}" AND `to` = "{to}" ')
        db.commit()


#update the friend_request status to 2 -> means a request that is rejected
    def friend_request_reject(self, db, from_, to) :
        cur = db.cursor()
        cur.execute(f'UPDATE `friend_requests` SET `status` = 2 WHERE `from` = "{from_}" AND `to` = "{to}" ')
        db.commit()

#send a messege to someone
    def messege_send(self, db, from_, to, text) :
        cur = db.cursor()
        cur.execute(f'INSERT INTO `messeges` VALUES (0, "{from_}", "{to}", "{text}")')
        db.commit()

