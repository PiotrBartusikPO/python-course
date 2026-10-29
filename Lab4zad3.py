ilosc_pomiarow = int(input("Podaj liczbe pomiarów: "))
pomiary = []
for i in range(1, ilosc_pomiarow + 1):
    pomiar = int(input(f"Podaj pomiar {i}: "))
    pomiary.append(pomiar)
prog_alarmowy = 50
pomiary_alarmowe = [x for x in pomiary if x > prog_alarmowy]
pomiary_pomnozone = [x * 2 for x in pomiary]
czy_alarm = any(x > prog_alarmowy for x in pomiary)
czy_prawidlowe = all(x <= prog_alarmowy for x in pomiary)
print(f"Pomiary alarmowe: {pomiary_alarmowe}")
print(f"Pomiary pomnozone przez 2: {pomiary_pomnozone}")
print(f"Czy wystapil alarm? {'Tak' if czy_alarm else 'Nie'}")
print(f"Czy wszystkie pomiary sa prawidlowe? {'Tak' if czy_prawidlowe else 'Nie'}")