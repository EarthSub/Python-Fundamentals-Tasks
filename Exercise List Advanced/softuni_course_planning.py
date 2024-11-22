# Help plan the next Programming Fundamentals course by keeping track of the lessons that will be included in the course
# and all the exercises for the lessons. Before the course starts, there are some changes to be made.

# On the first input line, you will receive the initial schedule of lessons
# and exercises that will be part of the next course, separated by a comma and a space ", ".
# Until you receive the "course start" command, you will be given some commands to modify the course schedule.

# The possible commands are:

# · "Add:{lessonTitle}" - add the lesson to the end of the schedule if it does not exist.
# · "Insert:{lessonTitle}:{index}" - insert the lesson to the given index, if it does not exist.
# · "Remove:{lessonTitle}" - remove the lesson, if it exists.
# · "Swap:{lessonTitle}:{lessonTitle}" - swap the position of the two lessons if they exist.
# · "Exercise:{lessonTitle}" - add Exercise in the schedule right after the lesson index,
# if the lesson exists and there is no exercise already, in the following format "{lessonTitle}-Exercise".
# If the lesson doesn't exist, add the lesson at the end of the course schedule, followed by the Exercise.

# Note: Each time you Swap or Remove a lesson, you should do the same with the Exercises, if there are any following the lessons.

# Input / Constraints

# · On the first line - the initial schedule lessons - strings, separated by comma and space ", ".
# · Until "course start" you will receive commands in the format described above.

# Output

# · Print the whole course schedule, each lesson on a new line with its number (index) in the schedule: "{lesson index}.{lessonTitle}".
# · Allowed working time / memory: 100ms / 16MB.


#                             Examples

# Input                       Output                  Comment

# Data Types, Objects,        1.Arrays                We receive the initial schedule.
# Lists                       2.Data Types            Next, we add the Databases lesson, because it doesn('t exist.'
# Add:Databases               3.Objects               We Insert at the given index lesson Arrays because it(')s not'
# Insert:Arrays:0             4.Databases             present in the schedule.
# Remove:Lists                                        After receiving the last command and removing lesson Lists,
# course start                                        we print the whole schedule.)


# Arrays, Lists,              1.Methods               We swap the given lessons because both exist.
# Methods                     2.Databases             After receiving the Exercise command, we see that such a
# Swap:Arrays:Methods         3.Databases-Exercise    lesson doesn('t exist, so we add the lesson at the end, followed'
# Exercise: Databases         4.Arrays                by the exercise.
# Swap: Lists:Databases       5.Lists                 We swap Lists and Databases lessons, and the
# Insert: Arrays:0                                    Databases-Exercise is also moved after the Databases lesson.
# course start                                        We skip the next command because we already have such a
#                                                     lesson in our schedule.)



initial_schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break
    command_split = command.split(":")
    current_command = command_split[0]
    if current_command == "Add":
        lesson_title = command_split[1]
        if lesson_title not in initial_schedule:
            initial_schedule.append(lesson_title)
    elif current_command == "Insert":
        lesson_title = command_split[1]
        index = command_split[2]
        if lesson_title not in initial_schedule:
            initial_schedule.insert(int(index), lesson_title)
    elif current_command == "Remove":
        lesson_title = command_split[1]
        if lesson_title in initial_schedule:
            initial_schedule.remove(lesson_title)
            exercise_name = f"{lesson_title}-Exercise"
            if exercise_name in initial_schedule:
                initial_schedule.remove(exercise_name)
    elif current_command == "Swap":
        lesson_title1 = command_split[1]
        lesson_title2 = command_split[2]
        exercise_name1 = f"{lesson_title1}-Exercise"
        exercise_name2 = f"{lesson_title2}-Exercise"
        index1 = initial_schedule.index(lesson_title1)
        index2 = initial_schedule.index(lesson_title2)
        if lesson_title1 in initial_schedule and lesson_title2 in initial_schedule:
            initial_schedule[index1], initial_schedule[index2] = initial_schedule[index2], initial_schedule[index1]
        if exercise_name1 in initial_schedule and exercise_name2 in initial_schedule:
            initial_schedule[index1 + 1], initial_schedule[index2 + 1] = initial_schedule[index2 + 1], initial_schedule[
                index1 + 1]
        elif exercise_name1 not in initial_schedule and exercise_name2 in initial_schedule:
            initial_schedule.insert(index1 + 1, initial_schedule.pop(index2 + 1))
        elif exercise_name1 in initial_schedule and exercise_name2 not in initial_schedule:
            initial_schedule.insert(index2 + 1, initial_schedule.pop(index1 + 1))
    elif current_command == "Exercise":
        lesson_title = command_split[1]
        exercise_name = f"{lesson_title}-Exercise"
        if lesson_title in initial_schedule and exercise_name not in initial_schedule:
            index = initial_schedule.index(lesson_title)
            initial_schedule.insert(index + 1, exercise_name)
        elif lesson_title not in initial_schedule:
            initial_schedule.append(lesson_title)
            initial_schedule.append(exercise_name)

for index, lesson in enumerate(initial_schedule):
    print(f"{index + 1}.{lesson}")
