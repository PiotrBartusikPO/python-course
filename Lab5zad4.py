import matplotlib.pyplot as plt
import pandas as pd
def oblicz_ocene(pts):
  if pts < 50:
    return 2.0
  elif pts < 60:
    return 3.0
  elif pts < 70:
    return 3.5
  elif pts < 80:
    return 4.0
  elif pts < 90:
    return 4.5
  else:
    return 5.0

liczba_studentow = int(input("Podaj liczbe studentow: "))
nazwiska = []
punkty = []

for i in range(1, liczba_studentow + 1):
  nazwisko = input(f"Nazwisko studenta {i}: ")
  pts = float(input("Punkty: "))
  nazwiska.append(nazwisko)
  punkty.append(pts)

df = pd.DataFrame({"Nazwisko": nazwiska, "Punkty": punkty})
df["Ocena"] = df["Punkty"].apply(oblicz_ocene)
print()
print(df)
srednia = df["Ocena"].mean()
zaliczenia = (df["Ocena"] >= 3.0).sum()
print(f"\nSrednia ocen: {srednia}")
print(f"Liczba zaliczen: {zaliczenia}")
posortowane = df.sort_values("Punkty", ascending=False)
print("\nPosortowane wyniki:")
print(posortowane)

plt.figure(figsize=(8, 5))
plt.bar(df["Nazwisko"], df["Ocena"], color="blue")
plt.xlabel("Student")
plt.ylabel("Ocena")
plt.title("Wyniki egzaminu")
plt.ylim(0, 5.5)
plt.tight_layout()
plt.show()