slowo = input("Podaj słowo: ")
samoglos = 0

#a e i o u y
lista = ["a", "e", "i", "o", "u", "y"]

for i in range(0, len(slowo)):
    if slowo[i] in lista:
        samoglos += 1

print(f"Liczba samogłosek w słowie wynosi: {samoglos}")