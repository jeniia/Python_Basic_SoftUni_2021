people = int(input())
name = input()
rating = 0
scores = 0
count = 0

while name != "Finish":
    for i in range(1, people + 1):
        score = float(input())
        rating += score
    average_rating = rating / people
    scores += average_rating
    print(f"{name} - {average_rating:.2f}.")
    name = input()
    count += 1
    rating = 0

average_score = scores / count
print(f"Student's final assessment is {average_score:.2f}.")