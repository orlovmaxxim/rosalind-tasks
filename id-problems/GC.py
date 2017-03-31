# Computing GC Content 


inputFile = open('txt/input.txt', 'r')
outputFile = open('txt/output.txt', 'w')

dnaString = ''
nameContent = ''

collection = {}

percentProm = 0
percentHighestResult = 0
nameHighestResult = ''
length = 0

for line in inputFile:
  if line[0] == '>':
    key = line.strip()
    dnaString = ''
  else:
    dnaString = dnaString + line.strip()
    collection[key] = dnaString


for key in collection:
  for element in collection[key]:
    if (element == 'G') | (element == 'C'):
      length = length + 1
  percentProm = (length / len(collection[key])) * 100
  length = 0
  if percentProm > percentHighestResult:
    percentHighestResult = percentProm
    nameHighestResult = key


outputFile.write(nameHighestResult + '\n' + str(percentHighestResult))
