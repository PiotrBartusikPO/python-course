suma = 0
while True:
    print("\n========== KALKULATOR ==========")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnozenie")
    print("4. Dzielenie")
    print("5. Potegowanie")
    print("6. Srednia z podanych liczb")
    print("0. Zakoncz")
    print("================================")
    opcja = int(input("Wybierz opcję: "))
    if opcja == 1:
        liczba1 = int(input("Pierwsza liczba: "))
        liczba2 = int(input("Druga liczba: "))
        print(f"Wynik: {liczba1} + {liczba2} = {liczba1 + liczba2}")

    elif opcja == 2:
        liczba1 = int(input("Pierwsza liczba: "))
        liczba2 = int(input("Druga liczba: "))
        print(f"Wynik: {liczba1} - {liczba2} = {liczba1 - liczba2}")
    elif opcja == 3:
        liczba1 = int(input("Pierwsza liczba: "))
        liczba2 = int(input("Druga liczba: "))
        print(f"Wynik: {liczba1} * {liczba2} = {liczba1 * liczba2}")
    elif opcja == 4:
        liczba1 = int(input("Pierwsza liczba: "))
        liczba2 = int(input("Druga liczba: "))
        if liczba2 == 0:
            print("Nie można dzielić przez 0")
            liczba2 = int(input("Podaj inną liczbę: "))
        else:
            print(f"Wynik: {liczba1} : {liczba2} = {liczba1 / liczba2}")
    elif opcja == 5:
        liczba1 = int(input("Pierwsza liczba: "))
        liczba2 = int(input("Druga liczba: "))
        print(f"Wynik: {liczba1} ** {liczba2} = {liczba1 ** liczba2}")
    elif opcja == 6:
        ilosc_liczb = int(input("Ile liczb?: "))
        if ilosc_liczb < 0:
            print("Nieprawidłowa ilość elementów")
            continue
        else:
            for i in range(1,ilosc_liczb+1):
                liczba = int(input(f"Liczba {i} = "))
                suma += liczba
                srednia = suma/ilosc_liczb
            print(f"Średnia: {srednia}")
    elif opcja == 0:
        print("Do widzenia")
        break
    else:
        print("Nieprawidłowa opcja")
        continue



