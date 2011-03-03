import string

def words(text):
    for c in string.punctuation:
        text = text.replace(c,"")
    return map(lambda x: x.lower(), text.split())



file = raw_input("What file would you like to sort? ")
strs = {}
text = str(open(file, 'r').read())
for word in words(text):
  if (not strs.has_key(word)):
    strs[word] = 0
  strs[word] += 1
for word in sorted(strs.keys()):
  print word + " : " + str(strs[word])

