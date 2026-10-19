zakupy = []
liczba_produktow = int(input("Ile produktów chcesz dodać? "))
for i in range(1, liczba_produktow+1):
    produkt = input("Podaj nazwe produktu: ")
    zakupy.append(produkt)
    print(f"Produkt {i}: {produkt}")

print(f"Lista: {zakupy}")
print(f"Liczba produktów: {len(zakupy)}")
usun = input("Produkt do usunięcia: ")
if usun in zakupy:
    zakupy.remove(usun)
    print(f"Nowa lista: {zakupy}")
else:
    print("Brak takiego produktu")

