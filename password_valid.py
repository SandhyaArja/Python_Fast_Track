class User:
    def __init__(self,username,password):
        self._username=username
        self._password=password 
    
    @ property 
    def username(self):
        return self._username 
    
    @property 
    def password(self):
        return self._password 
        
    
    
    @password.setter 
    
    def password(self,new_pass):
        if len(new_pass)<8:
            raise ValueError ("Password must be at least 8 characters")
        self._password=new_pass
        
user=User("priyanka","secure password")
print(user.username)
print(user.password)
user.password='sand'
print(user.password)
