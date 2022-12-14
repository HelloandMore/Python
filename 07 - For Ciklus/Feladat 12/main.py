kezdo: int = None
vegso: int = None
osszeg: int = 0

print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
kezdo = int(input().strip())
print("Adja meg a végső értéket: ", end='')
vegso = int(input().strip())

if kezdo > vegso:
    for i in range(kezdo, vegso - 1, -1):
        if i%3 == 0:
            osszeg += 1
    print(f"{osszeg} szám osztható 3-al")
    
elif vegso > kezdo: 
    for i in range(vegso, kezdo - 1, -1):
        if i%3 == 0:
            osszeg += 1
    print(f"{osszeg} szám osztható 3-al")
else:
    print("A két szám egyenlő, vagy érvénytelen!")