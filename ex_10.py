pierwsza_licz = int(input("Podaj pierwszą liczbę: "))
druga_licz = int(input("Podaj drugą liczbę: "))
operacja = input("Podaj rodzaj operacji: ")

if operacja == "+":
    wynik = pierwsza_licz+druga_licz
    print("Wynik:",wynik)
elif operacja == "-":
    wynik = pierwsza_licz-druga_licz
    print("Wynik:",wynik)
elif operacja == "*":
    wynik = pierwsza_licz*druga_licz
    print("Wynik:",wynik)
else:
    wynik = pierwsza_licz/druga_licz
    print("Wynik:",wynik)