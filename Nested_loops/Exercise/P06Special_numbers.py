n = int(input())

for special_number in range(1111, 9999):
    special_number = str(special_number)
    if "0" not in special_number:
        first_num = int(special_number[0])
        second_num = int(special_number[1])
        third_num = int(special_number[2])
        fourth_num = int(special_number[3])

        if n % first_num == 0:
            if n % second_num == 0:
               if n % third_num == 0:
                   if n % fourth_num == 0:
                       print(special_number, end=' ')