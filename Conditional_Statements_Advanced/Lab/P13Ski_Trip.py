count_days = int(input())
type_room = str(input())
review = str(input())

count_nights = count_days - 1
price = 0
if type_room == "room for one person":
   price = count_nights * 18.00
elif type_room == "apartment":
    price = count_nights * 25.00
    if count_days < 10:
        price -= price * 0.30
    elif 10 <= count_days <= 15:
        price -= price * 0.35
    elif count_days > 15:
        price -= price * 0.50
elif type_room == "president apartment":
    price = count_nights * 35.00
    if count_days < 10:
        price -= price * 0.10
    elif 10 <= count_days <= 15:
        price -= price * 0.15
    elif count_days > 15:
        price -= price * 0.20
if review == "positive":
    price += price * 0.25
else:
    price -= price * 0.10
print(f"{price:.2f}")