kwota_odkladana = int(input("Ile odkładasz tygodniowo: "))
ile_tygodni = int(input("Ile tygodni: "))
suma_oszczednosci = 0
for i in range(1,ile_tygodni+1):
    suma_oszczednosci += kwota_odkladana
    print(f"Tydzień {i}: {suma_oszczednosci} zł")
print(f"Lączne oszczędności: {suma_oszczednosci} zł")

