n = int(input())
numbers = []
max_num = 0
min_num = 0

for i in range(0, n):
    num = int(input())
    numbers.append(num)

max_num = max(numbers)
min_num = min(numbers)

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")