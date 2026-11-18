import numpy as np
liczba_produktow = int(input("Podaj liczba produktow: "))
ceny = []
for i in range(1,liczba_produktow+1):
    cena = int(input(f"Podaj cene {i}: "))
    ceny.append(cena)
cenynp = np.array(ceny)
rabat = int(input("Podaj rabat (%): "))
print(f"Ceny początkowe: {cenynp}")
nowe_ceny = cenynp * (1 - rabat / 100)
print(f"Ceny po rabacie: {nowe_ceny}")
print(f"Suma przed rabatem: {sum(cenynp)} zł")
print(f"Suma po rabacie: {sum(nowe_ceny)} zł")
print(f"Ceny powyżej 100 zł: {nowe_ceny[nowe_ceny > 100]}")
