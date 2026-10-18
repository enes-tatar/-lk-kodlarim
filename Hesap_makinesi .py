sayi1 = int(input("1. sayiyi gir: "))
sayi2 = int(input("2. sayiyi gir: "))

islem = input("İşlem seç (+, -, *, /): ")

if islem == "+":
    print("Sonuç:", sayi1 + sayi2)
elif islem == "-":
    print("Sonuç:", sayi1 - sayi2)
elif islem == "*":
    print("Sonuç:", sayi1 * sayi2)
elif islem == "/":
    print("Sonuç:", sayi1 / sayi2)
else:
    print("Geçersiz işlem!")

