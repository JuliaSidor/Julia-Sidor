pon_temp = int(input("Pogoda w poniedzialek: "))
wto_temp = int(input("Pogoda we wtorek: "))
srd_temp = int(input("Pogoda w środe: "))
czw_temp = int(input("Pogoda w czwartek: "))
pia_temp = int(input("Pogoda w piątek: "))
sob_temp = int(input("Pogoda w sobote: "))
nie_temp = int(input("Pogoda w niedziele: "))

srednia_temp = (pon_temp+wto_temp+srd_temp+czw_temp+pia_temp+sob_temp+nie_temp)/7
print(f"Średnia temperatura wynosiła {int(srednia_temp)} stopni Celcjusza")