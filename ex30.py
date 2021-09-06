# know about if, elseif, and else statements and practice on booleans
people = 30
cars = 40
buses = 150

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")

if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")

if people > buses == people > cars:
    print("wow")

'''
Study drill:
1. elif might be run if the initial if statement is not true. else will be run if all the if statements in the front are false.
'''