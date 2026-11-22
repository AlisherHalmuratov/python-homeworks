class user:
    def __init__(self, name, age, gmail):
        self.name = name
        self.age = age
        self.gmail = gmail
        self.bio = f"{self.name} \n {self.age} \n {self.gmail}"

    def get_info(self):
        print(self.bio)

    def get_full_name(self):
        self.last_name = input("input last name: ")
        return self.last_name, self.name

    def get_gmail(self):
        print(f"user gmail: {self.gmail}")

user1 = user("Alisher", 15, "alisherhalmuratova630@gmail.com")
print(user1.get_info())
print(user1.get_gmail())
print(user1.get_full_name())
