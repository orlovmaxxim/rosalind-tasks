# Degree array

import collections

inputFile = open('txt/input.txt', 'r')
outputFile = open('txt/output.txt', 'w')

io = 0
arr = []
collectionGraph = collections.Counter()

for line in inputFile:
  if io == 0:
    line = line.split(' ')
    n = int(line[0])
    m = int(line[1].strip())
  else:
    line = line.split(' ')
    arr.append(int(line[0]))
    arr.append(int(line[1].strip()))
  io = io + 1

for elem in arr:
  collectionGraph[elem] += 1

sortedCollection = sorted(collectionGraph.items())
i = 0
res = ''

while i < len(sortedCollection):
  res = res + ' ' + str(sortedCollection[i][1])
  i = i + 1


outputFile.write(str(res))

