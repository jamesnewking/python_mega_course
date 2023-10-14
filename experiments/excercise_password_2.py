password = input("Enter a password: ")
passwordLength = len(password)
if passwordLength > 7:
    print("Great password there")
elif passwordLength == 7:
    print("Password is OK, but not too strong")
else:
    print("Your password is weak")
