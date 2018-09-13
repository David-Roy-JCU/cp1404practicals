""" CP1404 Prac 06 guitars file for adding guitars to a list of guitar objects """

from prac_06.guitar import Guitar

guitars = []

# name = input("Name: ")
# while name != '':
#     year = int(input("Year: "))
#     cost = float(input("Cost: "))
#     guitars.append(Guitar(name, year, cost))
#     print("{} ({}) : ${} added".format(name, year, cost))
#     name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))
guitars.append(Guitar("Ibanez JMP100 P3", 1995, 1830))


print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage = "(vintage)" if guitar.is_vintage() else ""
    print("Guitar {}: {:20} ({}), worth ${:>8.2f} {}".format(i, guitar.name, guitar.year, guitar.cost, vintage))
