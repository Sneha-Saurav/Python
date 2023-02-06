# linear Search 
arr = [10,20,30,40, 50]
find = int(input("Enter the no want to search: "))



def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            print("Found at index " ,i)
    print("Not found") 

linear_search(arr,find)