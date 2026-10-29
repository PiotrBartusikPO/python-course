ilosc_produktow = int(input("Podaj ilość produktów: "))
produkty = []
ceny = []
for i in range(1,ilosc_produktow+1):
    produkt = input("Podaj produkt: ")
    produkty.append(produkt)
    cena = int(input("Podaj cena: "))
    ceny.append(cena)
    i+=1

print("\n=== CENNIK ===")
for numer, (produkt, cena) in enumerate(zip(produkty, ceny), start=1):
    print(f"{numer} - {produkt} - {float(cena)}")
suma_cen = sum(ceny)
print(f"Suma ceny: {suma_cen} zł")

max_cena = max(ceny)
max_index = ceny.index(max_cena)
najdroższy_prosukt = produkty[max_index]
print(f"Najdroższy produkt: {najdroższy_prosukt} - {float(max_cena)} zł")
