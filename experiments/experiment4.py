# a = ["jon", "peter", "abe"]
# a.sort()
# for index, item in enumerate(a):
#     print(f"{index+1}.{item.capitalize()}")

ips = ['100.122.133.105', '100.122.133.111']
choseIndex = input("Chose an index ")
if(str.isdigit(choseIndex)):
    choseIndex = int(choseIndex)
    print(f"You chose {ips[choseIndex]}")