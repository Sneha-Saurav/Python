#Buuble Sort
arr = [45,89,67,12,47]
n = len(arr)
def bubble_sort(arr):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]> arr[j+1]:    
                temp = arr[j]
                arr[j] =arr[j+1]
                arr[j+1] = temp

    return arr

print(bubble_sort(arr))


