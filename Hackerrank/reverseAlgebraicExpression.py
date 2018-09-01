def test(expression):
  operations = ['/','*','+','-']
  numbers = []
  tempNum = ''
  opList = []

  for i in expression:
    
    if i not in operations:
      tempNum += i
    elif i in operations:
      opList.append(i)
      numbers.append(tempNum)
      tempNum = ''
    else:
      tempNum += i
  numbers.append(tempNum)

  revNums = numbers[::-1]
  revOpList = opList[::-1]

  output = ''
  for i in range(len(revNums)-1):
    output += revNums[i]
    if revOpList[i]:
      output += revOpList[i]
  
  output += revNums[-1]

  print(expression +'\n'+ output)


test('200*300-43+12')

