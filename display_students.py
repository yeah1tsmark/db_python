from main import Student

my_students = Student.select()
for stud in my_students:
    print(stud.student_name, stud.student_id, stud.student_class)

