searched_book = input()
book = input()
counter = 0
operations = False

while book != "No More Books":
    if book == searched_book:
        operations = True
        print(f"You checked {counter} books and found it.")
        break
    counter += 1
    book = input()
if not operations:
    print(f"The book you search is not here!")
    print(f"You checked {counter} books.")