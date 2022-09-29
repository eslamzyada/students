from finalProject import Course


courses_list = []
file = open("courses.txt","r")
with file as fp:
    for count,line in enumerate(fp):
        course_data = str(line).split("-")
        if len(course_data) == 2:
            course = Course(course_name=course_data[0],course_class=course_data[1])
            courses_list.append(course)
file.close()

print("---------------------")
print("Course number \t\t| Course name \t\t| Course Class")
for i in courses_list:
    print(i.course_number, "\t\t", i.course_name,"\t\t",i.course_class)
print("---------------------")


def find_course(course_number,courses):
    index = 0
    for i in courses:
        if i.course_name == course_number:
            return index
        else:
            index += 1
    return -1


while True:
    choose = int(input("1.Create course\n2.Print courses\n3.Find course\n4.Exit"))
    if choose == 1:
            course_name = input("Enter course name: ")
            course_class = None
            while True:
                course_class = input("select course (A,B,C)")
                if course_class in ["A","B","C"]:
                    break
            course = Course(course_name,course_class)
            file = open("courses.txt","a")
            course_data = "\n"+ str(course.course_number) + "-" + course.course_name + "-" + course.course_class
            file.write(course_data)
            file.close()
            courses_list.append(course)
    elif choose == 2:
        for i in courses_list:
            print(i.course_name,"\t",i.course_class)
    elif choose == 3:
        search = int(input("Enter student number: "))
        index = find_course(search, courses_list)
        if index != -1:
            print("course not exist")
        else:
            print(courses_list[index].course_name, "\t", courses_list[index].course_class)

    elif choose == 4:
        exit()
