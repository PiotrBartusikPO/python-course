kontakty = {}

while True:
    print("========== KSIAZKA KONTAKTOW ==========")
    print("1. - Dodaj kontakt ")
    print("2. - Wyświetl wszystkie kontakty ")
    print("3. - Wyszukaj kontakt ")
    print("4. - Edytuj kontakt ")
    print("5. - Usuń kontakt ")
    print("0. - Zakończ")
    print("=======================================")

    opcja = int(input("Wybierz opcję: "))

    if opcja == 1:
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        telefon = input("Podaj telefon: ")
        if telefon in kontakty:
            print("Kontakt o podanym numerze już istnieje!")
        else:
            kontakty[telefon] = [imie, nazwisko]
            print("Kontakt dodany.")
    elif opcja == 2:
        if not kontakty:
            print("Książka kontaktów jest pusta.")
        else:
            for telefon, dane in kontakty.items():
                print(f"Telefon: {telefon}, Imię: {dane[0]}, Nazwisko: {dane[1]}")
    elif opcja == 3:
        telefon = input("Podaj numer telefonu do wyszukania: ")
        if telefon in kontakty:
            dane = kontakty[telefon]
            print(f"Znaleziono kontakt: {dane[0]} {dane[1]}")
        else:
            print("Nie znaleziono kontaktu o tym numerze.")
    elif opcja == 4:
        telefon = input("Podaj numer telefonu kontaktu do edycji: ")
        if telefon in kontakty:
            nowe_imie = input("Podaj nowe imię: ")
            nowe_nazwisko = input("Podaj nowe nazwisko: ")
            kontakty[telefon] = [nowe_imie, nowe_nazwisko]
            print("Kontakt został zaktualizowany.")
        else:
            print("Nie znaleziono kontaktu o tym numerze.")
    elif opcja == 5:
        telefon = input("Podaj numer telefonu kontaktu do usunięcia: ")
        if telefon in kontakty:
            del kontakty[telefon]
            print("Kontakt usunięty.")
        else:
            print("Nie znaleziono kontaktu o tym numerze.")

    elif opcja == 0:
        print("Koniec programu.")
        break

    else:
        print("Nieprawidłowa opcja, spróbuj ponownie.")