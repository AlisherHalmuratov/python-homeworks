def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

print(summa(1,2))
print(summa(1,2,3,4,5))

def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return sum(sonlar)

print(summa(4,5,6,7))

def summa(x,y,*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return x+y+sum(sonlar)

print(summa(2, 5, 7, 8))

def avto_info(kompaniya,model,**malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qay.funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar

avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)

print(avto1)
print(avto2)

#Lambda

import math

uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))

product = lambda x, y : x ** y
print(product(3, 2))

def daraja(n):
    return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")

from math import sqrt

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
ildizlar = list(map(sqrt,sonlar))
print(ildizlar)

numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)

print(list(result))

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati

# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x

print(list(map(lambda x: x*x,sonlar))) # sonlar ning kvadratini hisoblaymiz

a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)

ismlar = ['hasan','husan','olim','umid']
print(list(map(lambda matn:matn.upper(),ismlar)))

import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar

# def juftmi(x):
#     """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
#     return x%2==0

juft_sonlar = list(filter(lambda x: x%2==0,sonlar))
print(sonlar)
print(juft_sonlar)

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
juft_sonlar = list(filter(lambda son: son%2==0,sonlar))

print(sonlar)
print(juft_sonlar)

mevalar =['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
print(mevalar_b)

mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)