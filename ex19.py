# Create a function called cheese_and_crackers with two parameters 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print texts
    print("You have %d cheeses!" % cheese_count)
    # print texts
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    # print texts
    print("Man that's enough for a party!")
    # print texts
    print("Get a blanket.\n")

# print texts
print("We can just give the function numbers directly:")
# Call the function with the parameter of 20 and 30
cheese_and_crackers(20, 30)

# print texts
print("OR, we can use variables from our script:")
# create a variable
amount_of_cheese = 10
# create a variable
amount_of_crackers = 50
# Call the function with the parameter of two variables just created
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# print texts
print("We can even do math inside too:")
# call the function with the parameter of two numbers of 10+20 and 5+6
cheese_and_crackers(10+20, 5+6)
# print texts
print("And we can combine the two, variables and math:")
# call the function witht the parameter of a variable plus 100 and another variable plus 1000
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

def fun(num):
    print(num)

fun(0)
fun(3+2)
fun(4-5)
fun(6*3)
fun(4/3)
no = 2
fun(no)
fun(no+2)
fun(no-2)
fun(no*2)
fun(no/2)