import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("klienci.csv", encoding="utf-8-sig")
print("Nazwy kolumn:", list(df.columns))
print("Liczba klientow:", len(df))

df = df[["klient", "miasto", "wojewodztwo", "zamowienia"]].copy()
df = df.sort_values("zamowienia", ascending=False)

print("\nTOP 5 klientow (bez udzialu):")
print(df[["klient", "miasto", "zamowienia"]].head(5))

suma_zamowien = df["zamowienia"].sum()
df["udzial_procent"] = (df["zamowienia"] / suma_zamowien * 100).round(2)

print("\nTOP 5 klientow:")
print(df[["klient", "miasto", "zamowienia", "udzial_procent"]].head(5))
print("\nSuma zamowionych sztuk:", suma_zamowien)

top10 = df.head(10)

plt.figure(figsize=(9, 5))
plt.bar(top10["klient"], top10["zamowienia"])
plt.title("TOP 10 klientow z najwieksza liczba zamowien")
plt.xlabel("Klient")
plt.ylabel("Liczba zamowionych sztuk")
plt.tight_layout()
plt.show()

suma_top10 = top10["zamowienia"].sum()
suma_pozostali = suma_zamowien - suma_top10

wartosci = [suma_top10, suma_pozostali]
etykiety = ["TOP 10 klientow", "Pozostali klienci"]

plt.figure(figsize=(6, 6))
plt.pie(wartosci, labels=etykiety, autopct="%1.1f%%")
plt.title("Udzial TOP 10 klientow w calkowitej liczbie zamowien")
plt.tight_layout()
plt.show()