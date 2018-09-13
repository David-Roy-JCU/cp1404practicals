""" CP1404 week 08 Do This Now """

def main():
    names_to_ages = {"Bill": 21, "Jane": 34, "Sven": 56}
    threshold_age = int(input("Enter age"))
    names = find_names_for_age(names_to_ages, threshold_age)
    print("names of people who are {} years and over are: ".format(threshold_age))
    print(names)


def find_names_for_age(names_to_ages, threshold_age):
    names = []
    for name in names_to_ages:
        if names_to_ages[name] >= threshold_age:
            names.append(name)
    return names

main()

