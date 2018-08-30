for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_stars = int(input("Enter number of stars: "))
for i in range(0, number_of_stars):
    print('*', end='')
print()

number_of_stars = int(input("Enter number of stars: "))
for line in range(0, number_of_stars):
    for i in range(0, line + 1):
        print("*", end='')
    print()
print()

for x in range(0, number_of_stars):
    for i in range(0, x+1):
        # do something