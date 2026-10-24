n = int(input("Enter number of passwords: "))

for i in range(n):
    password = input("Enter password: ")

    # Rule 1: At least 15 characters
    if len(password) >= 15:
        print("STRONG")

    # Rule 2: At least 8 characters + number + lowercase letter
    elif len(password) >= 8 and any(c.isdigit() for c in password) and any(c.islower() for c in password):
        print("STRONG")

    else:
        print("WEAK_LENGTH")