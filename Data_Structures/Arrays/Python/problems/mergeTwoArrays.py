#Given two arrays that are sorted, can you merge them into one and sort them?
# [0,1,3,4,6] and [2,5,7] will become [0,1,2,3,4,5,6,7]

def mergeArrays(arr1, arr2):
    answer = []

    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    while (len(arr1) or len(arr2)):
        if (arr1[0] < arr2[0]):
            answer.append(arr1[0])
            arr1.pop(0)
        elif (arr1[0] > arr2[0]):
            answer.append(arr2[0])
            arr2.pop(0)
        else:
            answer.append(arr1[0])
            answer.append(arr2[0])
            arr1.pop(0)
            arr2.pop(0)

        return [*answer, *arr1, *arr2]


arr1 = [0,3,4]
arr2 = [4,6,30]
arr = mergeArrays(arr1,arr2)
print(arr)
