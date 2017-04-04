# Counting Point Mutations - Evolution as a Sequence of Mistakes


# function Hamming distance
def hammingDistance(stringOne, stringTwo):
  res = 0
  j = 0
  stringLen = len(stringOne)
  while j < stringLen:
    if stringOne[j] != stringTwo[j]:
      res = res + 1
    j = j + 1
  return res

inputFile = open('txt/input.txt', 'r')
outputFile = open('txt/output.txt', 'w')

# second variant function
def hamming(s, t):
  return len (filter(lambda pair: pair[0]!=pair[1], zip(list(s),list(t))))

hammingS = ''
hammingT = ''
result = ''
i = 0

for line in inputFile:
  if i == 0:
    hammingS = line.strip()
  else:
    hammingT = line.strip()  
  i = i + 1


outputRes = hammingDistance(hammingS, hammingT)


outputFile.write(str(outputRes))
