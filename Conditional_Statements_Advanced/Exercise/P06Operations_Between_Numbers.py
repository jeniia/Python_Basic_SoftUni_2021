n1 = int(input())
n2 = int(input())
operation = str(input())

result = 0
even_or_odd = ""
output = ""
if operation == "+":
    result = n1 + n2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    output = f"{n1} {operation} {n2} = {result} - {even_or_odd}"
elif operation == "-":
    result = n1 - n2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    output = f"{n1} {operation} {n2} = {result} - {even_or_odd}"
elif operation == "*":
    result = n1 * n2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    output = f"{n1} {operation} {n2} = {result} - {even_or_odd}"
elif operation == "/":
    if n2 == 0:
        output = f"Cannot divide {n1} by zero"
    else:
        divide_result = 1.0 * n1 / n2
        output = f"{n1} {operation} {n2} = {divide_result:.2f}"
elif operation == "%":
    if n2 == 0:
        output = f"Cannot divide {n1} by zero"
    else:
        result = n1 % n2
        output = f"{n1} {operation} {n2} = {result}"
print(output)