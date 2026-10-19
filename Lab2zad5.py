proba = 0
haslo = "Python123"
while True:
    wpisz_haslo = input("Podaj hasło: ")
    if wpisz_haslo == haslo:
        print("Logowanie udane!")
        break
    else:
        proba += 1
        print(f"Hasło niepoprawne. Pozostałe próby: {3-proba}")
        if proba == 3:
            print("Konto zablokowane")
            break




