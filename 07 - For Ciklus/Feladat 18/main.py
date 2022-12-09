szam1: int = None
szam2: int = None
osszeg: int = 0
elsoSzam: int = 0
masodikSzam: int = 0
elso: bool = True

print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
szam1 = int(input())
print("Adja meg a végső értéket: ", end='')
szam2 = int(input())

if szam1 > szam2:
    for i in range(szam2, szam1 + 1, 1):
        if elso:
            osszeg += i
            elso = False
        else:
            osszeg -= i
            elso = True
    print(osszeg)

elif szam2 > szam1: 
    for i in range(szam1, szam2 + 1, 1):
        if elso:
            osszeg += i
            elso = False
        else:
            osszeg -= i
            elso = True
    print(osszeg)
else:
    print("A két szám egyenlő, vagy érvénytelen!")