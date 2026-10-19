temperatury = []
for i in range(1,7+1):
    temp_dnia = int(input(f"Podaj temperature dla dnia {i}: "))
    temperatury.append(temp_dnia)
    print(f"Dzień {i}: {temp_dnia}")
srednia = sum(temperatury) / len(temperatury)
maks = max(temperatury)
minimal = min(temperatury)
powyzej_sredniej = []
for temp_dnia in temperatury:
    if temp_dnia > srednia:
        powyzej_sredniej.append(temp_dnia)
print(f"Średnia: {srednia} C")
print(f"Najwyższa: {maks} C ")
print(f"Najniższa: {minimal} C ")
print(f"Powyżej średniej: {powyzej_sredniej}")
print(f"Liczba dni: {len(powyzej_sredniej)}")

