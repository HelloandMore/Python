start: int = None
end: int = None
osszeg: int = 0

print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
start = int(input())
print("Adja meg a végső értéket: ", end='')
end = int(input())

if start > end:
    for i in range(end, start-1, -1):
        if i%2:
            if i%3 == 0:
                osszeg += 1

else: 
    for i in range(start, end-1, -1):
        if i%2:
            if i%3 == 0:
                osszeg += 1