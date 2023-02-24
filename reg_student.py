from main import Student

try:
    st_name = input("Enter your name \n")
    st_id = input("Enter your student id \n")
    st_class = input("Enter your class \n")

    Student.create(student_name=st_name, student_id=st_id, student_class=st_class)
    print("Student Registered Successfully")
except:
    print("Failed to register Student use a different student id")
