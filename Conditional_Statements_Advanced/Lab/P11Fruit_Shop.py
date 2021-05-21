product = str(input())
day = str(input())
amount = float(input())
result = 0
if day != "Monday" and day != "Tuesday" and day != "Wednesday" and day != "Thursday" and day != "Friday" and day != "Saturday" and day != "Sunday" or product != "banana" and product != "kiwi" and product != "orange" and product != "apple" and product != "pineapple" and product != "grapes" and product != "grapefruit":
    print("error")
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if product == "banana":
        result = amount * 2.50
        print(f"{result:.2f}")
    if product == "apple":
        result = amount * 1.20
        print(f"{result:.2f}")
    if product == "orange":
        result = amount * 0.85
        print(f"{result:.2f}")
    if product == "grapefruit":
        result = amount * 1.40
        print(f"{result:.2f}")
    if product == "kiwi":
        result = amount * 2.70
        print(f"{result:.2f}")
    if product == "pineapple":
        result = amount * 5.50
        print(f"{result:.2f}")
    if product == "grapes":
        result = amount * 3.85
        print(f"{result:.2f}")
elif day == "Saturday" or day == "Sunday":
    if product == "banana":
        result = amount * 2.70
        print(f"{result:.2f}")
    if product == "apple":
        result = amount * 1.25
        print(f"{result:.2f}")
    if product == "orange":
        result = amount * 0.90
        print(f"{result:.2f}")
    if product == "grapefruit":
        result = amount * 1.60
        print(f"{result:.2f}")
    if product == "kiwi":
        result = amount * 3.00
        print(f"{result:.2f}")
    if product == "pineapple":
        result = amount * 5.60
        print(f"{result:.2f}")
    if product == "grapes":
        result = amount * 4.20
        print(f"{result:.2f}")