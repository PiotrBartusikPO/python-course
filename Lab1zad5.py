czas_parkowania = int(input("Podaj czas parkowania (h): "))
opłata = 0
if czas_parkowania <=1:
    opłata = 5
if czas_parkowania >1 and czas_parkowania <=3:
    opłata = 12
if czas_parkowania >3 and czas_parkowania <=6:
    opłata = 20
if czas_parkowania >6:
    opłata = 30
if czas_parkowania <= 0:
    print("Nieprawidłowe dane")
else:
    print(f"Czas parkowania {czas_parkowania} godz")
    print(f"Opłata za parking {opłata} zł")

