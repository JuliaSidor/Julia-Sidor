import random
lista = []
ilosc = 0
while ilosc < 10:
    x = random.randint(-100, 100)
    lista.append(x)
    ilosc += 1
print(lista)
dodatnie = 0
ujemne = 0
for liczba in range(0, len(lista)):
    if lista[liczba] >= 0:
        dodatnie += 1
    else:
        ujemne += 1

print(f"Liczba ujemnych : {ujemne} Liczba dodatnich: {dodatnie}")