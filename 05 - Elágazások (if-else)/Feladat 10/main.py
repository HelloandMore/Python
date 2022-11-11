from http.client import NotConnected


from os import system

number: int = None

print("Adj meg egy számot > ", end="")
number = int(input())
system('echo.')

if number%2 == 0 and number%3 == 0:
    print("ZIZI")
elif number%2 == 0:
    print("BIZ")
elif number%3 == 0:
    print("BAZ")