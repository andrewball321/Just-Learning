import string
true = 1
false = 0


def print_options():
    print "_______DIYS (do it yourself) Dictionary!______"
    print
    print "Enter [a] to look up an English word"
    print "Enter [b] to look up a Spanish word"
    print "Enter [c] to enter new words"
    print "Enter [d] to load words from an existing file"
    print "Enter [e] to save your current dictionary to a file"
    print "Enter [f] to view all saved English words and their translations"
    print "Enter [g] to view all saved Spanish words and their translations"
    print "Enter [h] to review your options"
    print "Enter [q] to quit"

edictionary = {}
sdictionary = {}

def load_dictionarys(ed,sd,filename):
    in_file = open(filename, "r")
    while true:
        in_line = in_file.readline()
        if in_line == "":
            break
        in_line = in_line[:-1]
        [english,spanish] = string.split(in_line,";")
        ed[english] = spanish
        sd[spanish] = english
    in_file.close()

def save_dictionarys(ed,filename):
    out_file = open(filename,"w")
    for x in ed.keys():
        out_file.write(x+";"+ed[x]+"\n")
    out_file.close

def capitalize(firstletter):
    location = ord(firstletter) - ord('a')
    new_ascii = location + ord('A')
    capletter = chr(new_ascii) 
    return capletter

choice = "h"
while choice != "q":
    if choice == "a":
        print "Lookup English Word"
        english = raw_input("English: ")
        e1 = english[0]
        if 'a' <= e1 <= 'z':
            english = capitalize(e1) + english[1:]
        if edictionary.has_key(english):
            print "The Spanish word is",edictionary[english]
        else:
            print "Word not found."
        #Look up English word
    elif choice == "b":
        print "Lookup Spanish Word"
        spanish = raw_input("Spanish: ")
        s1 = spanish[0]
        if 'a' <= s1 <= 'z':
            spanish = capitalize(s1) + spanish[1:]
        if sdictionary.has_key(spanish):
            print "The English word is",sdictionary[spanish]
        else:
            print "Word not found."
        #Look up Spanish word
    elif choice == "c":
        #Enter new words
        english = raw_input("What is your word in English? ")
        spanish = raw_input("What is your word in Spanish? ")
        e1 = english[0]
        s1 = spanish[0]
        if 'a' <= e1 <= 'z':
            english = capitalize(e1) + english[1:]
        if 'a' <= s1 <= 'z':
            spanish = capitalize(s1) + spanish[1:]
        edictionary[english] = spanish
        sdictionary[spanish] = english
    elif choice == "d":
        filename = raw_input("What file would you like to load from? ")
        load_dictionarys(edictionary,sdictionary,filename)
    #load from an existing file
    elif choice == "e":
        filename = raw_input("What would you like to save your file as? ")
        save_dictionarys(edictionary,filename)
        #save current dictionary to file
    elif choice == "f":
        print "English to Spanish"
        elist = edictionary.keys()
        elist.sort()
        for x in elist:
           print "English: ",x," \tSpanish: ",edictionary[x]
        print
       #view all english words and translations
    elif choice == "g":
        #view all spanish words and translations
        print "Spanish to English"
        slist = sdictionary.keys()
        slist.sort()
        for x in slist:
           print "Spanish: ",x," \tEnglish: ",sdictionary[x]
        print
    elif choice != "q":
        print_options()
    choice = raw_input("Option: ")
