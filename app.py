from mymodules.models import Student
from mymodules.math_utils import average_grade

class __main__():
    roster = []

    roster.append(Student("Chris", 90))
    roster.append(Student("Kelly", 85))
    roster.append(Student("Tom", 70))
    roster.append(Student("Daniel", 87))
    roster.append(Student("John", 92))
    roster.append(Student("Matthew", 50))
    roster.append(Student("Joanne", 86))
    roster.append(Student("Angela", 75))
    roster.append(Student("Josephine", 57))
    roster.append(Student("William", 88))

    for i in roster:
        i.print_student_info()

    print(f"Average Grade: {average_grade(roster)}")
