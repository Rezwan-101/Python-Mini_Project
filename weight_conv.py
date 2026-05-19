weight = input("Enter your weight: ")
unit = input("Enter the unit kg or lb (K or LB): ")

if unit.upper() == "K":
    weight = float(weight) * 2.205 
    unit = "Lbs"
    print(f"your weight is {round(weight, 2)} {unit}")
elif unit.upper() == "LB":
    weight = float(weight) / 2.205
    unit = "Kg"
    print(f"your weight is {round(weight, 2)} {unit}")
else:
    print(f"{unit} was not valid")


