#Advent of Code Day 2

inputFile = open("Day2Input.txt","r");
input = inputFile.readlines();
inputList = [];
finalResult = 0;

for line in input:
    data_line = line.rstrip().split('\t');
    inputList.append(data_line);

for row in inputList:
	row = [ int(x) for x in row ]

	for x in row:
		i = 0;
		while i < len(row):
			if x % row[i] == 0 and x!= row[i]:
				div = x // row[i];
				finalResult += div;
			i += 1;

print inputList;
print finalResult;