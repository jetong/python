mySet = set()
file = open("data.txt", "r")
for item in file:
	mySet.add(item.title().strip())

print(mySet)	
