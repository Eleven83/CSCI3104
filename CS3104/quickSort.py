
# Python program for implementation of Quicksort Sort 
  
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    print("Starting partition. low is",low,"and high is",high)
    print("The array is:",arr)
    i = ( low-1 )         # index of smaller element
    print("i equals:",i) 
    pivot = arr[high]     # pivot 
    print ("The pivot is:",pivot)
    for j in range(low , high): 
        print("Comparing",pivot,"with j=",arr[j])
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
            print (arr[j],"is less than or equal to", pivot)
            # increment index of smaller element 
            i = i+1
            print("i is now equal to", i) 
            arr[i],arr[j] = arr[j],arr[i]
            print("Exchanging the values: A[i]=",arr[j],"and A[j]=",arr[i],"are switched to A[i]=",arr[i],"and A[j]=",arr[j])
            print(arr)
    print(arr[i+1],"is now",arr[high])
    arr[i+1],arr[high] = arr[high],arr[i+1]
    print(arr)
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
# Driver code to test above 
arr = [9,7,5,11,12,2,14,3,10,6] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
print(arr)