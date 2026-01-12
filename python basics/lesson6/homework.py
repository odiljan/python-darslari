# python_lugat = {
#     'integer': 'butun son',
#     'float': 'onlik son',
#     'string': 'matn',
#     'if': 'agar shart',
#     'else': 'aks xolda',
#     'for': 'takrorlovchi sikl',
#     'while': 'shartli sikl',
#     'list': 'royxat',
#     'dict': 'lugat',
#     'input': 'foydalanuvchidan malumot olish'
# }

# print("Python izoxli lugati alifbo boyicha:")
# for kalit in sorted(python_lugat):
#     print(f"{kalit} - {python_lugat[kalit]}")


# davlatlar = {
#     'uzbekistan': 'toshkent',
#     'russia': 'moskva',
#     'usa': 'washington',
#     'japan': 'tokyo',
#     'germany': 'berlin',
#     'turkey': 'ankara',
#     'france': 'paris',
#     'china': 'beijing',
#     'india': 'delhi',
#     'italy': 'rome'
# }

# print("\nDavlatlar alifbo tartibida:")
# for davlat in sorted(davlatlar):
#     print(davlat.title())

# print("\nPoytaxtlar alifbo tartibida:")
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())


# davlat = input("\nXoxlagan davlat nomini yozing: ").lower()
# if davlat in davlatlar:
#     print(f"{davlat.title()} ni poytaxti {davlatlar[davlat].title()}")
# else:
#     print("Bizda bunaqa malumot yoq")


menyu = {
    'osh': 30000,
    'kabob': 25000,
    'norin': 35000,
    'mastava': 20000,
    'shashlik': 27000,
    'somsa': 10000,
    'lagmon': 22000,
    'manti': 24000,
    'tuxum': 8000,
    'qaymoq': 12000
}

print("\n3ta ovqat buyurtma qiling:")
buyurtmalar = []
for i in range(3):
    taom = input(f"{i+1}-taom: ").lower()
    buyurtmalar.append(taom)

for taom in buyurtmalar:
    if taom in menyu:
        print(f"{taom.title()} narxi {menyu[taom]} som")
    else:
        print(f"Bizda {taom.title()} yoq")


# son = 0
# while son < 10:
#     if son % 2 != 0:
#         son += 1
#         continue
#     print(son)
#     son += 1


# while True:
#     yosh = input("\nYoshingzni kriting: ")
#     if yosh.lower() in ['exit', 'quit']:
#         break
#     yosh = int(yosh)
#     if yosh < 7:
#         print("2000 som")
#     elif yosh < 18:
#         print("4000 som")
#     elif yosh < 65:
#         print("6000 som")
#     else:
#         print("Bepul")


# while True:
#     yosh = input("\nYoshni yozing: ")
#     if yosh.lower() == 'exit':
#         break
#     yosh = int(yosh)
#     if yosh < 7:
#         print("2000 som")
#     elif yosh < 18:
#         print("4000 som")
#     elif yosh < 65:
#         print("6000 som")
#     else:
#         print("Bepul")


# son = 1
# while son < 10:
#     son += 1
#     if son % 2 != 0:
#         continue
#     print(son)


# savol = "Kiritilgan sonni ildizini chiqaradi.\n"
# savol += "Musbat son yozing "
# savol += "(toxtatish uchun exit deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat.lower() == 'exit':
#         break
#     qiymat = float(qiymat)
#     if qiymat < 0:
#         continue
#     ildiz = qiymat ** 0.5
#     print(f"{qiymat} ni ildizi {ildiz} ga teng")
