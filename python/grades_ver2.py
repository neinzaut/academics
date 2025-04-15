# TUAZON, Francesca Marie A. 
# Grading Table (FINAL VER)

'''
Should have: Create, Read, Update, Delete
VER 2 CHANGES: Array stores info according to student; not per column info

'''

grade_composition = [
    ["STUDENT #", "NAME", "QUIZ 1", "QUIZ 2", "QUIZ 3", "QUIZ TOTAL", "CLASS PAR", "FINAL EXAM", "GRADE", "REMARKS"]
]

def create_table():
    counter = 1 # for while loop
    x = 1 # for studentX 
    current_student = 1 # for f-string formatting

    while counter <= 4:
        arrayName = 'student' + str(x) # Variable to indicate which student's info it is for the list being created
        student_data = []  # Create a new list for each student's data

        print(f"STUDENT {current_student} INFORMATION")

        # Collect Data
        input_studentnum = input("Enter Student Number: ")
        student_data.append(input_studentnum)

        input_name = input("Enter Student's Name: ")
        student_data.append(input_name)

        input_firstq = int(input("Enter Score of First Quiz: "))
        student_data.append(input_firstq)

        input_secondq = int(input("Enter Score of Second Quiz: "))
        student_data.append(input_secondq)

        input_thirdq = int(input("Enter Score of Third Quiz: "))
        student_data.append(input_thirdq)

        # FORMULA: Total for Quizzes 1, 2, and 3
        quiz_total_sum = input_firstq + input_secondq + input_thirdq
        quiz_total = round(quiz_total_sum / 3, 2) # round to 2 decimal places
        student_data.append(quiz_total)

        input_classpar = int(input("Enter Class Participation: ")) 
        student_data.append(input_classpar)

        input_finalexam = int(input("Enter Score of Final Exam: ")) 
        student_data.append(input_finalexam)

        # FORMULA: Compute final grade
        total_grade = round((input_classpar * 0.10) + (quiz_total * 0.40) + (input_finalexam * 0.50), 2)
        student_data.append(total_grade)

        # CONDITION: Remarks
        if total_grade >= 75:
            remarks = "PASSED"
            student_data.append(remarks)
        else:
            remarks = "FAILED"
            student_data.append(remarks)

        print("\n")

        grade_composition.append(student_data)  # Append the student's data to the 2D array

        x = int(x) + 1
        counter = counter + 1
        current_student += 1
    

    Main()

def read_table():
    # Display Grade Table
    for r in grade_composition:
        for value in r:
            print(f"| {str(value).center(11)} ", end="")
        print("|")
    
    Main()

def update_value():
    # Ask the user for the student to update
    update_choice = int(input("Which student's information would you like to update? (Choose between 1-4): "))
    if update_choice >= 1 and update_choice <= len(grade_composition) - 1:
        print(f"STUDENT {update_choice} INFORMATION")
        updated_data = [] 

        input_studentnum = input("Enter Student Number: ")
        updated_data.append(input_studentnum)

        input_name = input("Enter Student's Name: ")
        updated_data.append(input_name)

        input_firstq = int(input("Enter Score of First Quiz: "))
        updated_data.append(input_firstq)

        input_secondq = int(input("Enter Score of Second Quiz: "))
        updated_data.append(input_secondq)

        input_thirdq = int(input("Enter Score of Third Quiz: "))
        updated_data.append(input_thirdq)

        # FORMULA: Total for Quizzes 1, 2, and 3
        quiz_total_sum = input_firstq + input_secondq + input_thirdq
        quiz_total = round(quiz_total_sum / 3, 2) # round to 2 decimal places
        updated_data.append(quiz_total)

        input_classpar = int(input("Enter Class Participation: "))
        updated_data.append(input_classpar)

        input_finalexam = int(input("Enter Score of Final Exam: "))
        updated_data.append(input_finalexam)

        # FORMULA: Compute final grade
        total_grade = round((input_classpar * 0.10) + (quiz_total * 0.40) + (input_finalexam * 0.50), 2) # round to 2 decimal places
        updated_data.append(total_grade)

        # CONDITION: Remarks
        if total_grade >= 75:
            remarks = "PASSED"
            updated_data.append(remarks)
        else:
            remarks = "FAILED"
            updated_data.append(remarks)

        grade_composition[update_choice] = updated_data
    else:
        print("Invalid student choice. No updates made.")

    Main()


def delete():
    print("Please input which option you would like to proceed to.\n\t1: CLEAR ONE (1) STUDENT'S INFORMATION\n\t2: CLEAR ALL STUDENT'S INFORMATION")
    del_choice = int(input("Option chosen: "))

    if del_choice == 1:
        delete_one_input = int(input("Which student's information would you like to delete? (Choose between 1-4): "))
        if delete_one_input >= 1 and delete_one_input <= len(grade_composition) - 1:
            del grade_composition[delete_one_input]
            print(f"Student {delete_one_input} information has been deleted.")
        else:
            print("Invalid input choice. No updates made.")
    elif del_choice == 2:
        # Clear all students' information except the header row
        grade_composition[1:] = []
        print("All students' information has been cleared.")
    else:
        print("Invalid input choice. No updates made.")

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