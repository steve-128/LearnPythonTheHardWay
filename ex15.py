# import argv
from sys import argv
# state that it needs to run from terminal by typing the py file name following a txt name for python the read the file
script = argv
filename = input()
# let txt be the texts in the read file
txt = open(filename)
# print some texts and the entered text file name
print("Here's your file %r:" %filename)
# print the file
print(txt.read())
filename.close()
# print some texts
print("Type the filename again:")
# let file_again be a variable that reads user input and print some text 
file_again = input("> ")
# let txt_again be the texts in the read file
txt_again = open(file_again)
# print the file
print(txt_again.read())
filename.close()
