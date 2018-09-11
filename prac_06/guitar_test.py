""" CP1404 guitar test pythoing file """

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
strat = Guitar("Fender Stratocaster", 2003, 1445.00)

print(gibson)
print(strat)

print(gibson.get_age())