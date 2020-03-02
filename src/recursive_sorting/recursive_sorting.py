# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # print(elements)
    # merged_arr = [0] * elements
    i = 0
    j = 0
    len1 = len(arrA)
    len2 = len(arrB)
    print(arrA[2])
    arr = []
    # TO-DO
    while ((i<len1) and (j<len2)):
        if arrA[i] < arrB[j]:
            arr.append(arrA[i])
            i = i + 1
        else:
            arr.append(arrB[j])
            j = j + 1
    
    while(i < len1):
        arr.append(arrA[i])
        i = i + 1

    while(j < len2):
        arr.append(arrB[j])
        j = j + 1
    return arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    print("split",arr)
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i=0
        j=0
        x=0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[x]=left[i]
                i=i+1
            else:
                arr[x]=right[j]
                j=j+1
            x=x+1

        while i < len(left):
            arr[x]=left[i]
            i=i+1
            x=x+1

        while j < len(right):
            arr[x]=right[j]
            j=j+1
            x=x+1
    print("the merge ",arr)
    return arr
arr1 = [ 1, 2, 4, 7]
arr2 = [ 1 , 3, 5]

print('yo',merge_sort([8, 2, 9, 4, 16, 3, 7, 10]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: checx out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
