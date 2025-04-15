/*
Create a simple Grading System. Ask the user to input (using prompt) for Midterm Grade and Final Grade. The program then output (using alert) the Subject Grade, Equivalent and Remarks.

Subject Grade = (Midterm + Finals) divided by 2
Remarks = ""PASSED" grade>=60, otherwise "FAILED"
Equivalent = See the attached image

SAMPLE OUTPUT:
Enter Midterm Grade:  90.00
Enter Final Grade : 96.00
SUBJECT GRADE: 93.00
EQUIVALENT : 3.50
REMARKS: PASSED
*/

let mid_grade = Number(prompt("Enter Midterm Grade: "));
let fin_grade = Number(prompt("Enter Final Grade: "));

let subject_grade = (mid_grade + fin_grade) / 2;
let remarks;

if (subject_grade >= 60) {
    remarks = "PASSED";
} else {
    remarks = "FAILED";
}

let equivalent;

// switch case for equivalent
switch (true) {
    case subject_grade >= 98:
        equivalent = 4.0;
        break;
    case subject_grade >= 95 && subject_grade < 98:
        equivalent = 3.75;
        break;
    case subject_grade >= 92 && subject_grade < 95: 
        equivalent = 3.50;
        break;

    case subject_grade >= 89 && subject_grade < 92: 
        quivalent = 3.25;
        break;
    case subject_grade >= 86 && subject_grade < 89: 
        equivalent = 3.00;
        break;
    case subject_grade >= 83 && subject_grade < 86: 
        equivalent = 2.75;
        break;
    case subject_grade >= 80 && subject_grade < 83: 
        equivalent = 2.50;
        break;
    case subject_grade >= 77 && subject_grade < 80: 
        equivalent = 2.25;
        break;
    case subject_grade >= 74 && subject_grade < 77: 
        equivalent = 2.00;
        break;
    case subject_grade >= 71 && subject_grade < 74: 
        equivalent = 1.75;
        break;
    case subject_grade >= 68 && subject_grade < 71: 
        equivalent = 1.50;
        break;
    case subject_grade >= 64 && subject_grade < 68: 
        equivalent = 1.25;
        break;
    case subject_grade >= 60 && subject_grade < 64: 
        equivalent = 1.00;
        break;
    case subject_grade >= 0 && subject_grade < 60: 
        equivalent = 0.00;
        break;
}

alert("SUBJECT GRADE: " + subject_grade.toFixed(2) + "\nEQUIVALENT: " + equivalent.toFixed(2) + "\nREMARKS: " + remarks);

