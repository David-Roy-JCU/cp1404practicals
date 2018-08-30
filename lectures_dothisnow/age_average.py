
# use a counter
total_people = 0
total_age = 0
age = int(input("enter age: "))
while age >= 0:
    total_age = total_age + age
    total_people += 1
    age = int(input("enter age: "))
average_age = total_age // total_people
print("the average age is {} in the group of {} people".format(average_age, total_people))


# use a list
ages = []
age = int(input("enter age: "))
while age >= 0:
    ages.append(age)
    age = int(input("enter age: "))
average_age = sum(ages) // len(ages)
print("the average age is {} in the group of {} people".format(average_age, len(ages)))
