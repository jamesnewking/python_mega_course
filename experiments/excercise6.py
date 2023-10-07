# create the list of files and put in the content
filenames = ['doc.txt', 'report.txt', 'presentation.txt']
content = "hello"
for filename in filenames:
    writeFile = open(rf"..\files\{filename}", "w")
    writeFile.write(content)
    writeFile.close()

# delete the files
# import os
# for filename in filenames:
#     path = rf"..\files\{filename}"
#     if os.path.isfile(path):
#         os.remove(path)
