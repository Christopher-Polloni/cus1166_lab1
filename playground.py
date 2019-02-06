# print("Practicing Basic Program\n")
# print("Hello World") # Display a message
# # Get user input and display a message.
# myname = input("What is your name: ")
# print("Hello " + str(myname))
# # Alternative way to format a string
# print("Hello %s again!" % myname)
# print(f"Hello {myname}!!!! ")
# print("\nFinished Practicing Basic Program\n\n")
#
# print("Practicing Variables\n")
#
# i = 120
# print(f"Variable i has the value {i}")
# f = 1.6180339
# print(f"Variable f has the value {f} and its type is {type(f)}")
# b = True
# print(f"Variable b has the value {b}")
# n = None
# print(f"Variable n has the value of {n}")
# # tuple
# c = (10,20,10)
# print(f" c[0] has the value {c[0]} and is of type: {type(c)}")
# # list
# l = ["Anna", "Tom", "John"]
# l = [10,20,30]
# print(f" l[0] has the value {l[0]} and is of type: {type(l)}")
# print(f"Ouput l[0:2]: {l[0:2]}")
#
# # Sets variables.
# s = set()
# s.add(1)
# s.add(4)
# s.add(6)
# print(s)

# Dictionary
# grades = {"Tom" : "A", "Mark": "B-"}
# grades["Tom"]
# grades["Anna"] = "F"
# grades["Tom"] = "F"
# print(grades["Anna"])
#
# print(f"\n {grades.keys()} \n")
#
# # Create an empty dictionary .
# mydictionary = dict()
# mydictionary["Chris"] = "A"
# mydictionary["Tom"] = 10
# mydictionary["roster"] = grades
#
# print(mydictionary)
# print(mydictionary("Tom"))
#
# print("\nFinished Practicing Variables\n\n")
#
# print("Practicing Conditionals\n")
#
# x=10
# if (x > 0):
#     print("The number x is positive")
# elif (x<0):
#     print("The number x is negative")
# else:
#     print("The number x is zero")
#
# print("\nFinished Practiing Conditionals\n\n")
#
# print("Practicing Loops\n")
#
# for i in range(5):
#     print(i)
# for i_idx, i_value in enumerate(range(2,10)):
#     print(f"{i_idx} - {i_value}" )
#
# print("\nFinished Practicing Loops\n\n")
#
# print("Practicing Functions\n")
#
# def is_even(x):
#     if (x % 2) == 0:
#         return True
#     else:
#         return False
#
# print(is_even(5))
#
# print("\nFinished Practicing Functions\n\n")
#
print("Practicing Classes\n")

class Book:
    def __init__(self, title="Software Engineering", isbn=""):
        self.title = title
        self.isbn = isbn
    def printBook(self):
        print(self.title + ", " + self.isbn)

def main():
    b1 = Book()
    b2 = Book("Introduction to Programming")
    b3 = Book("Introduction to Python", "11111")

    b1.printBook()
    b2.printBook()
    b3.printBook()

if __name__ == "__main__":
    main()

print("\nFinished Practicing Classes\n\n")
#
# print("Practicing Modules\n")
#
# from mymodule.helper_utils import square
# print(square(100))
#
# print("\nFinished Practicing Modules\n\n")
