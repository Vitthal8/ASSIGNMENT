student_marks = {
    "Vitthal": 99,
    "Rahul": 100,
    "Praju": 80,
    "Nobuddy" : 30
}

search_name = input("Enter the student's name: ").title()

if search_name in student_marks:
    print(f"{search_name}'s marks :{student_marks[search_name]}")
else:
    print("Student not found.")