def break_words(stuff):
    """This function will break up works for us."""
    words= stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping off."""
    word= words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping off."""
    word=words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words= break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words=break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sort the words then prints the first & last one"""
    words= sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

"""
line 23-24 call the function to get the first word and print 
line 25-26 call the function to get the last word and print
line 27-28 call sorted_words and print out 
line 29 adjust the values of sorted words
line 30-31 call sorted_words and print out 
line 32-end call function and print out things 

>> from ex25 import*
>> word = "ok ok"
>> print_first_word(word)
ok 

>>> & C:/Python39/python.exe c:/Users/ok/LearnPythonTheHardWay/ex25.py
  File "<stdin>", line 1
    & C:/Python39/python.exe c:/Users/ok/LearnPythonTheHardWay/ex25.py
    ^
SyntaxError: invalid syntax
"""



