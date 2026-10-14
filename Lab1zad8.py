wysokosc_choinki = int(input("Podaj wysokość choinki: "))
for i in range(1,wysokosc_choinki+1):
    spacja = " " * (wysokosc_choinki - i)
    gwiazda = "*" * (2 * i -1)
    print(spacja + gwiazda)
    