trip_money = float(input())
available_money = float(input())

spend = 0
days = 0

while available_money < trip_money:
    days += 1
    action = input()
    money = float(input())
    if action == "save":
        spend = 0
        available_money += money
    elif action == "spend":
        spend += 1
        if available_money < money:
            available_money = 0
        else:
            available_money -= money
        if spend == 5:
            print("You can't save the money.")
            print(f"{days}")
            break
if available_money >= trip_money:
    print(f"You saved the money for {days} days.")