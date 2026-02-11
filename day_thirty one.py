class SecurityError(Exception):
    
    def __init__(self,message):
        print(message)

    def logout(self):
        print('logout')

class Google:

    def __init__(self,name,email,password,device):
        self.name = name
        self.email = email
        self.password = password
        self.device = device

    def login(self,name,email,password,device):
        if device != self.device:
            raise SecurityError
        if email == self.email and password == self.password:
            print('welcome')
        else:
            print('login error')

obj = Google('nitish','nitish@gmail.com','1234','android')

try:
    obj.login('nitish@gmail.com','1234','android')
except SecurityError as e:
    e.logout()
else:
    print#(self.name)
finally:
    print('database connection closed')

#This gives us error.

class SecurityError(Exception):
    
    def __init__(self,message):
        print(message)

    def logout(self):
        print('logout')

class Google:

    def __init__(self,name,email,password,device):
        self.name = name
        self.email = email
        self.password = password
        self.device = device

    def login(self,name,email,password,device):
        if device != self.device:
            raise SecurityError
        if email == self.email and password == self.password:
            print('welcome')
        else:
            print('login error')

obj = Google('nitish','nitish@gmail.com','1234','android')

try:
    obj.login('nitish@gmail.com','1234','android')
except SecurityError as e:
    e.logout()
else:
    print(obj.name)
finally:
    print('database connection closed')

class SecurityError(Exception):
    
    def __init__(self,message):
        print(message)

    def logout(self):
        print('logout')

class Google:

    def __init__(self,name,email,password,device):
        self.name = name
        self.email = email
        self.password = password
        self.device = device

    def login(self,name,email,password,device):
        if device != self.device:
            raise SecurityError('there is a problem')
        if email == self.email and password == self.password:
            print('welcome')
        else:
            print('login error')

obj = Google('nitish','nitish@gmail.com','1234','android')

try:
    obj.login('nitish@gmail.com','1234','window')
except SecurityError as e:
    e.logout()
else:
    print#(self.name)
finally:
    print('database connection closed')    