# Write a program that keeps the information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name until you receive the command "end".
# You should register each user into the corresponding course. If the given course does not exist, add it.
# When you receive the command "end", print the courses with their names and total registered users. For each course,
# print the registered users.

# Input
# · Until the "end" command is received, you will be receiving input lines in the format:
# "{course_name} : {student_name}"
# · The product data is always delimited by " : "

# Output
# · Print the information about each course in the following format: "{course_name}: {registered_students}"
# · Print the information about each student in the following format: "-- {student_name}"


# Examples

# Input                                                   Output

# Programming Fundamentals : John Smith                   Programming Fundamentals: 2
# Programming Fundamentals : Linda Johnson                -- John Smith
# JS Core : Will Wilson                                   -- Linda Johnson
# Java Advanced : Harrison White                          JS Core: 1
# end                                                     -- Will Wilson
#                                                         Java Advanced: 1
#                                                         -- Harrison White

# Algorithms : Jay Moore                                  Algorithms: 2
# Programming Basics : Martin Taylor                      -- Jay Moore
# Python Fundamentals : John Anderson                     -- Bob Jackson
# Python Fundamentals : Andrew Robinson                   Programming Basics: 1
# Algorithms : Bob Jackson                                -- Martin Taylor
# Python Fundamentals : Clark Lewis                       Python Fundamentals: 3
# end                                                     -- John Anderson
#                                                         -- Andrew Robinson
#                                                         -- Clark Lewis



courses_dictionary = {}


while True:
    course_data = input()
    if course_data == "end":
        break
    course, student_name = course_data.split(" : ")
    if course not in courses_dictionary:
        courses_dictionary[course] = {"number_of_students": 0, "name": []}
    courses_dictionary[course]["number_of_students"] += 1
    courses_dictionary[course]["name"] += [student_name]


for course, data in courses_dictionary.items():
    print(f"{course}: {data['number_of_students']}")
    for names in data['name']:
        print(f"-- {names}")