from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

one, two, three = argv
print("one: " , one)
print("two: " , two)
print("three: " , three)

single = argv
print("one argv: ", single)

# It expects to have a file name along with 3 other variables