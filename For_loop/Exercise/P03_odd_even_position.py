import sys

n = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for i in range(0, n):
    num = float(input())
    if i % 2 == 0:
        if num > odd_max:
            odd_max = num
        if num < odd_min:
            odd_min = num
        odd_sum += num
    else:
        if num < even_min:
            even_min = num
        if num > even_max:
            even_max = num
        even_sum += num
print(f"OddSum={odd_sum:.2f},")
if odd_min != sys.maxsize:
    print(f"OddMin={odd_min:.2f},")
else:
    print(f"OddMin=No,")
if odd_max != -sys.maxsize:
    print(f"OddMax={odd_max:.2f},")
else:
    print(f"OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
if even_min != sys.maxsize:
    print(f"EvenMin={even_min:.2f},")
else:
    print(f"EvenMin=No,")
if even_max != -sys.maxsize:
    print(f"EvenMax={even_max:.2f}")
else:
    print(f"EvenMax=No")