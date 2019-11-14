produkty = {'jablka': 3.50, 'pomarancze': 4.40, 'winogrona': 5.50, 'nektarynki': 3.20, 'kokos': 8.90}
suma = 0

while True:
    owoc = input("Co chce kupic? ")

    if owoc == "koniec":
        break
    if owoc not in produkty:
        print("Nie ma takiego produktu")
        continue

    ilosc = int(input("Ile kg?: "))
    cena_za_kg = produkty[owoc]
    cena = ilosc*cena_za_kg

    suma += cena

print(f"Za zakupy zapłace: {suma} zł")
