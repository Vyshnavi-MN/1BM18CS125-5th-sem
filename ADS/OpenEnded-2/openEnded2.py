class Solution:
    #This is the function uniqueNumbers() which will return the list of unique numbers integers in O(n) - Time-Complexity
    def uniqueNumbers(self, left, right):
        ans = [i for i in range(left,right+1) if len(set(str(i))) == len(str(i))]
        return ans

if __name__ == "__main__":
    testCases = int(input())
    leftRange, rightRange = [int(i) for i in input().split()]
    for num in range(testCases):
        obj = Solution()
        ans = obj.uniqueNumbers(leftRange, rightRange)
        for i in ans: print(i, end = ' ')
        print()
