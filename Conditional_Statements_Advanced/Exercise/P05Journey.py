budget = float(input())
season = str(input())
price = 0.0
if season == "summer":
    if budget <= 100:
        print("Somewhere in Bulgaria")
        price = budget * 30 / 100
        print(f"Camp - {price:.2f}")
    elif 100 < budget <= 1000:
        print("Somewhere in Balkans")
        price = budget * 40 / 100
        print(f"Camp - {price:.2f}")
    else:
        print("Somewhere in Europe")
        price = budget * 90 / 100
        print(f"Hotel - {price:.2f}")
if season == "winter":
    if budget <= 100:
        print("Somewhere in Bulgaria")
        price = budget * 70 / 100
        print(f"Hotel - {price:.2f}")
    elif 100 < budget <= 1000:
        print("Somewhere in Balkans")
        price = budget * 80 / 100
        print(f"Hotel - {price:.2f}")
    else:
        print("Somewhere in Europe")
        price = budget * 90 / 100
        print(f"Hotel - {price:.2f}")
