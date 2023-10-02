import os.path
newMemberName = input("Add a new member: ")
if os.path.exists(rf"../files/members.txt"):
    memberFile = open(rf"../files/members.txt", "r")
    currentMembers = memberFile.readlines()
    memberFile.close()
    currentMembers.append(newMemberName + "\n")
    memberFile = open(rf"../files/members.txt", "w")
    memberFile.writelines(currentMembers)
    memberFile.close()
else:
    memberFile = open(rf"../files/members.txt", "w")
    currentMembers = newMemberName + "\n"
    memberFile.write(currentMembers)
    memberFile.close()
