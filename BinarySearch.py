# binary Search

def binarySearch(items,key):
    
    low = 0
    high = len(items)-1
    
    while low <= high:
        mid = (low + high)//2
        if key == items[mid]:
            return mid
        elif key < items[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# implementation
items = [1,2,3,4,5,6,7,8,9,10]
print(binarySearch(items,10))