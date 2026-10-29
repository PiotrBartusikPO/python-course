def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b == 0:
        return "Nie można dzielić przez zero"
    return a / b

def potegowanie(a, b):
    return a**b

def srednia(liczb_lista):
    if not liczb_lista:
        return 0
    return sum(liczb_lista) / len(liczb_lista)

def wyswietl_menu():
    print("\n--- MENU ---")
    print("1 – dodawanie")
    print("2 – odejmowanie")
    print("3 – mnożenie")
    print("4 – dzielenie")
    print("5 – potęgowanie")
    print("6 – średnia")
    print("0 – zakończ")

def main():
    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcje: ")

        if wybor == "0":
            print("Koniec.")
            break
        elif wybor in ["1", "2", "3", "4", "5"]:
            a = float(input("Podaj pierwsza liczbe: "))
            b = float(input("Podaj druga liczbe: "))

            if wybor == "1":
                wynik = dodawanie(a, b)
            elif wybor == "2":
                wynik = odejmowanie(a, b)
            elif wybor == "3":
                wynik = mnozenie(a, b)
            elif wybor == "4":
                wynik = dzielenie(a, b)
            elif wybor == "5":
                wynik = potegowanie(a, b)

            print("Wynik:", wynik)

        elif wybor == "6":
            ile = int(input("Ile liczb chcesz podac? "))
            liczby = []
            for i in range(1, ile + 1):
                num = float(input(f"Liczba {i}: "))
                liczby.append(num)

            wynik = srednia(liczby)
            print("Srednia:", wynik)
        else:
            print("Niepoprawna opcja.")

if __name__ == "__main__":
    main()
    