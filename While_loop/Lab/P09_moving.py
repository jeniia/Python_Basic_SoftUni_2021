width = int(input())
length = int(input())
height = int(input())

space = width * length * height
boxes = 0

command = input()
while command != "Done":
    command = int(command)
    boxes += command
    if space < boxes:
        print(f"No more free space! You need {boxes - space} Cubic meters more.")
        break
    command = input()
if boxes < space:
    print(f"{space - boxes} Cubic meters left.")