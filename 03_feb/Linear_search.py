# linear Search 
arr = [10,20,30,40, 50]
find = int(input("Enter the no want to search: "))



def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

result = linear_search(arr,find)
if result == -1:
    print("Not Found")

else:
    print("Element found at ", result)
