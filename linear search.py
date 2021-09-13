import time 

def search(key, arr):
    ans = []
    for i in range(len(arr)):
        if arr[i] == key:
            ans.append(i)
    return ans

arr = []
'''
for i in range(100000000):
    arr.append(i)
'''
arr[2,2,2,3,4,5,6]
now = time.time()
x = search(2, arr)
end = time.time()
print(len(x))
if len(x) == 0:
    print("not in list")
else :
    print(x)

print(end - now)
