# grading table ni jayden

grading_table = [
    ["Student#", "Student Name", "Q1", "Q2", "Q3", "Quiz Total", "CP", "Final Exam Grade", "Final Grade", "Remarks"],
    [0, "", 0, 0, 0, 0, 0, 0, 0, ""],
    [0, "", 0, 0, 0, 0, 0, 0, 0, ""],
    [0, "", 0, 0, 0, 0, 0, 0, 0, ""],
    [0, "", 0, 0, 0, 0, 0, 0, 0, ""],
]

row_input = [0, 1, 2, 3, 4, 6, 7]
num_rows = len(grading_table)
num_cols = len(grading_table[0])
program_run = True

while program_run:
    for row in range(1, num_rows):
        for col in row_input:
            grading_table[row][col] = input(f"Enter {grading_table[0][col]}: ")
        grading_table[row][5] = (int(grading_table[row][2]) + int(grading_table[row][3]) + int(grading_table[row][4]))
        grading_table[row][8] = int(((int(grading_table[row][7]) * 0.5) + (int(grading_table[row][6]) * 0.1) +
                                      ((int(grading_table[row][5]) * 0.4) / 3)))

        if grading_table[row][8] < 80:
            grading_table[row][9] = "Failed"
        else:
            grading_table[row][9] = "Passed"

    for table_row in grading_table:
        for indiv in table_row:
            print(f"| {str(indiv).center(16)}", end="")
        print("|")

    print("Options:")
    print("1. Delete a student record")
    print("2. Add a student")
    print("3. Replace a student")
    print("4. Replace student info")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        student_number_to_delete = int(input("Enter the student number to delete: "))
        for i in range(1, num_rows):
            if grading_table[i][0] == student_number_to_delete:
                grading_table.pop(i)
                num_rows -= 1
                break
    elif choice == "2":
        new_student_data = [int(input("Enter Student Number: "))]
        for col in range(1, num_cols):
            new_student_data.append(input(f"Enter {grading_table[0][col]}: "))
        grading_table.append(new_student_data)
        num_rows += 1
    elif choice == "3":
        student_number_to_replace = int(input("Enter the student number to replace: "))
        for i in range(1, num_rows):
            if grading_table[i][0] == student_number_to_replace:
                for col in range(1, num_cols):
                    grading_table[i][col] = input(f"Enter new {grading_table[0][col]}: ")
                break
    elif choice == "4":
        student_number_to_replace = int(input("Enter the student number to replace info: "))
        for i in range(1, num_rows):
            if grading_table[i][0] == student_number_to_replace:
                for col in row_input:
                    grading_table[i][col] = input(f"Enter new {grading_table[0][col]}: ")
                grading_table[i][5] = (int(grading_table[i][2]) + int(grading_table[i][3]) + int(grading_table[i][4]))
                grading_table[i][8] = int(((int(grading_table[i][7]) * 0.5) + (int(grading_table[i][6]) * 0.1) +
                                            ((int(grading_table[i][5]) * 0.4) / 3)))
                if grading_table[i][8] < 80:
                    grading_table[i][9] = "Failed"
                else:
                    grading_table[i][9] = "Passed"
                break
    elif choice == "5":
        program_run = False
    else:
        print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")

print("Program exited.")