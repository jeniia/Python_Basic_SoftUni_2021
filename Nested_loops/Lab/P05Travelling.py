destination = input()
total_sum = 0

while destination != "End":
    needed_money = float(input())
    while total_sum < needed_money:
        money = float(input())
        total_sum += money
        if total_sum >= needed_money:
            print(f"Going to {destination}!")
    total_sum = 0
    destination = input()