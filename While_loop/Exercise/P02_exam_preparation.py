poor_rating = int(input())

command = input()
total = 0
counter = 0
last_problem = ""
poor = 0

while command != "Enough":
    rating = int(input())
    if rating <= 4:
        poor += 1
        counter += 1
        if poor == poor_rating:
            print(f"You need a break, {poor_rating} poor grades.")
            break
    else:
        counter += 1
        last_problem = command
    total += rating
    command = input()
average_score = total / counter

if poor != poor_rating:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {counter}")
    print(f"Last problem: {last_problem}")