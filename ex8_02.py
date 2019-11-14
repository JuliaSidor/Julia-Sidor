napis = input("napis: ")

pocz_indx = napis.find("<") #znajduje indeks znaku "<"
konc_indx = napis.find(">") #znajduje indeks znaku "<"

indxp = pocz_indx+1
indxk = konc_indx #przy wycinaniu [a:b] zwraca a do b-1

dlugosc_wyrazu = len(napis[indxp:konc_indx])
print(dlugosc_wyrazu)