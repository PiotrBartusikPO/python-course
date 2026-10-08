from turtledemo.round_dance import stop

temperatura = int(input("Podaj temperature: "))
ktoś_w_domu = str(input("Czy ktoś jest w domu: "))
okno_otwarte = str(input("Czy okno jest otwarte: "))
ogrzewanie = "WLACZONE"
if okno_otwarte == "nie" and ktoś_w_domu == "tak" and temperatura <20:
    ogrzewanie = "WLACZONE"
    print(f"Ogrzewanie: {ogrzewanie}")
    print("Powód: Temperatura poniżej 20")
    if okno_otwarte == "nie" and ktoś_w_domu == "nie" and temperatura <16:
        ogrzewanie = "WLACZONE"
        print(f"Ogrzewanie: {ogrzewanie}")
        print("Powód: Temperatura poniżej 16")
else:
    ogrzewanie = "WYLACZONE"
    print(f"Ogrzewanie: {ogrzewanie}")
if okno_otwarte == "tak":
    ogrzewanie = "WYLACZONE"
    print("Powód: Okno jest otwarte")
