# import stuff
from sys import argv
# set two things that need to be entered in the terminal to run the program
script, input_file = argv
# create a function 
def print_all(f):
    # print the file f
    print(f.read())
# create a function 
def rewind(f):
    # set the reference point to the very first line with the index of 0
    f.seek(0)
# create a function 
def print_a_line(line_count, f):
    # print some text and print what's in the file
    print(line_count, f.readline())
# open the file
current_file = open(input_file)
# print texts
print("First let's print the whole file:\n")
# call the function print_all
print_all(current_file)
# print texts
print("Now let's rewind, kind of like a tape.")
# call the function rewind
rewind(current_file)
# print texts
print("Let's print three lines:")
# Create a variable
# current_line = 1 aka 1st line 
current_line = 1
# call the function print_a_line with the parameter of current line and current file 
print_a_line(current_line, current_file)
# Change the variable with current_line 
# current_line = 2 aka 2nd line
current_line += 1
# call the function print_a_line with the parameter of current line and current file 
print_a_line(current_line, current_file)
# Change the variable with current_line
# current_line = 3 aka 3rd line
current_line += 1
# call the function print_a_line with the parameter of current line and current file 
print_a_line(current_line, current_file)

# seek() means to set the reference point  in this case it sets the reference point to the very first line
# Right argument cheked 