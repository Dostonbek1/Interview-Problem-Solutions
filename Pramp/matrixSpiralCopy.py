def spiral_copy(inputMatrix):  
  outputLst = []
  right = len(inputMatrix[0]) -1
  bottom = len(inputMatrix) 
  top = 0
  left = 0
  
  return recursive(outputLst, inputMatrix, right, bottom, top, left)
  

def recursive(outputLst, inputMatrix, right, bottom, top, left):
  
  if bottom >= top:
    for i in range(left,right):
      outputLst.append(inputMatrix[top][i])
    top += 1

  if right >= left:  
    for j in range(top-1,bottom):
      outputLst.append(inputMatrix[j][right])
    right -= 1
    left -= 1

  if bottom > top:
    for k in range(right,left,-1):
      outputLst.append(inputMatrix[bottom-1][k]) # bottom
    bottom -= 1
  
  if right >= left:
    for l in range(bottom-1, top, -1):
      outputLst.append(inputMatrix[l][left])
    left += 1
  if len(outputLst) >= len(inputMatrix[0]) * len(inputMatrix):
    return outputLst
  else:    
    return recursive(outputLst,inputMatrix,right,bottom,top,left)


m = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [10,11,12]
]  
print(spiral_copy(m))
