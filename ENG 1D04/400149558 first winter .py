from python import 400149558_Student 

def create_student():
    student_name = input("Enter your student name:   ")
    student_id = input ("Enter your Student id:   ")
    student_units = input(int("Enter total number of units:   "))
    student_points = input(int("Enter total number of points:   "))
    
### assigning a class
    
    new_student = 400149558_Student(student_name, student_id)
    new_student.set_units(student_units)
    new_student.set_points(student_points)
    new_student.calculate_gpa()
    return (new_student)

def display_student_records(arg_student):
    student = arg_student
    print("Student Name: ", student_name, "\n")
    print ("Student ID: ", student_id, "\n")
    print("GPA: ", gpa, "\n")
    
def main():
    student_list = []
    for i in range (5):
        new_student = create_students()
        student_list.append(new_student)
        display_student_record(student_list[i])

student_name = [Cosmo Kramer, Jerry Seinfeld, Elaine Benes, George Costanza, Newmam]
student_number = [400111111, 400222222, 400333333, 400444444, 400555555]
total_units = [37,34,37,40,30]
total_points = [370, 323, 444, 156, 216] 
