word = input()
lists = {"a": 1, "e": 2, "i":3, "o": 4,"u":5}
total = 0
for i in word:
    if i in lists:
        total += lists[i]
print(total)