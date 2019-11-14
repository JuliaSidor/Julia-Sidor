slowo = input("Podaj słowo: ")
i = 0
lista = {}
while i < len(slowo):
    literka = slowo[i]
    ilosc = slowo.count(literka)
    lista[literka] = ilosc
    i += 1
print(lista)