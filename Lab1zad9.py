poczatek = int(input("Podaj początek zakresu: "))
koniec = int(input("Podaj koniec zakresu: "))
ilosc_parzystych = 0
for i in range(poczatek,koniec+1):
    if i % 2 == 0:
        print(f"{i} - Parzysta")
        ilosc_parzystych += 1
    else:
        print(f"{i} - Nieparzysta")
print(f"Liczba liczb parzystych: {ilosc_parzystych}")

