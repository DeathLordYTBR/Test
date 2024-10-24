import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parola_uzunlugu = int(input("Lütfen parolanızın uzunluğunu girin: "))

parola = ""

for _ in range(parola_uzunlugu):
    rastgele_karakter = random.choice(karakterler)
    parola += rastgele_karakter

print("Oluşturulan parola:", parola)





