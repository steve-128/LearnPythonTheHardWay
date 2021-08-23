# assigning an int to the variable cars to represent 100 cars
cars = 100
# 4.0 makes the math operation become an answer with decimals
# If its just 4 then the answer of the math operation will not have decimals
# assigning an floating point to the variable space_in_a_car to represent 4.0 spaces in a car
space_in_a_car = 4.0
# assigning an int to the variable drivers to represent 30 drivers
drivers = 30
# assigning an int to the variable passengers to represent 90 passengers
passengers = 90
# assigning an int to the variable cars_not_driven to represent the difference between the cars and drivers
cars_not_driven = cars - drivers
# assigning an int to the variable cars_driven to represent how many cars are driven by showing the number of drivers
cars_driven = drivers
# assigning a floating point to the variable carpool_capacity to represent the capacity of the carpool by multiplying the cars driven and spaces in a car
carpool_capacity = cars_driven * space_in_a_car
# assigning an int to the variable average_passengers_per_car to represent the average passengers per car with dividing the passenger number by cars driven
average_passengers_per_car = passengers / cars_driven

# the car_pool_capacity is not defined

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")