score = float(input())
if score <= 10:
    print("slow")
elif score <= 50:
    print("average")
elif score <=  150:
    print("fast")
elif score <= 1000:
    print("ultra fast")
else:
    print("extremely fast")