#1
while True:
    trafic_input = input("Введите цвет светофора: ")
    if trafic_input.lower() == "зеленый" or trafic_input.lower() == "желтый" or trafic_input.lower() == "красный":
        print("Правильно подходит!")
        break
    else:
        print("Неправильно попробуйте еще")
        continue
    
#2
import random

random_num = random.randint(1, 10)

while True:
    user_input = int(input("Попробуйте угадать рандомное число от 1 до 10: "))
    if user_input == random_num:
        print("Правильно :) поздровляю!")
        break
    elif user_input == 67:
        print("серьезно? SIX SEVEN")
    else:
        print("Неправльно :( попробуйте еще раз")
    
#3
print("МЫ делаем список ваших друзей что бы прекратить добовлять имена напишите stop")
friends = []
n = 1
while True:
    friend_name = input(f"{n} - Введите имя друга: ")
    n += 1
    if friend_name.lower() == "stop":
        break
    friends.append(friend_name)
for name in friends:
    print(name.title())
    
#4
while True:
    kurs_som = 12600
    som = input("Введите сумм что бы конвертировать его в доллары🤑: ")
    if som.lower() == "exit":
        break
    som = float(som)
    usd = som / kurs_som
    print(f"{som} сом равен {usd} доллорам")