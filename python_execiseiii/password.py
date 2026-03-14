def validate_password(password):

    if len(password) < 8:
        return "Password must be at least 8 characters"

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if not has_upper:
        return "Password must contain an uppercase letter"

    if not has_lower:
        return "Password must contain a lowercase letter"

    if not has_digit:
        return "Password must contain a digit"

    return "Password is valid"


# user input
password = input("Enter your password: ")

print(validate_password(password))