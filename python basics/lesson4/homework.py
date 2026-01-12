# davlatlar = ["O'zbekiston", "Turkiya", "AQSH", "Malayziya", "Yaponiya", "Germaniya"]
# print("Davlatlar royxati:", davlatlar)

# print("Ro‘yxat uzunligi:", len(davlatlar))

# print("Tartiblangan royxat:", sorted(davlatlar))

# print("Teskari tartib:", sorted(davlatlar, reverse=True))

# print("Asl royxat:", davlatlar)

# davlatlar.reverse()
# print("Reverse qilingan ro‘yxat:", davlatlar)

# davlatlar.sort()
# print("Alifbo boyicha:", davlatlar)

# davlatlar.sort(reverse=True)
# print("Alifboga teskari:", davlatlar)

# juft_sonlar = list(range(120, 1201, 2))

# print("Yigindi:", sum(juft_sonlar))

# ayirma = max(juft_sonlar) - min(juft_sonlar)
# print("Eng katta va eng kichik son ayirmasi:", ayirma)

# print("Elementlar soni:", len(juft_sonlar))
 
# sonlar = list(range(1, 101))
# print("Boshidan 20 ta:", sonlar[:20])
# print("O'rtasidan 20 ta:", sonlar[40:60])
# print("Oxiridan 20 ta:", sonlar[-20:])

# taomlar = ["osh", "shashlik", "mastava", "norin", "somsa"]
# print("\nTaomlar ro'yxati:", taomlar)

# nonushta = taomlar[:]

# nonushta.remove("shashlik")
# nonushta.remove("norin")
# nonushta.append("tuxum")
# nonushta.append("qaymoq")

# print("\nAsl taomlar ro'yxati:", taomlar)
# print("Nonushta ro'yxati:", nonushta)

# nonushta = tuple(nonushta)
# print("\nO'zgarmas nonushta ro'yxati:", nonushta)

# try:
#     nonushta[0] = "qaymoq va non"
# except TypeError:
#     print("Xatolik: Tuple elementini uzgartirib bulmaydi")


# ismlar = ["Ali", "Vali", "Hasan", "Husan", "G'ani"]
# for ism in ismlar:
#     print(f"{ism}, siz eng yaqin dostimsiz")

# print(f"\nKod {len(ismlar)} marta takrorlandi")

# toq_sonlar = list(range(11, 100, 2))
# for son in toq_sonlar:
#     print(f"{son} ning kubi: {son**3}")

# kinolar = []
# print("\n5 ta yoqtirgan kinoyingizni kiriting:")
# for i in range(5):
#     kino = input(f"{i+1}-kino: ")
#     kinolar.append(kino)

# print("\nSiz yoqtirgan kinolar:")
# for kino in kinolar:
#     print(kino)

odamlar = []
n = int(input("\nBugun nechta odam bilan suhbatlashdingiz? "))
for i in range(n):
    ism = input(f"{i+1}-suhbatdoshingizning ismi: ")
    odamlar.append(ism)

print("\nBugun suhbatlashgan odamlar:")
for ism in odamlar:
    print(ism)
