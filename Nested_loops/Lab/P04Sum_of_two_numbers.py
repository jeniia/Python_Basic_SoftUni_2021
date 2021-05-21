start = int(input())
end = int(input())
magic_number = int(input())
counter = 0
combination = 0

for i in range(start,end + 1):
    for j in range(start, end + 1):
        combination += 1
        if i + j == magic_number:
            if counter == 1:
                break
            print(f"Combination N:{combination}",end=" ")
            print(f"({i} + {j} = {i + j})")
            counter += 1
if counter == 0:
    print(f"{combination} combinations - neither equals {magic_number}")