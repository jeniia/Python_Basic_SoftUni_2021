movie_name = input()
tickets = 0
student_tickets = 0
total_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_student_tickets = 0
total_standard_tickets = 0
total_kids_tickets = 0

while movie_name != "Finish":
    capacity = int(input())
    while tickets < capacity:
        type_tickets = input()
        if type_tickets == "End":
            break
        tickets += 1
        if type_tickets == "student":
            student_tickets += 1
        elif type_tickets == "kid":
            kid_tickets += 1
        elif type_tickets == "standard":
            standard_tickets += 1
    print(f"{movie_name} - {((tickets / capacity) * 100):.2f}% full.")
    total_tickets += tickets
    total_kids_tickets += kid_tickets
    total_standard_tickets += standard_tickets
    total_student_tickets += student_tickets
    tickets = 0
    student_tickets = 0
    standard_tickets = 0
    kid_tickets = 0
    movie_name = input()

print(f"Total tickets: {total_tickets}")
print(f"{((total_student_tickets / total_tickets) * 100):.2f}% student tickets.")
print(f"{((total_standard_tickets / total_tickets) * 100):.2f}% standard tickets.")
print(f"{((total_kids_tickets / total_tickets) * 100):.2f}% kids tickets.")
