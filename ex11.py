print("How old are you?", end="")
age = input()
print("How tall are you?", end="")
height = input()
print("How much do you weigh?", end="")
weight = input()

print("So , you're %r old, %r tall, and %r heavy" % (age,height,weight))

print("enter your name: ", end="")
name = input()
print("Hi",name)

# 6'2" single quote needs to be escaped because %r will put the values in single qutation 
# without the \ to escape the ', the string will end right after 6
