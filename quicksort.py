import random


def QuickSort(arr):
    length = len(arr)
    if(length == 0):
        return []
    elif(length == 1):
        return arr
    pivot = len(arr) // 2
    leftArr = []
    rightArr = []
    for i in range(len(arr)):
        if(i == pivot):
            continue
        else:
            if(arr[i] < arr[pivot]):
                leftArr.append(arr[i])
            else:
                rightArr.append(arr[i])
    return QuickSort(leftArr) + [arr[pivot]] + QuickSort(rightArr)
    
    



unsorted = []
for i in range(10):
    unsorted.insert(min(random.randint(0,10),len(unsorted)),i)
print(unsorted)
sort = QuickSort(unsorted)
print(sort)
