""""
CP1404 Read numbers from file and add them together

"""

INPUT_FILE = "numbers.txt"
in_file = open(INPUT_FILE, 'r')
total = 0
for line in in_file:
    total += int(line)
print("Total is:", str(total))
in_file.close()