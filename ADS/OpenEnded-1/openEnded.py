numberOfTests = int(input())

def printOutput(elementsList):
    for i in elementsList:
        print(i, end=" ")
    print()
    
for i in range(numberOfTests):
    numberOfElements = int(input())
    elementsList = [int(ele) for ele in input().split()]
    printOutput(sorted(elementsList)[:-2])
