
password = input("Enter a password and it's strength will be determined:")
password = password.strip()
check = {"length": False,
         "capital": False,
         "lower": False,
         "number": False}
passText = f'\x1b[0;30;42mPASS\x1b[0m'
failText = f'\x1b[0;30;41mFAIL\x1b[0m'
resultText = {"length": failText,
              "capital": failText,
              "lower": failText,
              "number": failText}
passwordLength = len(password)
if passwordLength >= 8:
    check["length"] = True
    resultText["length"] = passText
for character in password:
    if character.isupper() and not check["capital"]:
        check["capital"] = True
        resultText["capital"] = passText
    if character.islower() and not check["lower"]:
        check["lower"] = True
        resultText["lower"] = passText
    if character.isnumeric() and not check["number"]:
        check["number"] = True
        resultText["number"] = passText
print(f'Checking criteria:\n'
      f'at least 8 characters {resultText["length"]}\n'
      f'at least 1 upper case {resultText["capital"]}\n'
      f'at least 1 lower case {resultText["lower"]}\n'
      f'at least 1 number {resultText["number"]}')
if all(check.values()):
    print(f'\x1b[0;30;42mSTRONG\x1b[0m password')
else:
    print(f'\x1b[0;30;41mWEAK\x1b[0m password')