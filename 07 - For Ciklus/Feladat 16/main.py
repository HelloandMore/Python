szam1: int = 0
szam2: int = 0
osszeg1: int = 0
osszeg2: int = 0
mennyiseg1: int = 1
mennyiseg2: int = 1
print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
szam1 = int(input())
print("Adja meg a végső értéket: ", end='')
szam2 = int(input())

if szam1 > szam2:
    for i in range(szam1, szam2 - 1, -1):
        if i%2== 0:
            osszeg1 += i
            mennyiseg1 += 1
        if i%2:
            osszeg2 += i
            mennyiseg2 += 1
    print(f"Páros zsámok átlaga: {osszeg1/mennyiseg1}")
    print(f"Páratlan számok összege: {osszeg2/mennyiseg2}")

elif szam2 > szam1: 
    for i in range(szam2, szam1 - 1, -1):
        if i%2 == 0:
            osszeg1 += i
            mennyiseg1 += 1
        if i%2:
            osszeg2 += i
            mennyiseg2 += 1
    print(f"Páros zsámok átlaga: {osszeg1/mennyiseg1}")
    print(f"Páratlan számok összege: {osszeg2/mennyiseg2}")
else:
    print("A két szám egyenlő, vagy érvénytelen!")