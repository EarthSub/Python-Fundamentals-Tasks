# You will be receiving names of students, their ID, and a course of programming they have taken in the format
# "{name}:{ID}:{course}". On the last line, you will receive the name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course in the format:
# "{name} - {ID}" on separate lines.

# Note: each student's ID will always be unique


#                         Example
# Input                                           Output

# Peter:123:programming basics                    John - 5622
# John:5622:fundamentals                          Maya - 89
# Maya:89:fundamentals                            Lilly - 633
# Lilly:633:fundamentals
# fundamentals

# Alex:6:programming basics                       Alex - 6
# Maria:7:programming basics                      Maria - 7
# Kaloyan:9:advanced
# Todor:10:fundamentals
# programming_basics



students = []
searching_course = ""

while True:
    student_information = input()
    if ":" not in student_information:
        searching_course =student_information
        break

    student, student_id, course = student_information.split(":")
    students.append({"name": student, "id": student_id, "course": course})

for student in students:
    if searching_course[:5] in student["course"]:
        print(f"{student['name']} - {student['id']}")
