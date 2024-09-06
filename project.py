class Student:
  def __init__(self, name:str, age:int, address:str, marks:int) -> None:
    self.name = name 
    self.age = age
    self.address = address
    self.marks = marks


class StudentManagementSys:
  def __init__(self) -> None:
    self.students = []

  def add_student(self):
    try:
      name = str(input("Enter name of the student: "))
    except ValueError:
      print("Name : string \nAge : integer\nAddress : string\nMarks : integer")
      
    try:  
      age = int(input("Enter the age of the student: "))
    except ValueError:
      print("Name : string \nAge : integer\nAddress : string\nMarks : integer")

    try:
      address = str(input("Enter the address of the student: "))
    except ValueError:
      print("Name : string \nAge : integer\nAddress : string\nMarks : integer")

    try:
      marks = int(input("Enter the marks: "))
    except ValueError:
      print("Name : string \nAge : integer\nAddress : string\nMarks : integer")
      
    
    
    
    
    student = Student(name, age, address,marks)
    self.students.append(student)
    print("Student successfully added.")
    return student
    
  def view_students(self):
    if len(self.students) == 0 :
      print("No students found.")
    else:
      view_type = input("All students or one student? (all/one): ")
      if view_type == "all" :
        for student in self.students:
          print(f"Name : {student.name} \nAge : {student.age} \nAddress : {student.address} \nMarks : {student.marks}")
      if view_type == "one":
        for student in self.students :
          name = input("Enter the name of the student you want to view: ")
          if student.name == name :
            print(f"Name : {student.name} \nAge : {student.age} \nAddress : {student.address} \nMarks : {student.marks}")
          else:
            print("Student not found.")
      else:
        print("Invalid choice.")
  def delete_student(self):
    name = input("Enter the name of the student you want to delete: ")
    for student in self.students:
      if student.name == name :
        self.students.remove(student)
      else:
        print("Student not found.")
    print("Student successfully deleted.")
    return self.students
  def update_student(self):
    name = input("Enter the name of the student you want to update: ")
    for student in self.students:
      if student.name == name :
        ip = input(print("What prroperty you want to update? (name/age/address/marks)"))
        try:
          if ip == "name":
            student.name = input("Enter name of the student: ")
          elif ip == "age":
            student.age = int(input("Enter the age of the student: "))
          elif ip == "address":
            student.address = input("Enter the address of the student: ")
          elif ip == "marks":
            student.marks = int(input("Enter the marks: "))
          else :
            print("Invalid property name....")
            break
        except ValueError:
          print("Name : string \nAge : integer\nAddress : string\nMarks : integer")
        except SyntaxError:
          print("Age have to be greater than 0.") 
        except Exception as e:
          print("Something went wrong")

        print("Student successfully updated.")
        return student
    print("Student not found.")


system = StudentManagementSys()
print("Welcome to Student Management System.")

while True:
  print("1. Add a student.")
  print("2. Delete a student.")
  print("3. Update a student.")
  print("4. View student.")
  print("5. Exit the system.")

  choice = input("Enter the number of your choice: ")

  if choice == "1":
    system.add_student()
  elif choice == "2":
    system.delete_student()
  elif choice == "3":
    system.update_student()
  elif choice == "4":
    system.view_students()
  elif choice == "5":
    break
  else:
    print("Invalid choice.")
