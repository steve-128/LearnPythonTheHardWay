# learn about while loop
numbers = []

def afunction(a,b):
    i = 0
    while i < a:
        print("At the top i is %d" % i)
        numbers.append(i)
        i = i + b
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

afunction(3,1)

for x in range(0,6):
    print(x)
    numbers.append(x)


print("The numbers: ")

for num in numbers:
    print(num)