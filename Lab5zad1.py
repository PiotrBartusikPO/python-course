import numpy as np
liczba_pomiarow = int(input("Podaj liczbe pomiarów: "))
pomiary = []
for i in range(1, liczba_pomiarow + 1):
    pomiar = int(input(f"Podaj pomiar {i}: "))
    pomiary.append(pomiar)
pomiarynp = np.array(pomiary)
print(f"Pomiary: {pomiarynp}")
print(f"Średnia: {np.mean(pomiarynp)} C")
print(f"Minimum: {np.min(pomiarynp)} C")
print(f"Makisum: {np.max(pomiarynp)} C")
print(f"Rozstęp: {np.max(pomiarynp)-np.min(pomiarynp)} C")
