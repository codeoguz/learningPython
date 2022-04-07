#functions

#def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

""" def myFunction(urunAdi,/ ,fiyati, *, fotograf, ):
    print('Urunun adi: ', urunAdi, '|  Urun fiyati: ', fiyati)

myFunction('TRIPOD', 30,  fotograf='image1.png') """


#lists

""" calisanlar = []
print(calisanlar)

calisanlar.append('Omer')
calisanlar.append('Oguz')

print('Sonra',calisanlar)

calisanlar.pop()

print('Pop',calisanlar)
 """


yemekler = ['iskender', 'bonfile', 'iskender']
print('Duplicate elements', yemekler)

#tuples



#sets   

""" setsYemek = {'iskender', 'bonfile', 'iskender', 'djasjd'}
print('Sets elements', setsYemek)
 """
#dictionaries

distionary = {'ok': 'tamam', 'sayi': 15}

omer = {'name': 'Omer', 'gender': 'male'}
kubra = {'name': 'kubra', 'gender': 'female'}
kaan = {'name': 'kaan', 'gender': 'male'}

users = [omer, kubra, kaan]

result = []

for user in users:
    if(user['gender'] == 'male'):
       result.append(user['name']) 

print(result)