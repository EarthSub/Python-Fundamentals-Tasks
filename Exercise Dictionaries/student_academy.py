# Write a program that keeps the information about students and their grades.

# On the first line, you will receive an integer number representing the next pair of rows.
# On the next lines, you will be receiving each student's name and their grade.

# Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.

# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"

# Format the average grade to the 2nd decimal place.


#           Examples

# Input                   Output

# 5                       John -> 5.00
# John                    Alice -> 4.50
# 5.5                     George -> 5.00
# John
# 4.5
# Alice
# 6
# Alice
# 3
# George
# 5

# 5                       Rob -> 5.50
# Amanda                  Christian -> 5.00
# 3.5                     Robert -> 6.00
# Amanda
# 4
# Rob
# 5.5
# Christian
# 5
# Robert
# 6



number_of_students = int(input())

students_grades = {}

for row in range(number_of_students):
    name = input()
    grade = float(input())
    if name not in students_grades:
        students_grades[name] = name
        students_grades[name] = {"grade": 0.0, "counter": 0}
    students_grades[name]["grade"] += grade
    students_grades[name]["counter"] += 1

for student in students_grades:
    students_grades[student]["grade"] = students_grades[student]["grade"] / students_grades[student]["counter"]
    if students_grades[student]["grade"] >= 4.5:
        print(f"{student} -> {students_grades[student]['grade']:.2f}")
