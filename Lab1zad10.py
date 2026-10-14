liczba_studentow = int(input("Podaj liczbe studentów: "))
zaliczone = 0

for i in range(1, liczba_studentow + 1):
    nazwisko = input(f"Nazwisko studenta {i}: ")
    liczba_punktow = int(input("Punkty: "))
    if liczba_punktow < 0 or liczba_punktow > 100:
        print("Nieprawidlowa liczba punktów")
        continue
    if liczba_punktow <= 49:
        ocena = 2.0
    elif liczba_punktow >= 50 and liczba_punktow <= 59:
        ocena = 3.0
    elif liczba_punktow >= 60 and liczba_punktow <= 69:
        ocena = 3.5
    elif liczba_punktow >= 70 and liczba_punktow <= 79:
        ocena = 4.0
    elif liczba_punktow >= 80 and liczba_punktow <= 89:
        ocena = 4.5
    elif liczba_punktow >= 90 and liczba_punktow <= 100:
        ocena = 5.0

    print(f"{nazwisko} - {liczba_punktow} pkt - ocena {ocena}")

    if ocena >= 3.0:
        zaliczone += 1
print(f"Liczba studentów, którzy zaliczyli: {zaliczone}")
