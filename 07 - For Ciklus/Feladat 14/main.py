szam1: int = None
szam2: int = None
osszeg: int = 0
osszeg2: int = 1

print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
szam1 = int(input())
print("Adja meg a végső értéket: ", end='')
szam2 = int(input())

if szam1 > szam2:
    for i in range(szam2, szam1 - 1, -1):
        if i%5 == 0:
            osszeg += i
        elif i%7 == 0:
            osszeg2 += i
    if osszeg > osszeg2:
        print(f"Az öttel osztható számok összege a nagyobb")
    else:
        print(f"A héttel osztható számok összege a nagyobb")

elif szam2 > szam1: 
    for i in range(szam1, szam2 - 1, -1):
        if i%5 == 0:
            osszeg += i
        elif i%7 == 0:
            osszeg2 += i
    if osszeg > osszeg2:
        print(f"Az öttel osztható számok összege a nagyobb")
    else:
        print(f"A héttel osztható számok összege a nagyobb")
else:
    print("A két szám egyenlő, vagy érvénytelen!")