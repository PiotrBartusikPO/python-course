liczba_studentow = int(input("Podaj liczbe studentow: "))
punkty = []
for i in range(1,liczba_studentow+1):
    punkty_studentow = int(input(f"Podaj punkty studenta {i}: "))
    punkty.append(punkty_studentow)
srednia = sum(punkty) / len(punkty)
print(f"Średnia: {srednia}")
max = max(punkty)
min = min(punkty)
print(f"Najwyższy wynik: {max}")
print(f"Najniższy wynik: {min}")
sortowanie = sorted(punkty)
print(f"Wyniki rosnąco: {sortowanie}")
zaliczone = 0
for i in punkty:
    if i >= 50:
        zaliczone += 1
print(f"Liczba zaliczeń: {zaliczone}")

