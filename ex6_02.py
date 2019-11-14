import random
lista = []
ilosc = 0

while ilosc < 10:
    x = random.randint(0, 100)
    lista.append(x)
    ilosc += 1
print(lista)

najmniejsza = min(lista)
najwieksza = max(lista)

indx_najm = 0
for indeksnajm in range(0, len(lista)):
    if lista[indeksnajm] == najmniejsza:
        indx_najm = indeksnajm
indx_najw = 0
for indeksnajw in range(0, len(lista)):
    if lista[indeksnajw] == najwieksza:
        indx_najw = indeksnajw

lista[indx_najm] = najwieksza
lista[indx_najw] = najmniejsza

print(lista)