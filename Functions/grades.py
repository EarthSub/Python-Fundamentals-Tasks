# Write a function that receives a grade between 2.00 and 6.00 and print the corresponding grade in words.
#
# · 2.00 – 2.99 - "Fail"
#
# · 3.00 – 3.49 - "Poor"
#
# · 3.50 – 4.49 - "Good"
#
# · 4.50 – 5.49 - "Very Good"
#
# # · 5.50 – 6.00 - "Excellent"



grade_info = float(input())


def see_grade(points):
    if 2.00 <= points <= 2.99:
        return "Fail"
    elif 3.00 <= points <= 3.49:
        return "Poor"
    elif 3.50 <= points <= 4.49:
        return "Good"
    elif 4.50 <= points <= 5.49:
        return "Very Good"
    elif 5.50 <= points <= 6.00:
        return "Excellent"


print(see_grade(grade_info))
