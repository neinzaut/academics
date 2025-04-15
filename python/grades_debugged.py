'''
Should have: Create, Read, Update, Delete
'''
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
remarks = ""

def create_table():
    counter = 1
    current_student = 1

    # CHANGE COUNTER TO 4 ONCE CODE IS DONE
    while counter <= 2: 
        print(f"STUDENT {current_student} INFORMATION")
        input_studentnum = input("Enter Student Number: ")
        student_number.append(input_studentnum)

        input_name = input("Enter Student's Name: ")
        student_name.append(input_name)

        input_firstq = int(input("Enter Score of First Quiz: "))  # Convert input to int
        quiz_1.append(input_firstq)

        input_secondq = int(input("Enter Score of Second Quiz: "))  # Convert input to int
        quiz_2.append(input_secondq)

        input_thirdq = int(input("Enter Score of Third Quiz: "))  # Convert input to int
        quiz_3.append(input_thirdq)

        input_classpar = int(input("Enter Class Participation: "))  # Convert input to int
        class_participation.append(input_classpar)

        input_finalexam = int(input("Enter Score of Final Exam: "))  # Convert input to int
        final_exam.append(input_finalexam)

        print("\n")

        current_student += 1
        counter += 1

    # Formulas / Conditions
    quiz_total == (sum(quiz_1) + sum(quiz_2) + sum(quiz_3)) / (3 * len(student_number))
    grade_total == (sum(class_participation) * 0.10) + (quiz_total * 0.40) + (sum(final_exam) * 0.50)
    if grade_total >= 75:
        remarks = "PASSED"
    else:
        remarks = "FAILED"
    
    Main()

def read_table():
    # Two-dimensional array; for computation of final grade; 10 x 5
    grade_composition = [
        ["STUDENT #", "STUDENT NAME", "QUIZ 1", "QUIZ 2", "QUIZ 3", "QUIZ TOTAL", "CLASS PAR", "FINAL EXAM", "GRADE", "REMARKS"],
        [str(student_number), str(student_name), str(quiz_1), str(quiz_2), str(quiz_3), str(quiz_total), str(class_participation), str(final_exam), str(grade_total), str(remarks)]
    ]

    # Display Grade Table
    for row in grade_composition:
        for value in row:
            print(f"| {value.center(11)} ", end="")
        print("|")
    
    Main()

def update_value():
    update_choice = input("Which student's information would you like to update? (Type '0' to Go Back): ")
    if update_choice == '1':
        # make new list, will update student 1's array list w new list
        pass
    elif update_choice == '2':
        pass
    elif update_choice == '3':
        pass
    elif update_choice == '4':
        pass
        

    Main()

def delete():
    del_choice = input("")

    Main()

def Main():
    print("\n>> Welcome to the Grade Database! Please input which option you would like to proceed to.\n\t1: CREATE TABLE\n\t2: DISPLAY TABLE\n\t3: UPDATE TABLE\n\t4: DELETE/CLEAR\n\t5: EXIT" )
    choice = input("Option chosen: ")
    print("\n")

    if choice == '1':
        create_table()
    elif choice == '2':
        read_table()
    elif choice == '3':
        update_value()
    elif choice == '4':
        delete()
    elif choice == '5':
        pass
    else:
        print("Please double-check the input value.")
        return
    

Main()
