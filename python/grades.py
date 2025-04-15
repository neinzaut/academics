# Array for User Inputs 
student_number = []
student_name = []
quiz_1 = []
quiz_2 = []
quiz_3 = []
class_participation = []
final_exam = []
quiz_total = 0
grade_total = 0

# User Input 
counter = 1
current_student = 1

while counter <= 2:
    print(f"STUDENT {current_student} INFORMATION")
    input_studentnum = input("Enter Student Number: ")
    student_number.append(input_studentnum)

    input_name = input("Enter Student's Name: ")
    student_name.append(input_name)

    input_firstq = input("Enter Score of First Quiz: ")
    quiz_1.append(input_firstq)

    input_secondq = input("Enter Score of Second Quiz: ")
    quiz_2.append(input_secondq)

    input_thirdq = input("Enter Score of Third Quiz: ")
    quiz_3.append(input_thirdq)

    input_classpar = input("Enter Class Participation: ")
    class_participation.append(input_classpar)

    input_finalexam = input("Enter Score of Final Exam: ")
    final_exam.append(input_finalexam)

    print("\n")
    
    current_student = current_student + 1
    counter = counter + 1

#print(grade_composition)

# Formulas / Conditions
quiz_total = int(len(quiz_1 + quiz_2 + quiz_3)) / 3
grade_total = (int(len(class_participation) * 0.10)) + (quiz_total * 0.40) + (int(len(final_exam)) * 0.50)
if grade_total >= 75:
    remarks = "PASSED"
else:
    remarks = "FAILED"

# Two-dimensional array; for computation of final grade; 10 x 5
grade_composition = [
    ["STUDENT NUMBER", "STUDENT NAME", "QUIZ 1", "QUIZ 2", "QUIZ TOTAL", "CLASS PARTICIPATION", "FINAL EXAM", "TOTAL GRADE", "REMARKS"],
    [student_number, student_name, quiz_1, quiz_2, quiz_3, quiz_total, class_participation, final_exam, grade_total, remarks]
]

print(grade_composition)

# Grade Table
for row in grade_composition:
    for value in row:
       print(f"| {value.center(20)} ")
    #print("| {:^14} | {:^12} | {:^6} | {:^6} | {:^6} | {:^10} | {:^19} | {:^10} | {:^5} | {:^8} |".format(*row))
    #print("|")