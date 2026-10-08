wiek = int(input("Podaj wiek: "))
dokument_tozsamosci = str("Czy masz dokument tożsamości? ")
zgoda_opiekuna = str("Czy masz zgode opiekuna? ")
if wiek <13:
    print("Wypożyczenie niemożliwe")
else:
    dokument_tozsamosci = str(input("Czy masz dokument tożsamości? "))
    zgoda_opiekuna = str(input("Czy masz zgode opiekuna? "))
    if dokument_tozsamosci == "tak" and zgoda_opiekuna == "tak":
        print("Wypożyczenie możliwe")
    else:
        print("Wypożyczenie niemożliwe")
