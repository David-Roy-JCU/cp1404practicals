

number_of_items = int(input("Enter the number of items: "))
while number_of_items <= 0:
    print("Invalid input. Must be one or more item ")
    number_of_items = int(input("Enter the number of items: "))
total_price = 0
for i in range(0, number_of_items):
    total_price += float(input("Enter Price of item {}: ".format(i+1)))
if total_price > 100:
    total_price = total_price * 0.9
print("Total Price for {} item(s) is {:.2f}".format(number_of_items, total_price))
print()