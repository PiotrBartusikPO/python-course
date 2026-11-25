import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("magazyny.csv", encoding="utf-8-sig")
print("Kolumny:", df.columns.tolist())
print(df.head())

df = df[["magazyn", "miasto", "wojewodztwo", "produkty"]]

print(f"\nLiczba magazynow: {len(df[["magazyn"]])}")

df_posortowane = df.sort_values(by="produkty", ascending=False)

print("TOP 5 magazynow:")
print(df_posortowane[["magazyn", "miasto", "produkty"]].head())

suma_produktow = df_posortowane["produkty"].sum()
print(f"\nLaczna liczba produktow: {suma_produktow}")

top10 = df_posortowane.head(10).iloc[::-1]
plt.figure(figsize=(10, 6))
plt.barh(top10["magazyn"], top10["produkty"], color="blue")
plt.xlabel("Liczba produktów")
plt.ylabel("Identyfikator magazynu")
plt.title("TOP 10 magazynów z największą liczbą produktów")
plt.tight_layout()
plt.show()
