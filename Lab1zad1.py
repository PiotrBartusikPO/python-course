cena = int(input("Podaj cene produktu: "))
ilosc = int(input("Podaj ilosc produktu: "))
koszt_dostawy = 12
wartosc = cena * ilosc

if wartosc >= 100:
    koszt_dostawy = 0
else:
    koszt_dostawy = 12

laczna_wartosc = wartosc + koszt_dostawy
print(f"Wartosc produktów: {wartosc}")
print(f"Koszt dostawy: {koszt_dostawy}")
print(f"Do zapłaty: {laczna_wartosc}")
