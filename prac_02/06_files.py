"""
CP1404 practical - files
"""

# OUTPUT_FILE = "name.txt"
# name = input("Please enter your name")
# out_file = open(OUTPUT_FILE, 'w')
# print(name, file=out_file)
# out_file.close()

INPUT_FILE = "name.txt"
in_file = open(INPUT_FILE, 'r')
name_in_file = in_file.read()
print("Your name is", name_in_file)
in_file.close()




