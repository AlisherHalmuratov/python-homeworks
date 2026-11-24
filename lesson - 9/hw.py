#1
class Talaba:
    def __init__(self):
        self.fanlar = []
        
    def fanga_yozil(self, fan):
        self.fanlar.append(fan)
        
    def remove_fan(self, fan):
        if fan not in self.fanlar:
            return "вы не записаны на этот предмет"
        else:
            self.fanlar.remove(fan)
        
class Fan:
    def __init__(self, fan):
        self.fan = fan
        
matematika = Fan("matematika")
fizika = Fan("Физика")

talaba1 = Talaba()

talaba1.fanga_yozil(matematika)
talaba1.fanga_yozil(fizika)

talaba1.remove_fan(matematika)

print(talaba1.fanlar)

#2
class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
        
    def get_info(self):
        info = f"person name = {self.name.title()}, last name = {self.last_name.title()}, age = {self.age}"
        return info
    
class User(Person):
    def __init__(self, name, last_name, age, mail, id):
        super().__init__(name, last_name, age)
        self.mail = mail
        self.id = id
        self.base = []
        self.is_banned = False
        
    def get_info(self):
        info = f"user name = {self.name.title()}, last name = {self.last_name.title()}, age = {self.age}, mail = {self.mail}, id = {self.id}"
        return info
    
    def get_input(self):
        if self.is_banned:
            print("пользовотель заблокирован")
        else:
            self.user_input = input("введите текст мы запишем его в базу данных: ")
            self.base.append(self.user_input)
        
class Admin(User):
    def __init__(self, name, last_name, age, mail, id):
        super().__init__(name, last_name, age, mail, id)
        
    def can_ban(self, user):
        ban_input = input("выберите того пользовотеля которого хоитите забанить: ")
        if ban_input.lower() == user.name.lower():
            user.is_banned = True 
            return f"пользователь {user.name.lower()} забанен"
        else:
            return "такого пользователя не существует"

class Base:
    def __init__(self, base):
        self.base = base
        
    def show_base(self):
        if self.base:
            print(f"база = {self.base}")
        else:
            print("в базе нечего нету")

user1 = User("alisher", "halmuratov", 15, "alisherhalmuratov226@gmail.com", "741258963")
admin1 = Admin("Jonibek", "uralov", 25, "jonibekuralov662@gmail.com", "963258741")
    
base = Base(user1.base)

print(user1.get_info())
user1.get_input()
base.show_base()

print(admin1.get_info())
admin1.can_ban(user1)
user1.get_input()

base.show_base()