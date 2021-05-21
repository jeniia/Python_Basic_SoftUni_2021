command = input()

sum_non_prime = 0
sum_prime = 0


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


while command != "stop":
    number = int(command)
    if number < 0:
        print("Number is negative.")
    else:
        if is_prime(number):
            sum_prime += number
        else:
            sum_non_prime += number
    command = input()
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
