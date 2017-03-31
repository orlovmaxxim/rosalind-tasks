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

