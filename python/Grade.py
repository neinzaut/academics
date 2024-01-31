# TUAZON, FRANCESCA MARIE A. (BCS24)
''' Write a Python program that will compute the final grade of a student. Final grade is 30% average of quiz1, quiz2, and quiz3 plus 20% average of project1, project2, and project3 plus 30% of final exam plus 10% of assignment grade plus 10% class standing.'''

# QUIZZES (30%)
quiz1 = int(input("Score of Quiz 1: "))
quiz2 = int(input("Score of Quiz 2: "))
quiz3 = int(input("Score of Quiz 3: "))
quiz_ave = (quiz1 + quiz2 + quiz3)/3

# PROJECTS (20%)
proj1 = int(input("Score of Project 1: "))
proj2 = int(input("Score of Project 2: "))
proj3 = int(input("Score of Project 3: "))
proj_ave = (proj1 + proj2 + proj3)/3

# FINAL EXAM (30%)
final_exam = int(input("Score of Final Exam: "))

# ASSIGNMENT GRADE (10%)
assignment = int(input("Score of Assignment: "))

# CLASS STANDING (10%)
class_standing = int(input("Score of Class Participation: "))

# FORMULA
final_grade = (quiz_ave * 0.30) + (proj_ave * 0.20) + (final_exam * 0.30) + (assignment * 0.10) + (class_standing * 0.10)

print("\n __________________________________________")
print(f"\nBREAKDOWN OF GRADES:\n  Quizzes (30%) = {quiz_ave}\n  Projects (20%) = {proj_ave}\n  Final Exam (30%) = {final_exam}\n  Assignment (10%) = {assignment}\n  Class Standing (10%) = {class_standing}")
print("FINAL GRADE: ",final_grade)