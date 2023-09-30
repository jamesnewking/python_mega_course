prompt = "enter a password: "
password = input(prompt)
guess_prompt = "Guess the password: "
guess = input(guess_prompt)
tries = 1
while guess != password:
    print("Number of tries: ",tries)
    guess = input(guess_prompt)
    tries = tries +1
print("Good job, the password was:", password, "and you guessed", tries, "times")