def minimumSwaps(arr):
    '''
    [1,3,5,2,4,6,8]
    '''
    swapCount = 0
    for i in range(len(arr)):
        if i == arr[i] - 1:
            continue
        else:
            for j in range(len(arr)):
                if arr[j] == i + 1:
                    swapNum = arr[j]
                    arr[i], arr[j] = arr[j], arr[i]
                    swapCount += 1
    return swapCount
