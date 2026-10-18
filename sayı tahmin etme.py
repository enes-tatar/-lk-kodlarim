import random

sayi = random.randint(1, 100)

print("1 ile 100 arasında bir sayı tuttum!")

while True:
    tahmin = int(input("Tahmin et: "))

    if tahmin < sayi:
        print("Daha büyük söyle!")
    elif tahmin > sayi:
        print("Daha küçük söyle!")
    else:
        print("🎉 Tebrikler! Bildin!")
        break