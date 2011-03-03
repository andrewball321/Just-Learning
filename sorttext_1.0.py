import string

def load_text(filename):
    in_file = open(filename, "r")
    text = str(in_file.read())
    textlist = sorted(text.split())
    return textlist

def list_text(sortedtext):
    prev = sortedtext[0]
    index = sortedtext[0]
    print sortedtext
    textnumb = 1
    for a in range(len(sortedtext)):
        if a == len(sortedtext)-1:
            if prev == index:
                print prev, ": ", textnumb+1
                return
            else:
                print prev, ": ", textnumb
                print index, ": 1"
                return
        elif prev == index:
            if prev != sortedtext[0]:
                textnumb = textnumb + 1
                index = sortedtext[a+1]
            else:
                index = sortedtext[a+1]
        else:
            print prev, ": ", textnumb
            prev = index
            index = sortedtext[a+1]
            textnumb = 1

file = raw_input("What file would you like to sort? ")
load_text(file)
list_text(load_text(file))
