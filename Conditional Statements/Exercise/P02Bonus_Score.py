number_start = int(input())
bonus_score = 0
if number_start <= 100:
    bonus_score = 5
elif number_start > 1000:
    bonus_score = number_start * 0.10
else:
    bonus_score = number_start * 0.20
if number_start % 2 == 0:
    bonus_score = bonus_score + 1
elif number_start % 10 == 5:
    bonus_score = bonus_score + 2
print(bonus_score)
print(bonus_score + number_start)