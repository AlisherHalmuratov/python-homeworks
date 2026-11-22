car_0 = {'model':'ferrari', 'rang':'qizil'}
print(car_0)
print(car_0['model'])
print(car_0['rang'])

talaba_0 = {'ism':'ali', 'yosh':15, 't_yill':2011}
print(f'{talaba_0['ism'].title()},\
    {talaba_0['yosh']} yoshda,\
    {talaba_0['t_yill']}  yilda togilgan')

talaba_0['sinif'] = 9
talaba_0['fakultet'] = 'informatika'

print(talaba_0)

talaba_1 = {}

talaba_1['ism'] = 'alisher'
talaba_1['yosh'] = 14
talaba_1['sinif'] = 9
print(talaba_1)
print(f'Talaba {talaba_1["ism"].title()} {talaba_1['sinif']} - sinif')

del talaba_0['yosh']
print(talaba_0)

telefonlar = {
    'ali':'honor x7d',
    'vali':'huawei x6',
    'zufar':'poco',
    'gech':'nokia 3310'
    }

phone = telefonlar['ali']
print(f'Alini telephoni - {phone}')

phone = telefonlar.get('hasan', 'bunday phone yok')
print(phone)