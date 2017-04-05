# Binary Search

io = 0
n = 5
m = 6
sortString = ''
integersList = ''
resString = ''

inputFile = open('txt/input.txt', 'r')
outputFile = open('txt/output.txt', 'w')


for line in inputFile:
  if io == 0:
    n = int(line.strip())
  if io == 1:
    m = int(line.strip())
  if io == 2:
    sortString = line.strip()
  if io == 3:
    integersList = line.strip()
  io = io + 1

sortArr = sortString.split(' ')
i = 0
for n in sortArr:
  sortArr[i] = int(n)
  i = i + 1

integersArr = integersList.split(' ')
i = 0
for n in integersArr:
  integersArr[i] = int(n)
  i = i + 1


def binSearch(arr, x):
  l = 0
  r = len(arr)
  while r - l > 1:
    m = (l + r) // 2 # Целочисленный тип в Python имеет неограниченную длину
    if x < arr[m]:
      r = m
    else:
      l = m
  return l+1 if arr[l] == x else -1 # если элемент не найден, возвращаем -1

i = 0
while i < m:
  promRes = binSearch(sortArr, integersArr[i])
  resString = resString + ' ' + str(promRes)
  i = i + 1


outputFile.write(str(resString))