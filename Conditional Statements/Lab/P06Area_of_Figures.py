import math
figure = str(input())
face = 0
if figure == "square":
    side_a = float(input())
    face = side_a * side_a
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    face = side_a * side_b
elif figure == "circle":
    radius = float(input())
    face = math.pi * (math.pow(radius, 2))
elif figure == "triangle":
    side_a = float(input())
    height_h = float(input())
    face = side_a * height_h / 2

print(f"{face:.3f}")