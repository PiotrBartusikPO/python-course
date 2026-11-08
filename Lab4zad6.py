import matplotlib.pyplot as plt
liczba_studentow = int(input("Podaj liczbe studentow: "))
nazwiska = []
punkty = []
oceny = []

for i in range(1, liczba_studentow + 1):
    nazwisko = input(f"Nazwisko studenta {i}: ")
    pts = float(input("Punkty: "))
    if pts < 50:
        ocena = 2.0
    elif pts < 60:
        ocena = 3.0
    elif pts < 70:
        ocena = 3.5
    elif pts < 80:
        ocena = 4.0
    elif pts < 90:
        ocena = 4.5
    else:
        ocena = 5.0
    nazwiska.append(nazwisko)
    punkty.append(pts)
    oceny.append(ocena)
print()
for nazwisko, ocena in zip(nazwiska, oceny):
    print(f"{nazwisko} - {ocena}")
srednia = sum(oceny) / len(oceny)
zaliczenia = sum(1 for ocena in oceny if ocena >= 3.0)

print(f"Srednia ocen: {srednia}")
print(f"Liczba zaliczen: {zaliczenia}")
print("Generowanie wykresu...")

plt.figure(figsize=(8, 5))
plt.bar(nazwiska, oceny, color="blue")
plt.xlabel("Nazwisko studenta")
plt.ylabel("Ocena")
plt.title("Analiza ocen studentów")
plt.ylim(0, 5.5)
plt.show()