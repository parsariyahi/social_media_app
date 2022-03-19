class User :
    __slots__ = ['db', 'username', 'full_name', 'age', 'email', 'phone_number', 'bio', 'privacy_status']

    @staticmethod
    def __convert_users_db_form_to_dict(db_data) :
        for user in db_data :
            yield {
                'username' : user[0],
                'full_name' : user[1],
                'email' : user[2],
                'phone_number' : user[3],
                'age' : user[4],
                'bio' : user[5],
            }

    @staticmethod
    def __convert_messages_db_form_to_dict(db_data) :
        for message in db_data :
            yield {
                    'from' : message[0],
                    'title' : message[1],
                    'content' : message[2],
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

    def friend_request_get(self, limit=0) :
        result = []
        if limit :
            cur = self.db.cursor()
            cur.execute(f'select `username`, `full_name`, `email`, `phone_number`, `age`, `bio` from friend_requests join users where friend_requests.from = users.username and friend_requests.to = "{self.username}" and friend_requests.status = 0 limit {limit}')
            res = cur.fetchall()
            for user in self.__convert_users_db_form_to_dict(res) :
                result.append(user)
        else :
            cur = self.db.cursor()
            cur.execute(f'select `username`, `full_name`, `email`, `phone_number`, `age`, `bio` from friend_requests join users where friend_requests.from = users.username and friend_requests.to = "{self.username}" and friend_requests.status = 0')
            res = cur.fetchall()
            for user in self.__convert_users_db_form_to_dict(res) :
                result.append(user)

        return result

#send a messege to someone
    def messege_send(self, to, title, text) :
        cur = self.db.cursor()
        cur.execute(f'INSERT INTO `messages` VALUES (0, "{self.username}", "{to}", "{title}", "{text}", 0)')
        self.db.commit()


    def message_get(self, limit=0) :
        result = []
        if limit :
            cur = self.db.cursor()
            cur.execute(f'SELECT `from`, `title`, `content` FROM `messages` WHERE `to` = "{self.username}" limit {limit}')
            res = cur.fetchall()
            
            for message in self.__convert_messages_db_form_to_dict(res) :
                result.append(message)

        else :
            cur = self.db.cursor()
            cur.execute(f'SELECT `from`, `title`, `content` FROM `messages` WHERE `to` = "{self.username}" ')
            res = cur.fetchall()
            
            for message in self.__convert_messages_db_form_to_dict(res) :
                result.append(message)

        return result



# select some users (only public users) randomly for recomending to user
    def user_recomendation(self, count) :
        result = []
        cur = self.db.cursor()
        cur.execute(f'select `username`, `full_name`, `email`, `phone_number`, `age`, `bio` from users left join vertices on vertices.from!="{self.username}" and vertices.to!=users.username  where users.privacy_status=1 order by rand() limit {count} ')
        res = cur.fetchall()

        for user in self.__convert_users_db_form_to_dict(res) :
            result.append(user)

        return result

