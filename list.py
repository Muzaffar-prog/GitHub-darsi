# bugungi dars list bilan ishlash

# moshinalar = ['tesla', 'GM', 'BMW', 'Audi']
# bozorlik = ['gosht', 'olma', 'sabzi', 'yog']
# sonlar = [123, 345, 12, 40]
# aralash = ['salom', 'hello', 1,2,3,4,5, 10.2]
# royxat = []   # bo'sh ro'yxat!
# print(aralash)




# telefonlar = ['iphone', 'redmi', 'samsung', 'oppo', 'mi']
#
# print("Birinchi telefon: ", telefonlar[0])
# print("Uchinchi telefon: ", telefonlar[3])
# print("Uchinchi telefon: ", telefonlar[-1]) # oxiridan sanash - bilan
# print("Uchinchi telefon: ", telefonlar[4])
#
# # sonlar ustida amallar
# narxlar = [12000, 15000, 20000, 50000]
# print(narxlar[2] + narxlar[3])




# sonlar = [12000, 15000, 20000, 50000]
# print(sonlar)
# sonlar[0] = sonlar[0] + 25000
#
# # tarkibni almashtirish
# sonlar[1] = 17000
# sonlar[-1] = 55000
# print(sonlar)
#
# # matnlar ustida amallar
# dostlar = ['alisher', 'kamron', 'odil', 'olim', 'anvar']
# print('asl royxat: ', dostlar)
# dostlar[0] = 'mansur'
# print('almashgan: ',dostlar)
#
# print('Kecha biz bilan fudbol korgan dostlarim: ', dostlar[0], dostlar[3])



# bozorlik = ['gosht', 'sabzi', 'yog', 'guruch']
# print(bozorlik)
#
# # append bilan yangi element qo'shish
# bozorlik.append('piyoz')
# bozorlik.append('ziravorlar')
# bozorlik.append('gugurt')
# print(bozorlik)
#
# # append orqali bosh ro'yxatni to'ldirish
# ismlar = []
# print(ismlar)
#
# ismlar.append('alisher')
# ismlar.append('olim')
# ismlar.append('jahongir')
# print(ismlar)
#
# narxlar = [33000, 20000, 10000, 5000]
# print(narxlar)
# narxlar.append(70000)
# narxlar.append(15000)
# narxlar.append(100000)
# narxlar.append(1000000)
# print(narxlar)
# print(narxlar[-2])



# moshinalar = ['malibu', 'gentra', 'spark', 'matiz']
# moshinalar.append('captiva')
# moshinalar.append('volga')
# print(moshinalar)
#
# # insert metodi bilan hohlagan joyga element qo'shamiz
# moshinalar.insert(0, 'nexia')
# moshinalar.insert(-1, 'nexia 3')
# moshinalar.insert(2, 'nexia 2')
# print(moshinalar)


# ro'yxat ichidan elementni o'chirishni ko'ramiz!
# ismlar = ['faxriddin', 'azizbek', 'aliyor', 'faxriddin', 'ulmasbek', 'muhammadyahyo', 'faxriddin']
# print(ismlar)
#
# # del ismlar[1]
# # del ismlar[3]
#
# ismlar.remove('faxriddin')
# ismlar.remove('muhammadyahyo')
# ismlar.remove('aliyor')
# ismlar.remove('ulmasbek')
# ismlar.remove('azizbek')
# print(ismlar)



# pop yordamida element boshqa ro'yxatga ko'chirib o'tish
# ismlar = ['azizbek', 'aliyor', 'ulmasbek', 'muhammadyahyo', 'faxriddin']
# vazifa = ismlar.pop(1)
# print("Vazifani qilgan dasturchilar: ", vazifa)
# print("Vazifani qilmagan dasturchilar: ", ismlar)



# ism = ['alisher', 'yaxyo', 'mansur']
# ism.insert(3, 'odil')
# print(ism)




#
# ism = ['alisher', 'yaxyo', 'mansur']
# del ism[1]
# ism.insert(1, 'yahyo')
# print(ism)







# moshinalar = ['bmw', 'audi', 'merc', 'tesla', 'gm', 'volga', 'ferrari']
# print(moshinalar)
#
#
# print(sorted(moshinalar, reverse=True))



# sonlar = [1, 4, 4554, 76, 2, 9, 33]
# print(sonlar)
#
# sonlar.sort(reverse=True)
# print(sonlar)


#
# telefon = ['iphone', 'redmi', 'samsung', 'realmi']
# print(telefon)
#
# telefon.reverse()
# print(telefon)




# sonlar = [1, 4, 4554, 76, 2, 9, 33]
# telefon = ['iphone', 'redmi', 'samsung', 'realmi', 'LG']
#
# print("Telefonlar soni: ", len(sonlar))



# sonlar = [1,2,3,4,5,6,7,8,9,10]
# print(sonlar)
#
#
#
# number1 = list(range(10))
# print(number1)



# sonlar = [100, 200, 400, 50, 30, 10]
# kich = min(sonlar)
# kat = max(sonlar)
# jami = sum(sonlar)
#
# print("Sonlarning kichkinasi: ", kich)
# print("Sonlarning Kattasi: ", kat)
# print("Sonlarning Jami miqdori: ", jami)



# telefon = ['iphone', 'redmi', 'samsung', 'realmi', 'lg']
# yangi_telefon = telefon[0:0]
# print(telefon)
# print(yangi_telefon)





# eski_telefon = ['iphone', 'redmi', 'samsung', 'realmi', 'lg']
# yangiTelefon = eski_telefon[:]
#
# yangiTelefon.append('oppo')
#
# print(eski_telefon)
# print(yangiTelefon)


# sonlar1 = [1, 2, 3, 4, 5]  # list ozgaruvchi ro'yxat
# sonlar2 = (1, 2, 3, 4, 5)  # tuple ozgarmas ro'yxat
#
# sonlar2 = list(sonlar2)
#
# print(type(sonlar1))
# print(type(sonlar2))
#
# sonlar1.append(6)
# sonlar2.append(999)
#
# sonlar2 = tuple(sonlar2)
# print(type(sonlar2))
#
# sonlar2 = list(sonlar2)
# sonlar2.append(777)
#
#
# print(sonlar1)
# print(sonlar2)


