command = input()
total = 0

while command != "NoMoreMoney":
    command = float(command)
    if command < 0:
        print("Invalid operation!")
        break
    total += command
    print(f"Increase: {command:.2f}")
    command = input()
print(f"Total: {total:.2f}")