warsztat_python = set()
warsztat_ai = set()

while True:
    print("\n1. Zapisz na Python")
    print("2. Zapisz na AI")
    print("3. Wyswietl uczestnikow")
    print("4. Uczestnicy obu warsztatow")
    print("5. Wszyscy unikalni uczestnicy")
    print("0. Zakoncz")

    opcja = input("\nWybierz opcje: ")
    if opcja == "1":
        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        uczestnik = (imie, nazwisko)
        if uczestnik in warsztat_python:
            print("Uczestnik jest juz zapisany na te warsztaty")
        else:
            warsztat_python.add(uczestnik)
            print("Dodano uczestnika.")
    elif opcja == "2":
        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        uczestnik = (imie, nazwisko)
        if uczestnik in warsztat_ai:
            print("Uczestnik jest juz zapisany na te warsztaty")
        else:
            warsztat_ai.add(uczestnik)
            print("Dodano uczestnika.")
    elif opcja == "3":
        print("\n--- Warsztat Python ---")
        for imie, nazwisko in warsztat_python:
            print(f"{imie} {nazwisko}")

        print("\n--- Warsztat AI ---")
        for imie, nazwisko in warsztat_ai:
            print(f"{imie} {nazwisko}")
    elif opcja == "4":
        wspolni = warsztat_python & warsztat_ai
        print("\nUczestnicy obu warsztatow:")
        for imie, nazwisko in wspolni:
            print(f"{imie} {nazwisko}")
    elif opcja == "5":
        wszyscy = warsztat_python | warsztat_ai
        print("\nWszyscy unikalni uczestnicy:")
        for imie, nazwisko in wszyscy:
            print(f"{imie} {nazwisko}")
    elif opcja == "0":
        print("Koniec programu.")
        break
    else:
        print("Sprobuj ponownie.")
