n = int(input())
l = int(input())

for first in range(1, n):
    for second in range(1, n):
        for third in range(97, 97 + l):
            for forth in range(97, 97 + l):
                for fifth in range(1, n + 1):
                    third_as_chr = chr(third)
                    forth_as_chr = chr(forth)
                    if fifth > first and fifth > second:
                        print(f"{first}{second}{third_as_chr}{forth_as_chr}{fifth}", end=" ")