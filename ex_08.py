miara1 = int(input("Podaj dlugos boku: "))
miara2 = int(input("Podaj dlugosc boku: "))
wysokosc = int(input("Podaj wysokosc: "))

#I sposob
objetosc = miara1*miara2*wysokosc
czyWieksza = objetosc > 1000
print(f"""Objetosc kartonu wynosi: {objetosc} cm3
Czy jest wieksza od litra?: {czyWieksza}""")

#II sposob
if objetosc > 1000:
    print("Objetosc wynosi:",objetosc)
    print("Objetosc jest wieksza od litra")
else:
    print("Objetosc wynosi:",objetosc)
    print("Objetosc nie jest wieksza od litra")