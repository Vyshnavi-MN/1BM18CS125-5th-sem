def rodCut(arr, size):
    if size<=0: return 0
    max_val = -1
    for i in range(0, size):
        max_val = max(max_val, arr[i] + rodCut(arr, size-i-1))
    return max_val

print(rodCut([1, 5, 8, 9, 10, 17, 17, 20],8))


