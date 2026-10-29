ilosc_pomiarow = int(input("Ile pomiarów chcesz wprowadzić? "))
pomiary = []
for i in range(1, ilosc_pomiarow + 1):
    pomiar = int(input(f"Podaj wartość pomiaru {i}: "))
    print(f"Pomiar {i}: {pomiar}")
    pomiary.append(pomiar)
    i +=1
print(f"Pierwszy pomiar: {pomiary[0]}")
print(f"Ostatni pomiar: {pomiary[-1]}")
print(f"Pierwsze trzy: {pomiary[:3]}")
print(f"Ostatni trzy: {pomiary[-3:]}")
print(f"Co drugi: {pomiary[::2]}")
print(f"Odwrócona lista: {pomiary[::-1]}")
print(f"Oryginał: {pomiary}")
kopia = pomiary.copy()
kopia[0] = 0
print(f"Kopia po zmianie: {kopia}")
