szam1: int = None
szam2: int = None
osszeg: int = 0

print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
szam1 = int(input())
print("Adja meg a végső értéket: ", end='')
szam2 = int(input())

if szam1 > szam2:
    for i in range(szam2, szam1 - 1, -1):
        if i%3 == 0:
            osszeg += 1
    print(f"{osszeg} szám osztható 3-al")
    
elif szam2 > szam1: 
    for i in range(szam2, szam1 - 1, -1):
        if i%3 == 0:
            osszeg += 1
    print(f"{osszeg} szám osztható 3-al")
else:
    print("A két szám egyenlő, vagy érvénytelen!")