import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("magazyny.csv", encoding="utf-8-sig")
print("Dostepne kolumny:", list(df.columns))

df = df[["magazyn", "miasto", "wojewodztwo", "produkty"]]

woj = input("Podaj wojewodztwo: ").strip().lower()
min_produkty = int(input("Minimalna liczba produktow: "))

wyniki = df[(df["wojewodztwo"].str.lower() == woj) & (df["produkty"] >= min_produkty)]

if wyniki.empty:
    print("\nBrak magazynow spelniajacych podane warunki.")
else:
    wyniki = wyniki.sort_values("produkty", ascending=False)
    print("\nMagazyny spelniajace warunki:")
    print(wyniki[["magazyn", "miasto", "produkty"]])

    print("\nLiczba magazynow:", len(wyniki))
    print("Suma produktow:", wyniki["produkty"].sum())

    top5 = wyniki.head(5)

    plt.figure(figsize=(8, 4))
    plt.barh(top5["magazyn"], top5["produkty"])
    plt.gca().invert_yaxis()
    plt.title(f"Najwieksze magazyny w woj. {woj} (min. {min_produkty} szt.)")
    plt.xlabel("Liczba produktow")
    plt.ylabel("Magazyn")
    plt.tight_layout()
    plt.show()
