import string
import random

crossboard = []
letters = random.choice(string.letters).lower()

word_selection = []
selector = raw_input('Enter your words, comma separated: ')
selector.replace(" ","")
selector.split(",")
word_selection.append(selector)

print word_selection
#for i in range({},{}):
#    crossboard.append({}*{})
