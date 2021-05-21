age = int(input())
price_wash = float(input())
price_toys = int(input())

money = 0
toys = 0
brother_money = 0

for i in range(1, age + 1):
    if i % 2 ==0:
        money += (i * 10) / 2
        brother_money += 1
    else:
        toys += 1
money -= brother_money
toys_money = price_toys * toys
money += toys_money

if money >= price_wash:
    print(f"Yes! {(money - price_wash):.2f}")
else:
    print(f"No! {(price_wash - money):.2f}")