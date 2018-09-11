"""
CP1404 prac 05 hec colours dictionary
"""

COLOURS = {"azure1": "#f0ffff", "coral": "#ff7f50", "darkorchid": "#9932cc"}

colour = input("Enter colour name").lower()
while colour != "":
    if colour in COLOURS:
        hex_code = COLOURS[colour]
        print("{} is {}".format(colour, hex_code))
    else:
        print("not in dictionary")
    colour = input("Enter colour name").lower()



