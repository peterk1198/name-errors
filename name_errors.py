# This file checks which names are mismatched between two excel sheets.

import csv
import numpy
from enum import Enum
from sets import Set

class National(Enum):
	first = 3
	last = 5

class Salesforce(Enum):
	first = 0
	last = 1

# reprompts user if invalid file.
def ask():
	while True:
		try:
			class_info = raw_input("""Please enter the file name of the class info 
(For example: boulder_class.csv or boulder_report.csv): """).lower()   
			open(class_info) 
		except IOError:
			print("Invalid file name; try again.")
			continue
		else:
			break
	return class_info


print """



Enter NATIONAL class info."""
nationalCSV = ask()
print """Enter SALESFORCE class info"""
salesforceCSV = ask()


national = []
salesforce = []

with open(nationalCSV) as csvfile:
	readCSV = csv.reader(csvfile, delimiter = ',')
	for row in readCSV:
		if row[0] != "":
			national.append(row[National.first.value] + " " + row[National.last.value])

with open(salesforceCSV) as csvfile:
	readCSV = csv.reader(csvfile, delimiter = ',')
	for row in readCSV:
		 if row[0] != "":
			salesforce.append(row[Salesforce.first.value] + " " + row[Salesforce.last.value])

def Diff(li1, li2):
    return (list(set(li1) - set(li2)))

print "Names that NATIONAL has, that SALESFORCE doesn't."
print(Diff(national, salesforce))
print "Names that SALESFORCE has, that NATIONAL doesn't."
print(Diff(salesforce, national))

print "National has " + str(len(Diff(national, salesforce))) + " unique names."
print "Salesforce has " + str(len(Diff(salesforce, national))) + " unique names."