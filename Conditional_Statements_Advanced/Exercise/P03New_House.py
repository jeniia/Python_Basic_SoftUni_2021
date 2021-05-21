import math
from math import fabs
kind_of_flowers = str(input())
count_of_flowers = int(input())
budget = float(input())
price_flowers = 0.0

if kind_of_flowers == "Roses":
 price_flowers = count_of_flowers * 5.00
elif kind_of_flowers == "Dahlias":
 price_flowers = count_of_flowers * 3.80
elif kind_of_flowers == "Tulips":
 price_flowers = count_of_flowers * 2.80
elif kind_of_flowers == "Narcissus":
 price_flowers = count_of_flowers * 3.00
elif kind_of_flowers == "Gladiolus":
 price_flowers = count_of_flowers * 2.50
if kind_of_flowers == "Roses" and count_of_flowers > 80:
    price_flowers *= 0.90
elif kind_of_flowers == "Dahlias" and count_of_flowers > 90:
    price_flowers *= 0.85
elif kind_of_flowers == "Tulips" and count_of_flowers > 80:
    price_flowers *= 0.85
elif kind_of_flowers == "Narcissus" and count_of_flowers < 120:
    price_flowers *= 1.15
elif kind_of_flowers == "Gladiolus" and count_of_flowers < 80:
    price_flowers *= 1.20
remaining_money = math.fabs(budget - price_flowers)
if budget >= price_flowers:
    print(f"Hey, you have a great garden with {count_of_flowers} {kind_of_flowers} and {remaining_money:.2f} leva left.")
else:
    print(f"Not enough money, you need {remaining_money:.2f} leva more.")