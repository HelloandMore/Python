number: int = None

print("Adj meg egy számot, ami -30 és +40 között van > ", end="")
number = int(input())

if number >= -30 and number <= 40:
    print(f"A szám ({number}) megfelel a követelménynek")
else:
    print(f"A szám ({number}) NEM felel meg a követelménynek!")