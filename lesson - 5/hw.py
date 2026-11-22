#1

def user_data(first_name, last_name, age):
    print(f"Ism: {first_name.title()} \nFamiliya: {last_name.title()} \nYosh:{age}")
first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
age = int(input("Введите возраст: "))

user_data(first_name, last_name, age)

#2
def find_max(a=0, b=0, c=0):
    max_num = max(a,b,c)
    if a == b == c:
        print(f"Самые большие цифра = A, B, C цифра: {max_num}")
    elif a == b == max_num:
        print(f"Самые большие цифра = A, B цифра: {max_num}")
    elif a == max_num == c:
        print(f"Самые большие цифра = A, C цифра: {max_num}")
    elif max_num == b == c:
        print(f"Самые большие цифра = B, C цифра: {max_num}")
    elif a == max_num:
        print(f"Самые большие цифра = A цифра: {max_num}")
    elif b == max_num:
        print(f"Самые большие цифра = B цифра: {max_num}")  
    elif c == max_num:
        print(f"Самые большие цифра = C цифра: {max_num}")
    
a = int(input("введите a: "))
b = int(input("введите b: "))
c = int(input("введите c: "))    
        
find_max(a, b, c)

#3
def find_letter_count(word, letter):
    n = 0
    for char in word.lower():
         if char == letter.lower():
             n += 1
    if letter.lower() in word.lower():
        print(f"в слове {word} буква '{letter}' встречается {n} раз")
    else:
        print("такой буквы в слове нету")
        
word_found = input("Напишите слово: ")
letter_found = input("Напишите букву которую хотите найти в слове: ")

find_letter_count(word_found, letter_found)
    
#4
def list_sum(myList):
    summ = sum(myList)
    print(f"Listning elementlar yig'indisi = {summ}")

result = [2, 5, 2, 3, 5, 5, 10]
list_sum(result)

#5
def daraja(a, b):
    print(a ** b)

daraja(2, 5)

#6
def daraja4(a, b, c, d):
    print(a ** b)
    print(a ** c)
    print(a ** d)
    
daraja4(2, 5, 8, 6)