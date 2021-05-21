import math

first = int(input())
second = int(input())

total = first * second
check = True

command = input()
while command != "STOP":
    piece = int(command)
    total -= piece
    if total <= 0:
        print(f"No more cake left! You need {math.fabs(total):.0f} pieces more.")
        check = False
        break
    command = input()
if check:
    print(f"{total} pieces are left.")