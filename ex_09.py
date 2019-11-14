rok_ur = int(input("Podaj swój rok urodzenia: "))
rok_akt = int(input("Podaj aktualny rok: "))
ile_mam_lat = rok_akt-rok_ur
if ile_mam_lat >= 18:
    print(f"Mam {ile_mam_lat} lat i jestem pełnoletni/a ")
else:
    print(f"Mam {ile_mam_lat} lat i jestem niepełnoletni/a")