import json

with open("../files/questions.json", "r") as file:
    content = file.read()

data = json.loads(content)
questionsAsked = 0
questionsCorrect = 0
for question in data:
    questionsAsked = questionsAsked + 1
    print(f"Question number {questionsAsked}")
    print(question["question"])
    for index, option in enumerate(question["options"]):
        print(f"{index + 1}) {option}")
    question["guess"] = int(input("Your answer: "))
    correctAnswer = question["answer"]
    print(f"Correct answer is {correctAnswer}")
    if question["guess"] == correctAnswer:
        questionsCorrect = questionsCorrect + 1
        print("Correct!")
    else:
        print("Sorry, that's not correct!")
print(f"You got {questionsCorrect}/{questionsAsked} correct.")
