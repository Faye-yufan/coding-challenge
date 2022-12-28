# Naxunyn Score
# 说得天花乱坠，本质就是top k sum。  
# 因为当你选出来top k后， top k 的 K个数字 必然在原数组中有个排列  
# 比如 ...k1...k2...k3...k4..k5... ， 你就按从左到右顺序逐个discard左半边就行了  
# （k1不一定比k2大， 仅仅代表在数组中的相对顺序)

def mergeSort(array):
    # Write your code here.
    if len(array) == 1:
        return array
    mid = len(array) // 2
    arr1 = array[: mid]
    arr2 = array[mid:]
    return mergeSortedArray(mergeSort(arr1), mergeSort(arr2))
    

def mergeSortedArray(arr1, arr2):
    array = [None] * (len(arr1) + len(arr2))
    a1_p, a2_p, i = 0, 0, 0
    while a1_p < len(arr1) and a2_p < len(arr2):
        if arr1[a1_p] <= arr2[a2_p]:
            array[i] = arr1[a1_p]
            a1_p += 1
        else:
            array[i] = arr2[a2_p]
            a2_p += 1
        i += 1
    while a1_p < len(arr1):
        array[i] = arr1[a1_p]
        a1_p += 1
        i += 1
    while a2_p < len(arr2):
        array[i] = arr2[a2_p]
        a2_p += 1
        i += 1
    return array
    
    
def maxScore(arr, k):
    arr_sort = mergeSort(arr)
    print(arr_sort[-k:])
    return sum(arr_sort[-k:])