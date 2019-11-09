rok_urodzenia = int(input("Podaj rok urodzenia postaci ( przed 1960 r): "))
ile_lat = 2019 - rok_urodzenia
ile_pokol = int(ile_lat/30)
relacja = (("pra")*(ile_pokol-2))+("babka")

print(f"""Rok urodzenia postaci: {rok_urodzenia}
Ta osoba urodziła się przed {ile_lat} laty.
To mogła być Twoja {relacja}.""")
