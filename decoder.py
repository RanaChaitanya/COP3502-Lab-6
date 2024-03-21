def decode(password):
    original_password = ""
    for digit in password:
        if digit.isdigit():
            original_password += str((int(digit) - 3) % 10)
    return original_password