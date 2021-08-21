tabby_cat = "\tI'm tabbed in."
persian = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian)
print(backslash_cat)
print(fat_cat)
print("\\\\\\\\\t\n\a\b\f")

while True:
    for i in ["/","-","|","\\","|"]:
        print("%r\r" % i, end="`")