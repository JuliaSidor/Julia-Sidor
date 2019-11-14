a = ("abc", 8, 10, True, "Kim Taehyung", 12, "Kabaty", None, 128.0, 69, "Byun Baekhyun")
#drugi element
print(a[2])
print("=========================")
#przedostatni element
print(a[len(a)-2])
print("=========================")
#elementy od trzeciego do siódmego włącznie
print(a[3:8])
print("=========================")
#co trzeci element

for liczba in range(0, len(a), 3):
    print(a[liczba])
print("=========================")
#co drugi element licząc od końca

for liczba in range(len(a)-1, -1, -2):
    print(a[liczba])