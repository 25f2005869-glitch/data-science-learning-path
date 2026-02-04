#ERROR

class student:
    def __init__(self, name):
        self.name = name

s1 = student("saloni")
print(s1.name)
del s1.name
print(s1.name)

#ERROR

class account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc__pass = acc_pass
    
acc1 = account("12345", "abcde")

print(acc1.acc_no)
print(acc1.__acc__pass)

#ERROR

class account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc__pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)
    
acc1 = account("12345", "abcde")

print(acc1.acc_no)
print(acc1.__acc_pass)

class account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)
    
acc1 = account("12345", "abcde")

print(acc1.acc_no)
print(acc1.reset_pass())

class person:
    __name = "anonymous"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()

p1 = person()

print(p1.welcome())

class car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyotacar(car):
    def __init__(self, name):
        self.name = name

car1 = Toyotacar("fortuner")
car2 = Toyotacar("prius")

class car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyotacar(car):
    def __init__(self, name):
        self.name = name

car1 = Toyotacar("fortuner")
car2 = Toyotacar("prius")

print(car1.name)

class car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyotacar(car):
    def __init__(self, name):
        self.name = name

car1 = Toyotacar("fortuner")
car2 = Toyotacar("prius")

print(car1.start())

class car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyotacar(car):
    def __init__(self, name):
        self.name = name

car1 = Toyotacar("fortuner")
car2 = Toyotacar("prius")

print(car1.color)





