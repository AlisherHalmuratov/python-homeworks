#1
ob_xavo = int(input("ob havo kiriting: "))

if ob_xavo < 0:
    print("Sovuq")
elif ob_xavo >= 0 and ob_xavo <= 20:
    print("Salqn")
elif ob_xavo >= 21 and ob_xavo <= 30:
    print("Iliq")
elif ob_xavo >= 31:
    print("Issik")
    
#2
summa = float(input("summa kiriting: "))
chegirma = 0

if summa < 50000:
    print("chegirma yo'q")
    chegirma = 0
elif summa >= 50000 and summa <= 100000:
    print(f'5% chegirma')
    chegirma = 5
elif summa > 100000:
    print(f'10% chegirma')
    chegirma = 10
    
#3
login = input("login kiriting:")
parol = int(input("parol kiriting:"))

if login == "admin" and parol == 12345:
    print("Xush kelibsiz, admin!")
else:
    print("get are here")
    
#4
age = int(input("yoush kiriting:"))

if age < 13:
    print("Sizga ushbu film tavsiya etilmaydi")
elif age >= 13 and age <= 17:
    print("Siz filmni ota-onangiz bilan ko'rishingiz mumkin")
elif age >= 18:
    print("Siz filmni tomosha qilishingiz mumkin")
    
#5
menu = input("1 dan 3 gacha taomni tanlang 1 osh 2 mastava 3 shashlik")

osh = [15000, 15]
mastava = [12000, 30]
shashlik = [10000, 10]

if menu == 1:
    print(f"vaqt {osh[1]} pul {osh[0]}")
elif menu == 2:
    print(f"vaqt {mastava[1]} pul {mastava[0]}")
elif menu == 3:
    print(f"vaqt {shashlik[1]} pul {osh[0]}")

#6
email = input("email: ")

if email.find("@") == -1 and email.find(".") == -1 :
    print("Noto'g'ri email manzili")
else:
    print("Email qabul qilindi")

#7
baho = int(input("baho: "))

if baho < 55:
    print("2")
elif baho < 69:
    print("3")
elif baho < 85:
    print("4")
else:
    print("5")

#6
summa = int(input("kartangizni pulini kiriting"))
yech = int(input("kartadan yechib oladigan pulingizni kirirting"))

protsent = summa / 100

if summa < yech:
    print("kartangizni mablagi yetarli emas")
elif summa == yech:
    print(f"minimal {summa + protsent}")
else:
    print("pul yechildi")

#9
kun = input("kuni kirizing: ")

if kun == "shanba" or kun == "yakshanba":
    print("bugun dam olish kuni")
else:
    print("bugun ish kuni")

#10
mobil = int(input("necha GB tarif hohlaysiz?"))

if mobil < 1:
    print("sizga MINI tarifi mos keladi")
elif mobil < 5:
    print("sizga ortacha tarifi mos keladi")
else:
    print("sizga UNLIMITE tarifi mos keladi")
