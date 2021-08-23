from sys import argv

script, filename = argv

print("We're going to erase %r."%filename)
print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# 'w' means to open and write the file
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# If the file is opened with 'w' mode then truncate has no use because it it basically overwriting the file again
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1+"\n"+line2+ "\n"+line3+ "\n")

print("And finally, we close it.")
target.close()

print("Here's your file %r:" %filename)
txt = open(filename)
print(txt.read())

