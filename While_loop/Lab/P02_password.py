name = input()
password = input()

input_pass = input()
while input_pass != password:
    input_pass = input()

if input_pass == password:
    print(f"Welcome {name}!")