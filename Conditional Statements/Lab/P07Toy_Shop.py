trip_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

profit = (puzzles_count * 2.60) + (dolls_count * 3) + (teddy_bears_count * 4.10) + (minions_count * 8.20) + (
            trucks_count * 2)
total_count = puzzles_count + dolls_count + teddy_bears_count + minions_count + trucks_count
if total_count >= 50:
    profit = profit - 0.25 * profit

rent = profit * 0.10
profit -= rent

if profit >= trip_price:
    left_money = profit - trip_price
    print(f"Yes! {left_money:.2f} lv left.")
else:
    need_money = trip_price - profit
    print(f"Not enough money! {need_money:.2f} lv needed.")
