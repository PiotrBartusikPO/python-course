zadania = []
dziala = True
while dziala == True:
    print("\n1 - Dodaj zadanie,")
    print("2 - Wyświetl zadanie,")
    print("3 - Usuń zadanie,")
    print("4 - Wyświetl liczbe zadań,")
    print("0 - Zakończ.")
    opcja = int(input("Wybierz opcję: "))
    if opcja == 1:
        zadanie = input("Podaj nazwę zadania: ")
        zadania.append(zadanie)
    elif opcja == 2:
        for i in range(len(zadania)):
            print(f"{i+1} - {zadania[i]}")
    elif opcja == 3:
        usun = int(input("Podaj numer zadania: "))
        zadania.pop(usun-1)
        print("Zadanie usunięte")
    elif opcja == 4:
        if len(zadania) == 0:
            print("Brak zadań")
        else:
            print(f"Liczba zadań wynosi: {len(zadania)}")
    elif opcja == 0:
        print("Do widzenia")
        dziala = False
    else:
        print("Nieprawidłowa opcja")
        continue
