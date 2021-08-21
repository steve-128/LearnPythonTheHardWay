from sys import argv
script, user_name, last = argv
prompt = '- '

print("Hi %s %s, I'm the %s script" % (user_name, last, script))
print("I'd like to ask a few questions.")
print("Do you like me %s %s?" %(user_name, last))
likes = input(prompt)

print("Where do you live %s %s?" %(user_name,last))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
ALright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))