cena_produktu = int(input("Podaj cena_produktu: "))
rabat = int(input("Podaj rabat (%): "))
kwota_rabatu = cena_produktu * (rabat/100)
cena_koncowa = cena_produktu - kwota_rabatu

print(f"Cena początkowa: {cena_produktu} zł")
print(f"Kwota rabatu: {kwota_rabatu} zł")
print(f"Cena koncowa: {cena_koncowa} zł")
if rabat > 20:
    print("Duża promocja!")
else:
    print("Standardowa promocja")