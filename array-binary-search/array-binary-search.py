test1=[[4, 8, 15, 16, 23, 42], 15]
test2=[[-131, -82, 0, 27, 42, 68, 179], 42]
test3=[[11, 22, 33, 44, 55, 66, 77], 90]
test4=[[1, 2, 3, 5, 6, 7], 4]



def binarySearch(arr,key):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1

print(binarySearch(test1[0],test1[1]))
print(binarySearch(test2[0],test2[1]))
print(binarySearch(test3[0],test3[1]))
print(binarySearch(test4[0],test4[1]))

