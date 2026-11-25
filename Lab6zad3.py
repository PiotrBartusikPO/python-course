import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

magazyny = pd.read_csv("magazyny.csv", encoding="utf-8-sig")
klienci = pd.read_csv("klienci.csv", encoding="utf-8-sig")

magazyny = magazyny[["wojewodztwo", "produkty"]]
klienci = klienci[["wojewodztwo", "zamowienia"]]

prod_woj = magazyny.groupby("wojewodztwo")["produkty"].sum().reset_index()
zam_woj = klienci.groupby("wojewodztwo")["zamowienia"].sum().reset_index()

wynik = pd.merge(prod_woj, zam_woj, on="wojewodztwo")
wynik["roznica"] = wynik["produkty"] - wynik["zamowienia"]
wynik = wynik.sort_values("roznica")
print(wynik)

x = np.arange(len(wynik["wojewodztwo"]))
szerokosc = 0.35

plt.figure(figsize=(11, 5))
plt.bar(x - szerokosc / 2, wynik["produkty"], width=szerokosc, label="Produkty w magazynach")
plt.bar(x + szerokosc / 2, wynik["zamowienia"], width=szerokosc, label="Zamowienia klientow")
plt.title("Porownanie liczby produktow i zamowien w wojewodztwach")
plt.xlabel("Wojewodztwo")
plt.ylabel("Liczba sztuk")
plt.xticks(x, wynik["wojewodztwo"], rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.barh(wynik["wojewodztwo"], wynik["roznica"])
plt.gca().invert_yaxis()
plt.title("Roznica (produkty - zamowienia) w wojewodztwach")
plt.xlabel("Roznica [szt.]")
plt.ylabel("Wojewodztwo")
plt.tight_layout()
plt.show()