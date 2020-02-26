import sys
import argparse
import csv
import random 

"""
e.g. 
From original devpost csv 
	Project 1, 22, google.com, taglineOne, 5:00, descriptionOne, [...], "sustainability", [...]
	Project 2, 34, yahoo.com, taglineTwo, 7:57, descriptionTwo, [...], "sustainability, education", [...]
Becomes this in new sorted csv when using `python formatTeams.py A 2 [devpost csv]`
	Project 1, A2, google.com, "sustanability"
	Project 2, A1, yahoo.com, "sustanability, education"
"""

parser = argparse.ArgumentParser(description="Process devpost csv")
parser.add_argument('maxChar', metavar='max char', type=str)
parser.add_argument('maxInt', metavar='max int', type=int)
parser.add_argument('devPost', metavar='devpos csv', type=str)
args = parser.parse_args()

unformatted = open(args.devPost, "r", encoding="utf8")
formatted = open("sorted.csv", "w", encoding="utf8")

csv_reader = csv.DictReader(unformatted, delimiter=',')

# create array maxChar(maxInt) size randomized 
array = []
for i in range(ord('A'), ord(args.maxChar) + 1):
	for j in range(0, args.maxInt):
		table = ("%s%i" % (chr(i), j))
		array.append(table)
random.shuffle(array)

# header row in new csv
formatted.write('Team,Table location,DevPos Url,Desired Prizes\n')

for x, lines in enumerate(csv_reader):
	if x >= len(array) :
		print("Please input a larger maxChar and/or maxInt to fit all teams in csv")
		sys.exit()
	formatted.write(lines['Submission Title'] + ',')
	formatted.write(array[x] + ',')
	formatted.write(lines['Submission Url'] + ',')
	formatted.write('\"' + lines['Desired Prizes'] + '\"\n')