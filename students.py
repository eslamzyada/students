from finalProjectTask1 import Student
import random


student_list = []
file = open("students.txt","r")
with file as fp:
    for count,line in enumerate(fp):
        student_data = str(line).split("-")
        if len(student_data) == 3:
            student = Student(student_number= int(student_data[0]), student_name= student_data[1], student_class=student_data[2])
            student_list.append(student)
file.close()
print("----------------------------")
print("ID \t\t|name \t\t |class")
for i in student_list:
    print(i.student_number, "\t", i.student_name, "\t\t", i.student_class)
print("-----------------------------")

def find_student(student_number,your_list):
    index = 0
    for i in your_list:
        if i.student_number == student_number:
            return index
        else:
            index += 1
    return -1


def delete_line(file_name, line_number):

    with open(file_name) as file:
        lines = file.readlines()

    if (line_number <= len(lines)):
        del lines[line_number - 1]

        with open(file_name,"w") as file:
            for line in lines:
                file.write(line)
    else:
        print("line",line_number,"is not in file.")
        print("file has", len(lines), "lines.")


while True:
    x = int(input("1.Create Student\n2.Find Student\n3.delete student\n4.Exit"))
    if x == 1:
        student_name = input("Enter Student Name")
        student_class = None
        while True:
            student_class = input("Select Student Class(A-B-C)")
            if student_class in ["A","B","C"]:
                break
        student_1 = Student(student_name, student_class)
        file = open("students.txt", "a")
        student_data = "\n" + str(student_1.student_number) + "-" + student_1.student_name + "-" + student_1.student_class
        file.write(student_data)
        file.close()
        student_list.append(student_1)
    elif x == 2:
        search = int(input("Enter Student Number"))
        index = find_student(search,student_list)
        if index != -1:
            print(student_list[index].student_number,student_list[index].student_name)
        else:
            print("Student not exist")
    elif x == 3:
        delete_file = input("File: ")
        delete_lines = int(input("Line: "))
        delstudent = delete_line(delete_file, delete_lines)
    elif x == 4:
        exit()