import pandas as pd
df = pd.DataFrame({"Produkt": ["Mysz", "Klawiatura","Monitor","Podkładka"], "Cena": [50, 120, 650, 30],"Ilosc": [10, 5, 3, 20]})
df["Wartosc"] = df["Cena"] * df["Ilosc"]
print(df)
print(f"\nProdukty droższe niż 100zł: \n{df[df["Cena"] > 100]}")
print(f"Wartość magazynu: {df["Wartosc"].sum()} zł")
print(f"Średnia cena: {df["Cena"].mean()} zł")


