def rodCutDP(arr, size):
    val , max_val = [0]*(size+1), -1
    if size<=0: return 0
    for i in range(1,size+1):
        for j in range(i):
            max_val = max(max_val, arr[j]+val[i-j-1])
        val[i] = max_val
    return val[size]

print(rodCutDP([1, 5, 8, 9, 10, 17, 17, 20],8))