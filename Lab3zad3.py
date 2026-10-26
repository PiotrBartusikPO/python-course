ksiazki = []

while True:
    print("========== BIBLIOTEKA ==========")
    print("1. Dodaj ksiazke")
    print("2. Wyświetl wszystkie książki")
    print("3. Wypożycz książkę")
    print("4. Zwróc książke")
    print("5. Usuń książke")
    print("0. Zakończ")
    print("================================")

    opcja = int(input("Wybierz opcję: "))

    if opcja == 1:
        tytuł = input("Podaj tytuł: ")
        autor = input("Podaj autora: ")
        ksiazka = {"tytul": tytuł, "autor": autor, "dostepna": True}
        ksiazki.append(ksiazka)
        print("Ksiazka dodana.")

    elif opcja == 2:
        if not ksiazki:
            print("Katalog książek jest pusty.")
        else:
            print("\nLista książek:")
            for idx, ksiazka in enumerate(ksiazki, start=1):
                status = "Dostępna" if ksiazka["dostepna"] else "Wypożyczona"
                print(f"{idx}. {ksiazka['tytul']} - {ksiazka['autor']} [{status}]")

    elif opcja == 3:
        if not ksiazki:
            print("Katalog książek jest pusty.")
        else:
            numer = int(input("Numer ksiazki: "))
            if 1 <= numer <= len(ksiazki):
                ksiazka = ksiazki[numer - 1]
                if ksiazka["dostepna"]:
                    ksiazka["dostepna"] = False
                    print(f"Wypozyczono: {ksiazka['tytul']}")
                else:
                    print("Ta książka jest już wypożyczona!")
            else:
                print("Nieprawidłowy numer książki!")

    elif opcja == 4:
        if not ksiazki:
            print("Katalog książek jest pusty.")
        else:
            numer = int(input("Numer ksiazki: "))
            if 1 <= numer <= len(ksiazki):
                ksiazka = ksiazki[numer - 1]
                if not ksiazka["dostepna"]:
                    ksiazka["dostepna"] = True
                    print(f"Zwrócono: {ksiazka['tytul']}")
                else:
                    print("Ta książka nie była wypożyczona!")
            else:
                print("Nieprawidłowy numer książki!")

    elif opcja == 5:
        if not ksiazki:
            print("Katalog książek jest pusty.")
        else:
            numer = int(input("Numer ksiazki: "))
            if 1 <= numer <= len(ksiazki):
                usunieta = ksiazki.pop(numer - 1)
                print(f"Usunięto książkę: {usunieta['tytul']}")
            else:
                print("Nieprawidłowy numer książki!")

    elif opcja == 0:
        print("Koniec programu.")
        break

    else:
        print("Nieprawidłowa opcja, spróbuj ponownie.")