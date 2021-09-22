import time
def search(key,arr):
    low = 0
    up = len(arr)-1

    while low<up:
        mid = (int)((up+low)/2)
        if arr[mid] == key:
            return mid 
        elif arr[mid]> key:
            up = mid -1
        else: 
            low = mid+1
    return -1
    

arr = []
#for i in range(100000000):
#    arr.append(i)
arr = [1,2,3,4,5,6,67]
#arr.sort()

if search(2,arr)>=0:
    now = time.time()
    print(search(2,arr))
    end = time.time()
    print(end - now)
else:
    print("n/a")