#I'll place my analysis below each line

import string
#imports all of the nifty string functions

def words(text):
    for c in string.punctuation:
        text = text.replace(c,"")
    #This replaces all the punctuation characters with nothing, essentially deleting them
    return map(lambda x: x.lower(), text.split())
    #Not sure how this works exactly (like you said, not worrying about it), but this returns the text split into a list of strings and with everything lowercase


file = raw_input("What file would you like to sort? ")
    #defiles file as the file to sort
strs = {}
    #defines strs as an empty dictionary
text = str(open(file, 'r').read())
    #defines text as all of the text that's in file as one long string.
for word in words(text):
    #for each word in the now split up, non uppercase, non punctuated text (courtesy of words()
  if (not strs.has_key(word)):
    #if the word in text isn't yet in dictionary strs
    strs[word] = 0
    #it creates the word as a key and then sets its associated data(whatever the vocab for that is) to 0
  strs[word] += 1
    #Adds 1 to the value of whatever is associated with that key in dictionary strs
for word in sorted(strs.keys()):
    #For each key in dictionary strs (which are being sorted)
  print word + " : " + str(strs[word])
    #prints the key, then a string of whatever the integer attached to it is. Really doesn't need to be a string for this program unless it goes on to interact with something later. Is that just a hygene choice?

