# Bubble sort implimentation

def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

# Bubble Sort Testing

# arr = [1,7,5,3,2,12,563,64]
# print(bubbleSort(arr))


# Selection Sort implimentation

def selectionSort(arr):
    for i in range(len(arr)):
        smallest = i
        temp = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
            
        arr[i] = arr[smallest]
        arr[smallest] = temp
    
    return arr

# Selection sort testing
# arr = [1,7,5,3,2,12,563,64]
# print(selectionSort(arr))

# Insertion sort implimentation
# usefull for times when the list is already almost sorted

def insertionSort(arr):
    for i in range(1, len(arr)):
        currentValue = arr[i]
        currentPosition = i
        while currentPosition > 0 and arr[currentPosition-1] > currentValue:
            arr[currentPosition] = arr[currentPosition-1]
            currentPosition = currentPosition-1
        arr[currentPosition] = currentValue

# Insertion sort Testing 
# arr = [1,7,5,3,2,12,563,64]
# print(selectionSort(arr))


# All above algorithms are O(n^2)
# below are merge sort and quick sort
# they are O(nlogn)

# for merge sort, we need to build a merge function, and then use it within the sort function along
# with some recursion

def merge(arr, left, right, middle):
    left_copy = arr[left:middle + 1]
    right_copy = arr[middle+1:right+1]

    left_index = 0
    right_index = 0
    sorted_index = left

    while left_index < len(left_copy) and right_index < len(right_copy):
        if left_copy[left_index] <= right_copy[right_index]:
            arr[sorted_index] = left_copy[left_index]
            left_index += 1
        else:
            arr[sorted_index] = right_copy[right_index]
            right_index += 1
        
        sorted_index += 1
    
    while left_index < len(left_copy):
        arr[sorted_index] = left_copy[left_index]
        left_index += 1
        sorted_index += 1
    
    while right_index < len(right_copy):
        arr[sorted_index] = right_copy[right_index]
        right_index += 1
        sorted_index += 1

def mergeSort(arr, left_index, right_index):
    if left_index >= right_index:
        return
    middle = (left_index + right_index)//2
    mergeSort(arr, left_index, middle)
    mergeSort(arr, middle+1, right_index)
    merge(arr, left_index, right_index, middle)


# Merge sort Testing 
# arr = [1,7,5,3,2,12,563,64]
# mergeSort(arr, 0 , len(arr)-1)
# print(arr)