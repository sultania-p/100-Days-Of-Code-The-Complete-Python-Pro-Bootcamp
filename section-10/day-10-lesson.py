
## Functions with Output
# def format_name(first_name, last_name):
#     return f"{first_name.title()} {last_name.title()}"
#
# print(format_name("PIYUSH", "sultania"))
#
# ## Function with more than one return values
# def employee_detail(emp_name, emp_department):
#     if emp_name == "" or emp_department == "":
#         return "You must provide valid inputs."
#
#     return f"The employee name is {emp_name} and his/her department is {emp_department}"
#
# print(employee_detail(input("What is the employee name?: "), input("What is the employee department?: ")))

## Coding Exercise --
# def leap_year(year):
#     # if year is divisible by 4 then is leap year EXCEPT century year
#     # Century year divisible by 100 AND 400 both qualify to be leap year
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 # print("Leap year")
#                 return True
#             else:
#                 # print("Not a leap year")
#                 return False
#         # print("Leap year")
#         return True
#     else:
#         # print("Not a leap year")
#         return False
#
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     # check to see if leap year and if month is February return 29
#     if 1 > month or month > 12:
#         return "Invalid month"
#
#     if leap_year(year) and month == 2:
#         return 29
#
#     return month_days[month - 1]
#
# year = int(input("Enter the year: "))
# month = int(input("Enter the month: "))
# days = days_in_month(year, month)
# print(days)

## Docstrings -- Creating documents
def employee_detail(emp_name, emp_department):
    """ This is always at first line after function definition
        Details of function like -- Take first and last name and format it to return the title case version of the name
    """
    if emp_name == "" or emp_department == "":
        return "You must provide valid inputs."

    """
    Its not recommended to use Docstring to write multi-line comment like this..
    """

    return f"The employee name is {emp_name} and his/her department is {emp_department}"

employee_detail('Piyush', 'IT')
