from mymodules.models import Student

def average_grade(roster):
    sum_grades = 0
    for i in range(10):
        sum_grades = sum_grades + Student.get_grade(roster[i])

    class_average = sum_grades / 10

    return class_average
