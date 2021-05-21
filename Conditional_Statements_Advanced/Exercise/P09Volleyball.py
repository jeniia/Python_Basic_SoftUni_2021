import math

year = str(input())
p = int(input())
h = int(input())
volleyball_time = 0.0
volleyball_time += (48 - h) * 3.0 / 4
volleyball_time += p * 2.0 / 3
volleyball_time += h
if year == "leap":
    volleyball_time *= 1.15
print(f"{math.floor(volleyball_time):.0f}")