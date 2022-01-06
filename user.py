class User :
    __slots__ = ['id', 'username', 'full_name', 'age', 'email', 'phone_number', 'bio', 'privacy_status']

    def __init__(self, **user_data) :
        self.id = user_data.get('id', None)
        self.username = user_data.get('username', None)
        self.full_name = user_data.get('full_name', None)
        self.age = user_data.get('age', None)
        self.email = user_data.get('email', None)
        self.phone_number = user_data.get('phone_number', None)
        self.bio = user_data.get('bio', None)
        self.privacy_status = user_data.get('privacy_status', None)
    
