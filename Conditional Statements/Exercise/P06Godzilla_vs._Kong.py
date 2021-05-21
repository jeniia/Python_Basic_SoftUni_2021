budget = float(input())
extras = int(input())
price_for_one_clothing = float(input())

price_decor = (budget * 0.10)
price_for_all_extras = extras * price_for_one_clothing
if extras > 150:
    price_for_all_extras= price_for_all_extras * 0.90
total_sum_for_movie = price_decor + price_for_all_extras
left_money = budget - total_sum_for_movie
needed_money = total_sum_for_movie - budget
if total_sum_for_movie > budget:
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")
if total_sum_for_movie <= budget:
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")