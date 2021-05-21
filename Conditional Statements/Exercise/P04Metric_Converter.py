number = float(input())
input_metric = str(input())
output_metric = str(input())
if input_metric == "mm":
    number = number / 1000
elif input_metric == "cm":
    number = number / 100
if output_metric == "mm":
    number = number * 1000
elif output_metric == "cm":
    number = number * 100
print(f"{number:.3f}")