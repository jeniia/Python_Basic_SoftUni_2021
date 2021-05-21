import math

n = int(input())
max_num = 0
sum_numbers = 0

for i in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_numbers += num

sum_numbers -= max_num
if sum_numbers == max_num:
    print("Yes")
    print(f"Sum = {sum_numbers}")
else:
    print("No")
    print(f"Diff = {math.fabs(max_num - sum_numbers):.0f}")