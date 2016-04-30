f = open('SampleTextFile.txt', "r") #Read txt file
myList = []
for line in f:
	myList.append(line)
print(myList)
f.close()
