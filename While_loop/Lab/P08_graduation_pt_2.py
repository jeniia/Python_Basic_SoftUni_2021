name = input()
counter = 0
n = 0
total = 0

while n < 12:
    grade = float(input())
    if grade >= 4:
        total += grade
    else:
        counter += 1
        if counter == 2:
            print(f"{name} has been excluded at {n} grade")
            break
    n += 1

if counter < 2:
    print(f"{name} graduated. Average grade: {(total / 12):.2f}")