
def basic_pivot(arr):
    return arr[-1]

def middle_pivot(arr):
    return arr[len(arr)//2]

def quicksort_no_in_place(arr, func_pivot=basic_pivot):
    if len(arr) <= 1:
        return arr
    pivot = func_pivot(arr)
    low = []
    equal = []
    high = []

    for ele in arr:
        if (ele<pivot):
            low.append(ele)
        elif (ele==pivot):
            equal.append(ele)
        else:
            high.append(ele)
    return quicksort_no_in_place(low,func_pivot) + equal + quicksort_no_in_place(high,func_pivot)

def partition(arr, low, high):
    # Choose the pivot
    pivot = arr[high]
    
    i = low - 1
    
    # Put smaller elements on left and larger on right
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # swap
    
    # Move pivot after smaller elements and
    # return its position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_in_place(arr,low,high):
    if low < high:
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)

        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)
        
def quicksort(arr,in_place=True,func_pivot=basic_pivot):
    if not in_place:
        arr = quicksort_no_in_place(arr,func_pivot)
    else:
        quick_sort_in_place(arr,0,len(arr)-1)

if __name__=="__main__":
    arr = [10, 80, 30, 90, 40, 50, 70]
    quicksort(arr)
    print("Sorted Array", arr)