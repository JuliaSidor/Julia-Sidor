lista_liczb = []
ilosc = 0
while ilosc < 10:
    wybor = int(input("Podaj liczbe: "))
    lista_liczb.append(wybor)
    ilosc += 1

srdn = sum(lista_liczb)/10
print(f"Średnia wartość wynosi: {srdn:.2f} ")