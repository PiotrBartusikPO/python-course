liczba_punktow = int(input("Podaj liczbe punktów: "))
ocena = 0
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

print(f"Liczba punktów: {liczba_punktow}")
print(f"Liczba ocena: {ocena}")
