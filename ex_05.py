miastoA = input("Miasto A: ")
miastoB = input("Miasto B: ")
dystans = float(input(f"Dystans {miastoA}-{miastoB}: "))
cena_paliwa = float(input("Cena paliwa: "))
spalanie = float(input("Spalanie na 100 km: "))

koszt = (dystans/100)*spalanie*cena_paliwa
print(f"Koszt przejazdu {miastoA}-{miastoB} to {round(koszt)} PLN")