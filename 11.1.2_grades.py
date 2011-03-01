import string

max_points = [25,25,50,25,100]
assignments = ['hw ch 1','hw ch 2','quiz    ','hw ch 3','test']
students = {' #max':max_points}

true = 1
false = 0

def print_menu():
    print "1. Add student"
    print "2. Remove student"
    print "3. Print Grades"
    print "4. Record grade"
    print "5. Save Students' Grades"
    print "6. Load Students' Grades"
    print "7. Print Menu"    
    print "8. Exit"

def print_all_grades():
    print '\t',
    for i in range (len(assignments)):
        print assignments[i],'\t',
    print
    keys = students.keys()
    keys.sort()
    for x in keys:
        print x,'\t',
        grades = students[x]
        print_grades(grades)

def print_grades(grades):
    for i in range(len(grades)):
        print grades[i],'\t\t',
    print

def save_grades(students,filename):
    out_file = open(filename,"w")
    for x in students.keys():
        out_file.write(x+";"+str(students[x])+"\n")
    out_file.close

def load_grades(students,filename):
    in_file = open(filename,"r")
    while true:
        in_line = in_file.readline()
        if in_line == "":
            break
        in_line = in_line[:-1]
        [name,grades_list] = string.split(in_line,";")
        grades = string.split(grades_list, ",")
        grades[0] = grades[0][1:]
        grades[-1] = grades[-1][:-1]
        a = 0
        for x in grades:
            grades[a] = int(grades[a])
            a = a+1
        students[name] = grades
    in_file.close()

print_menu()
menu_choice = 0
while menu_choice !=8:
    print
    menu_choice = input("Menu Choice (1-8):")
    if menu_choice == 1:
        name = raw_input("Student to add:")
        students[name] = [0]*len(max_points)
    elif menu_choice == 2:
        name = raw_input("Student to remove:")
        if students.has_key(name):
            del students[name]
        else:
            print "Student: ",name," not found"
    elif menu_choice == 3:
        print_all_grades()

    elif menu_choice == 4:
        print "Record Grade"
        name = raw_input("Student:")
        if students.has_key(name):
            grades = students[name]
            print "Type in the number of the grade to record"
            print "Type a 0 (zero) to exit"
            for i in range(len(assignments)):
                print i+1,' ',assignments[i],'\t',
            print
            print_grades(grades)
            which = 1234
            while which != -1:
                which = input("Change which Grade:")
                which = which-1
                if 0 <= which < len(grades):
                    grade = input("Grade:")
                    grades[which] = grade
                elif which != -1:
                    print "Invalid Grade Number"
        else:
           print "Student not found"
    elif menu_choice == 5:
        #Finish saving the grades here
        filename = raw_input("Filename to save:")
        save_grades(students,filename)
    elif menu_choice == 6:
        #Finish loading the grades here
        filename = raw_input("Filename to load:")
        load_grades(students,filename)
    elif menu_choice == 8:
        pass
    else:
        print_menu()
