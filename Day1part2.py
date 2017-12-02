#Advent of Code 2017 Day 1
inputFile = open("Day1Input.txt","r");
input = inputFile.read();
inputList = [];
finalResult = 0;

for num in input:
	inputList.append(num);

i = 0
while i < len(inputList):
	num = inputList[i];

	secIndex = i - len(inputList)//2;
	
	if inputList[i] == inputList[secIndex]:
		finalResult += int(inputList[i]);

	i += 1;

print "Sum is: {}".format(finalResult);