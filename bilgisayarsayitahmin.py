import random

print("--- AKILLI TELEFON ZİHİN OKUMA OYUNU ---")
print("1 ile 100 arasında bir sayı tut ve aklından çıkarma!")
print("Telefonun tahminlerine 'büyük', 'küçük' veya 'bildin' diye cevap ver.\n")

alt_sinir = 1
ust_sinir = 100
adim = 0

while True:
    tahmin = (alt_sinir + ust_sinir) // 2
    adim += 1
    
    print(f"\nTahminim: {tahmin}")
    cevap = input("Aklındaki sayı bundan (büyük / küçük / bildin): ").lower()
    
    if cevap == "bildin":
        print(f"\nHarika! Sayını {adim} adımda buldum! 😎")
        break
    elif cevap == "büyük":
        alt_sinir = tahmin + 1
    elif cevap == "küçük":
        ust_sinir = tahmin - 1
    else:
        print("Lütfen sadece 'büyük', 'küçük' veya 'bildin' yaz.")
        
    if alt_sinir > ust_sinir:
        print("\nHmm, galiba cevaplarda bir çelişki oldu, yeniden başlayalım! 😄")
        break