magazyn = {"Mysz": 5, "Klawiatura": 3, "Monitor": 2}
while True:
    print("\n1 - Stan magazynu")
    print("2 - Przyjęcie towaru")
    print("3 - Wydanie towaru")
    print("0 - Zakończ")
    opcja = int(input("Wybierz opcje: "))
    if opcja == 0:
        print("Do widzenia")
        break
    if opcja == 1:
        for przedmiot, ilosc in magazyn.items():
            print(f"{przedmiot} - {ilosc} szt")
    elif opcja == 2:
        nazwa_produktu = input("Nazwa produktu: ")
        if nazwa_produktu in magazyn:
            ilosc = int(input("Ilość: "))
            magazyn[nazwa_produktu] += ilosc
        else:
            print("Nie ma takiego produktu na magazynie")
    elif opcja == 3:
        nazwa_produktu = input("Nazwa produktu: ")
        if nazwa_produktu in magazyn:
            ilosc = int(input("Ilość: "))
            if ilosc > magazyn[nazwa_produktu]:
                print("Nie ma wystarczającej ilości produktu na magazynie")
            else:
                magazyn[nazwa_produktu] -= ilosc
        else:
            print("Nie ma takiego produktu na magazynie")
