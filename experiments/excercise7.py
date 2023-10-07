filenames = ["a.txt", "b.txt", "c.txt"]
for filename in filenames:
    fileContent = open(rf"..\files\{filename}", "r")
    content = fileContent.read()
    print(content)
