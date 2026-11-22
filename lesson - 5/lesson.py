#Funcia

def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")

salom_ber()

def salom_ber(ism):
    """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")

salom_ber('hasan')

print(salom_ber.__doc__)

def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
    
toliq_ism("Alisher", "Halmuratov")

def yosh_hisobla(tugilgan_yil, joriy_yil=2026): # joriy yil uchun st.qiymat 2024
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

yosh_hisobla(1998)
yosh_hisobla(1994, 2024)

#Funcia 2

def toliq_ism_yasa(ism, familiya):
    """Toliq isma qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism # qiymat qaytarish uchun return operatorini    ishlatamiz


talaba1 = toliq_ism_yasa('olim','hakimov')
talaba2 = toliq_ism_yasa('hakim','olimov')

print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
    """Toliq isma qaytaruvchi funksiya"""
    if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()

talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
avtolar = [avto1, avto2]
print('Onlayn bozordagi mavjud avtomashinalar:')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
    
def oraliq(min,max):
    sonlar = [] # bo'sh ro'yxat
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar

print(oraliq(0,10))
print(oraliq(10,21))

print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting",end='')
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narhi=input("Narhi: ")
    
    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break
    
print(avtolar)