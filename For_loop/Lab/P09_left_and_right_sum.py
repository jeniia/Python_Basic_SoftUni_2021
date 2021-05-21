x = int(input())

n = 2 * x

left_sum = 0
right_sum = 0

for i in range(0, n):
    number = int(input())
    if i < n/2:
        left_sum += number
    else:
        right_sum += number
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    if left_sum > right_sum:
        diff = left_sum - right_sum
        print(f"No, diff = {diff}")
    else:
        diff = right_sum - left_sum
        print(f"No, diff = {diff}")