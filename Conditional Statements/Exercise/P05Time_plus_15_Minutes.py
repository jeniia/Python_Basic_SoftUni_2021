time = int(input())
minutes = int(input())
minutes += 15
if minutes > 59:
    minutes -= 60
    time += 1
    if time == 24:
        time = 0
if minutes <= 9:
    print(f"{time}:0{minutes}")
else:
    print(f"{time}:{minutes}")