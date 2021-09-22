def sort(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[mini] > arr[j]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]

arr = []
n = int(input("Elements : "))

for i in range(0, n):
    ele = int(input())
    arr.append(ele)
print(arr)
sort(arr)
print(arr)