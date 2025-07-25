import json

with open("studentsdb.json","r") as f:
    students= json.load(f)
def save_students():
    with open("studentsdb.json","w") as f:
        json.dump(students,f,indent=4)

def add_std():
    while True:
        id_num = input("Enter student ID: ").lower()
        name = input("Enter student name: ")
        email = input("Enter Email ID: ")
        marks = input("Enter the mark: ")
        if not id_num or not name or not email or not marks:
            print("All fields are required!")
        student = {"id": id_num, "name":name,"email":email,"marks":marks}
        students.append(student)
        save_students()
        print("Student added successfully!")
        return students

def view_std():
    if not students:
        print("No students registered Yet!")
    else:
        for i, student in enumerate(students):
            print(f'{i+1}. {student["id"].capitalize()} | {student["name"]} | {student["email"]} | {student["marks"]}')

def update_std():
    std_id = input("Enter Student ID to update: ").lower()
    for student in students:
        if student['id'] == std_id:
            print(f'{student["email"]} | {student["marks"]}')
            new_email = input("Enter new email: ")
            if new_email == "":
                pass
            else:
                student["email"] = new_email
            new_marks = input("Enter new marks: ")
            if new_marks == "":
                pass
            else:
                student["marks"] = new_marks
        save_students()
        print("Successfully Updated!")     

def del_std():
    view_std()
    found =False
    del_id = input("Enter student ID to Delete: ").lower()
    for i,student in enumerate(students):
        if student["id"] == del_id:
            del students[i]
            save_students()
            print("Deleted Successfully!")
            found =True
            break
    if not found:
        print("No students found!")
            
print()
print("------ Welecome to Student Database ------")
menu = ["Add Student","View Student","Update Info","Delete Student"]
for i,option in enumerate(menu):
    print(f'{i+1}. {option}')
while True:
    option = input("Enter an option(1-4): ")
    try:
        option = int(option)
        if option == 1:
            print("------ Add Students ------")
            add_std()
        elif option == 2:
            print("------ View Students ------")
            view_std()
        elif option == 3:
            print("------ Update Student ------")
            update_std()
        elif option == 4:
            print("------ Delete Student ------")
            del_std()
        elif option == 5:
            print("----------------------- Exit Successfully ------------------------------")
            break
        else:
            print("Enter a valid option")
    except:
        print("Don't enter strings or float!")

