ile_ich_jest = 0
podzielne_3 = 0
podzielne_5 = 0
podzielne_3_5 = 0

for liczba in range(0, 101):
    if (liczba%3 == 0) or (liczba%5 == 0):
        print(liczba)
        ile_ich_jest +=1
        if(liczba%3 == 0 and liczba%5 == 0):
            podzielne_3_5 += 1
        elif (liczba %3 == 0 and liczba%5 != 0):
            podzielne_3 +=1
        else:
            podzielne_5 +=1
print(f"""W przedziale 0-100 jest {ile_ich_jest} liczb podzielnych przez 3 lub 5.
Podzielnych przez 3 i 5: {podzielne_3_5}
Podzielnych tylko przez 3: {podzielne_3}
Podzielnych tylko przez 5: {podzielne_5}""")