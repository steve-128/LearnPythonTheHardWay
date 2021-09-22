def sort(arr):
    swap = True
    while swap:
        swap = False
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            x= arr[i]
            arr[i] = arr[i+1]
            arr[i+1]=x
            swap = True

arr = []
n = int(input("Elements : "))

for i in range(0, n):
    ele = int(input())
    arr.append(ele)

print(arr)

sort(arr)

print(arr)
