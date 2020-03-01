# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        print( i)
        num = i
        x = num
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        small = i
        for j in range (i+1, len(arr)):
            if arr[small] > arr[j]:
                small = j
        arr[i], arr[small] = arr[small], arr[i]

        # TO-DO: swap




    return arr  

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    indexing_length = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


print('bs',bubble_sort([4,2,5,8,7]))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr  

