def printOutput(elementsList):
    return sorted(elementsList)[:-2]
    
numberOfTests = int(input())
outputList = []

for i in range(numberOfTests):
    numberOfElements = int(input())
    elementsList = [int(ele) for ele in input().split()]
    outputList.append(printOutput(elementsList))
    
for lst in outputList: print(lst)
