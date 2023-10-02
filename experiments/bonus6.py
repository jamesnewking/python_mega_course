contents = ["One first", "Two second", "Three third"]
fileNames = ["fileOne.txt", "fileTwo.txt", "fileThree"]
# for index, content in enumerate(contents):
#     currentFile = open(rf"../files/{fileNames[index]}", "w")
#     currentFile.writelines(content)
#     currentFile.close()
for content, fileName in zip(contents, fileNames):
    currentFile = open(rf"../files/{fileName}", "w")
    currentFile.write(content)
    currentFile.close()


