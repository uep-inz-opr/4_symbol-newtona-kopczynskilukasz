name = input("podaj swoje imię: ")

if not name.isalpha():
    print("Tylko litery są dozwolone!")
else:
    print("Hello " + name)
