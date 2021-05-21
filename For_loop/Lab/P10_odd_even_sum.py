n = int(input())

even_sum = 0
odd_sum = 0

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    if even_sum > odd_sum:
        diff = even_sum - odd_sum
        print("No")
        print(f"Diff = {diff}")
    else:
        diff = odd_sum - even_sum
        print("No")
        print(f"Diff = {diff}")