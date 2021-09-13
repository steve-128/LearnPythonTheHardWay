tabby_cat = "\tI'm tabbed in."
persian = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
"""I'll do a list:"""
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

# use ''' ''' instead of """ """ because that way escape sequence is not needed


print("%r" % tabby_cat)
print("%s" % persian)
print(backslash_cat)
print(fat_cat)
print("\\\\\\\\\t\n\a\b\f")

#while True:
#    for i in ["/","-","|","\\","|"]:
#        print("%r\r" % i, end="`")