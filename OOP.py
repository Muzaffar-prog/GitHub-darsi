

""" OOP bilan ishlash darslari """


# a = 777
# print(type(a))
#
# b = "hello"
# print(type(b))
#
# # funk
# def my_funk():
#     """ salom qaytaradi """
#     print("Assalomu Alaykum")
#
# print(type(my_funk))


# class Developer:
#     def __init__(self, ism, fam, soha, yoshi):
#         self.ismi = ism
#         self.familyasi = fam
#         self.sohasi = soha
#         self.yoshi = yoshi
#
#     def new_dev(self):
#         pass
#
#     def full(self):
#         pass
#
# dev1 = Developer("Alisher", "Rashidov", "Backend", 24)
# print("Birinchi dasturchining ismi: ",dev1.ismi, dev1.familyasi)

print("\n")


# class Dasturchilar: # super class
#     """ Barcha dasturchilar haqidagi ma'lumotni yig'uvchi class """
#     def __init__(self, ismi, fam, soha, yoshi):
#         self.ismi = ismi
#         self.familyasi = fam
#         self.sohasi = soha
#         self.yoshi = yoshi
#
#     def get_info(self):
#         dasturchi = f"Dasturchining ismi: {self.ismi}, familyasi: " \
#                     f"{self.familyasi}, sohasi: {self.sohasi}, yoshi: {self.yoshi} da "
#         return dasturchi
#
# developer1 = Dasturchilar("Mansur", "Saidov", "Python-backend", 22)
# developer2 = Dasturchilar("Odilbek", "Mirzayev", "Frontend", 26)
# developer3 = Dasturchilar("Feruzbek", "Odilov", "Mobile dasturlash", 20)
#
# # get metodi bilan chiqarish usuli:
# print(developer1.get_info())
# print(developer3.get_info())
# print(developer3.get_info())
#
# # get metodisiz chiqarish usuli:
# # print(f"Dasturchining ismi: {developer2.ismi}, Familyasi: {developer2.familyasi}, Sohasi: {developer2.sohasi}, Yoshi: {developer2.yoshi} ")
# # print(f"Dasturchining ismi: {developer3.ismi}, Familyasi: {developer3.familyasi}, Sohasi: {developer3.sohasi}, Yoshi: {developer3.yoshi} ")
#
#
# # voris olish usuli!!!
# class Yangi_dasturchi(Dasturchilar): # voris class
#     def __int__(self, ismi, fam, soha, yoshi, manzil):
#         super().__init__(ismi, fam, soha, yoshi)
#         self.manzili = manzil
#
#     # polimorfizim sifatida yangi element qo'shish
#     def get_info(self):
#         dasturchi = f"Dasturchining ismi: {self.ismi}, familyasi: " \
#                     f"{self.familyasi}, sohasi: {self.sohasi}, yoshi: {self.yoshi} da, Yashash manzili: {self.manzili} "
#         return dasturchi
#
# das1 = Yangi_dasturchi("Fahriddin", "Norimov", "IOS developer", 18)
# print(das1.get_info())



# class Cars: # super class
#     def __int__(self, model, nomi, rangi, narh=0):
#         self.model = model
#         self.nomi = nomi
#         self.rangi = rangi
#         self.__narh = narh # moshinaning narhi yashirin bo'lib qoldi bu ikapsulatsiya
#
#     def __repr__(self):
#         return f"Moshina: {self.nomi}, {self.model} "




















