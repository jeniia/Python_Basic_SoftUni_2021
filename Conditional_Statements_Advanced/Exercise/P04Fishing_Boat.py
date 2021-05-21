import math

budget = int(input())
season = str(input())
fishers = int(input())
boat_price = 0.0
if season == "Spring":
    boat_price = 3000
    if fishers <= 6:
        boat_price *= 0.90
    elif fishers <= 11:
        boat_price *= 0.85
    else:
        boat_price *= 0.75
if season == "Summer" or season == "Autumn":
    boat_price = 4200
    if fishers <= 6:
        boat_price *= 0.90
    elif fishers <= 11:
        boat_price *= 0.85
    else:
        boat_price *= 0.75
if season == "Winter":
    boat_price = 2600
    if fishers <= 6:
        boat_price *= 0.90
    elif fishers <= 11:
        boat_price *= 0.85
    else:
        boat_price *= 0.75
if fishers % 2 == 0 and season != "Autumn":
    boat_price *= 0.95
difference = math.fabs(budget - boat_price)
if budget >= boat_price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")