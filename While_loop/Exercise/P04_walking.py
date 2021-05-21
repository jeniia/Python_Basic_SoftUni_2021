target  = 10000
steps = 0

while steps <= target:
    command = input()
    if command == "Going home":
        command = input()
        steps += int(command)
        break
    steps += int(command)
if steps < target:
    difference = target - steps
    print(f"{difference} more steps to reach goal.")
else:
    difference = steps - target
    print(f"Goal reached! Good job!")
    print(f"{difference} steps over the goal!")