# Complementing a Strand of DNA

# function REVC
def REVC(string):
  resultReverseComplement = ''
  i = 0
  reverseComplement = string[::-1]
  for element in reverseComplement:
    if element == 'A':
      resultReverseComplement = resultReverseComplement + 'T'
    elif element == 'T':
      resultReverseComplement = resultReverseComplement + 'A'
    elif element == 'C':
      resultReverseComplement = resultReverseComplement + 'G'
    elif element == 'G':
      resultReverseComplement = resultReverseComplement + 'C'
    i = i + 1
  return resultReverseComplement

inputFile = open('txt/input.txt', 'r')
outputFile = open('txt/output.txt', 'w')

dnaString = ''
result = ''

for line in inputFile:
  dnaString = dnaString + line

result = REVC(dnaString)

outputFile.write(result)