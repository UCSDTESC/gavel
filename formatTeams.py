import sys
import csv
import random 

if len(sys.argv) != 4: 
	print("Invalid amount of arguments: Should be maxChar maxInt")
	sys.exit()

maxChar = ord(sys.argv[2])
maxInt = int(sys.argv[3])

unformatted = open(sys.argv[1], "r", encoding="utf8")
formatted = open("sorted.csv", "w", encoding="utf8")

csv_reader = csv.DictReader(unformatted, delimiter=',')

# create array maxChar(maxInt) size randomized 
array = []
for i in range(ord('A'), maxChar + 1):
	for j in range(0, maxInt):
		table = ("%s%i" % (chr(i), j))
		array.append(table)
random.shuffle(array)

# header row in new csv
formatted.write('Team,Table location,DevPos Url,Desired Prizes\n')

x = 0
for lines in csv_reader:
	formatted.write(lines['Submission Title'] + ',')
	formatted.write(array[x] + ',')
	formatted.write(lines['Submission Url'] + ',')
	formatted.write('\"' + lines['Desired Prizes'] + '\"\n')
