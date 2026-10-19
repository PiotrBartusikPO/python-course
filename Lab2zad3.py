napoje = ["Woda", "Sok", "Cola"]
ceny = [3,5,6]
i = 0
while i < len(napoje):
    print(f"{i+1}. {napoje[i]} - {ceny[i]} zł")
    i+=1
print("0. Zakończ")
suma = 0
while True:
    opcja = int(input("Wybierz opcje: "))
    if opcja == 0:
        print(f"Lącznie do zapłaty: {suma}")
        break
    elif opcja >3:
        print("Nieprawidłowa opcja")
        continue
    print(f"Wybrano: {napoje[opcja-1]}, cena: {ceny[opcja-1]}")
    suma += ceny[opcja-1]



