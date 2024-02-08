#******************************************************************************
# Author:           Bahman Shironi
# Assignment:       Assignment 4 
# Date:             11/25/2023
# Description:      This program calculates employee paychecks for the
#                   current month. program has been modified to have a menu.
#                   Calculation is based on if employees are salary or hourly.
# Revisions:        A01 - initial assignment
#                   A02 - second assignment
#                   A03 - third assignment
#                   A04 - assignment 4
#                   A05 - assignment 5
#******************************************************************************
import myvalid as v 

OVERTIME_RATE = 1.5
OVERTIME_RATE_EXTRA = 0.5
WEEKS_IN_YEAR = 52
WORK_HOURS_IN_WEEK = 40
MONTHS_IN_YEAR = 12

ADD_EMPLOYEE = 1
PRINT_LIST = 2
QUIT_MAIN = 3
IS_SALARY = 1
IS_HOURLY = 2
QUIT_SALARY = 3

def main():
    emp_num = 0
    name = []
    is_salary = []
    salary = [] 
    bonuses = []
    overtime_hours = []
    hourly_rate = []
    hours_worked = []
    paycheck = 0.00 
    choice_main = 0
    choice_salary = 0
    total_pay = 0.00

    print_welcome_message()

    while (choice_main!= QUIT_MAIN):
        print_main_menu()
        choice_main = get_main_choice()

        if (choice_main == ADD_EMPLOYEE):
            emp_num += 1
            name.append(get_name())
            print_is_salary_menu()
            choice_salary = get_salary_choice()

            if choice_salary == IS_SALARY:
                hourly_rate.append(0.00)
                hours_worked.append(0.00) 
                # adding 0 so that the lists stay parallel
                is_salary.append(True)

                print_please_enter()
                salary.append(get_salary())
                bonuses.append(get_bonuses())
                overtime_hours.append(get_overtime_hours())

                paycheck = calc_paycheck(emp_num - 1, is_salary, salary
                         , bonuses, overtime_hours, hourly_rate, hours_worked) 
                print_paycheck_amount(name[emp_num - 1], paycheck)                

            elif choice_salary == IS_HOURLY:
                salary.append(0.00)
                # adding 0 so that the lists stay parallel
                is_salary.append(False)

                print_please_enter()
                hourly_rate.append(get_input_hourly_rate())
                hours_worked.append(get_hours_worked())
                overtime_hours.append(get_overtime_hours())
                bonuses.append(get_bonuses())

                paycheck = calc_paycheck(emp_num - 1, is_salary, salary
                         , bonuses, overtime_hours, hourly_rate, hours_worked) 
                print_paycheck_amount(name[emp_num - 1], paycheck)                

            elif choice_salary == QUIT_SALARY:
                name.pop()
                emp_num -= 1
        
        elif choice_main == PRINT_LIST:
            print_employee_list(name, is_salary, salary, bonuses
                        , overtime_hours, hourly_rate, hours_worked)

    total_pay = calc_total_pay(is_salary, salary, bonuses
                        , overtime_hours, hourly_rate, hours_worked)
    print_total_pay(total_pay)
    print_goodbye()


def print_main_menu():
    """
    Prints the main menu for the user
    :param: none
    :return: none
    """
    print("\n1. Add an employee")
    print("2. Print employee list")
    print("3. Quit\n")


def get_main_choice():
    """
    Prompts and get the menu choice from the user
    :param: none
    :return: choice as integer
    """
    choice = 0
    choice = v.get_integer("Enter menu choice: ")

    while not(1 <= choice and choice <= 3):
        print("\nInvalid choice!")
        choice = v.get_integer("Enter menu choice: ")

    print() #prints an empty line to make output look nicer
    return choice


def get_salary_choice():
    """
    Prompts and get the menu choice from the user
    :param: none
    :return: choice as integer
    """
    choice = 0
    choice = v.get_integer("Enter menu choice: ")

    while not(1 <= choice and choice <= 3):
        print("\nInvalid choice!")
        choice = v.get_integer("Enter menu choice: ")

    print() #prints an empty line to make output look nicer
    return choice


def print_welcome_message():
    """
    Prints the welcome message for the user
    :param: none
    :return: none
    """
    print("\n       **** Welcome to paycheck calculator ****\n")


def print_please_enter():
    """
    Prints the Please enter the following message for the user
    :param: none
    :return: none
    """
    print("\nPlease enter the following:\n")


def get_name():
    """
    Prompts the user for the employee name and returns it
    :param: none
    :return: employee's name as a string
    """
    name = ""
    name = input("Name of the employee: ")

    while name == "":
        print("\nEmployee name connot be empty.")
        name = input("Name of the employee: ")

    print() #prints an empty line to make output look nicer
    return name


def get_salary():
    """
    Prompts the user for employee's annual salary and returns it
    :param: none
    :return: employee's annual salary as a float
    """
    salary = 0.00
    salary = v.get_float("Employee's annual salary: $ ")

    while not(salary >= 0):
        print("\nSalary cannot be negative.")
        salary = v.get_float("Employee's annual salary: $ ")
          
    print() #prints an empty line to make output look nicer
    return salary


def get_bonuses():
    """
    Prompts the user for employee's monthly bonuses and returns it
    :param: none
    :return: employee's monthly bonuses as a float
    """
    bonuses = 0.00
    bonuses = v.get_float("Amount of monthly bonuses: $ ")

    while not(bonuses >= 0):
        print("\nBonuses cannot be negative.")
        bonuses = v.get_float("Amount of monthly bonuses: $ ")

    print() #prints an empty line to make output look nicer
    return bonuses


def get_overtime_hours():
    """
    Prompts the user for overtime hours worked by the employee in the month
    :param: none
    :return: number of overtime hours as a float
    """
    overtime_hours = 0.00
    overtime_hours = v.get_float("Number of overtime hours " 
                                 + "worked by employee this month: ")

    while not(overtime_hours >= 0):
        print("\nOvertime hours cannot be negative.")
        overtime_hours = v.get_float("Number of overtime hours " 
                                 + "worked by employee this month: ")

    print() #prints an empty line to make output look nicer
    return overtime_hours


def print_is_salary_menu():
    """
    Prints the is salary menu for the user
    :param: none
    :return: none
    """
    print("\nIs the employee paid salary or hourly?\n")
    print("1. Salary")
    print("2. Hourly")
    print("3. Discard and go back\n")


def get_input_hourly_rate():
    """
    Prompts the user for the hourly rate of the employee
    :param: none
    :return: hourly_rate as float
    """
    hourly_rate = 0.00
    hourly_rate = v.get_float("Employee's hourly rate: $ ")

    while not(hourly_rate >= 0):
        print("\nHourly rate cannot be negative.")
        hourly_rate = v.get_float("Employee's hourly rate: $ ")

    print() #prints an empty line to make output look nicer
    return hourly_rate


def get_hours_worked():
    """
    Prompts the user for the number of hours employee has worked in the month
    :param: none
    :return: hours_worked as float
    """
    hours_worked = 0.00
    hours_worked = v.get_float("Total number of hours worked by employee "
                               + "this month: ")

    while not(hours_worked >= 0):
        print("\nHours worked cannot be negative.")
        hours_worked = v.get_float("Total number of hours worked by employee "
                               + "this month: ")

    print() #prints an empty line to make output look nicer
    return hours_worked


def Calc_hourly_rate(salary):
    """
    Calculates the hourly rate (hourly pay equivalent of salary)
    of the employee
    :param: salary as float
    :return: hourly_rate as float
    """
    hourly_rate = 0.00
    hourly_rate = salary / WEEKS_IN_YEAR / WORK_HOURS_IN_WEEK
    return hourly_rate


def calc_paycheck_salary(salary, bonuses, overtime_hours):
    """
    Calculate the total paycheck of a salary paid employee for the month
    :param salary: as float
    :param bonuses: as float
    :param overtime_hours: as float
    :return: paycheck as float
    """
    paycheck = 0.00
    hourly_rate = 0.00

    hourly_rate = Calc_hourly_rate(salary)
    paycheck = ( salary / MONTHS_IN_YEAR 
                + overtime_hours * hourly_rate * OVERTIME_RATE 
                + bonuses )
    return paycheck


def calc_paycheck_hourly(hourly_rate, hours_worked, overtime_hours, bonuses):
    """
    calculates the paycheck of an hourly paid employee for the month
    :param hourly_rate: as float
    :param hours_worked: as float
    :param overtime_hours: overtime hours worked in the month as float
    :param bonuses: as float
    :return: paycheck_amount as float
    """
    paycheck = 0.00
    paycheck = (hourly_rate * hours_worked 
                       + overtime_hours * hourly_rate * OVERTIME_RATE_EXTRA 
                       + bonuses)
    return paycheck


def calc_paycheck(index, is_salary, salary, bonuses
                  , overtime_hours, hourly_rate, hours_worked):
    """
    calculates the paycheck of an employee depending if they're hourly or 
    salary
    :param index: index of the employee in the list, as integer
    :param is_salary: says if employee is salary or hourly, list of booleans
    :param salary: salaries of employees, list of floats
    :param bonuses: bonuses of employees, list of floats
    :param overtime_hours: overtime_hours worked by employees, list of floats
    :param hourly_rate: hourly_rate of employees, list of floats
    :param hours_worked: hours_worked by employees, list of floats
    :return: employees paycheck amount as float
    """
    paycheck = 0.00
    if is_salary[index]:
        paycheck = calc_paycheck_salary(salary[index], bonuses[index]
                                        , overtime_hours[index])
    else:
        paycheck = calc_paycheck_hourly(hourly_rate[index]
                    , hours_worked[index], overtime_hours[index]
                    , bonuses[index])

    return paycheck


def print_paycheck_amount(name, paycheck):
    """
    Prints the total peycheck of the employee for the month
    :param name: as string
    :param paycheck: as float
    :return: none
    """
    print(f"\n{name}'s total paycheck amount for this month is "
          + f"$ {paycheck:.2f}\n")
    

def find_max_paycheck(is_salary, salary, bonuses, overtime_hours, hourly_rate
                      , hours_worked):
    """
    finds the employee that has the biggest paycheck and return the index
    :param is_salary: says if employee is salary or hourly, list of booleans
    :param salary: salaries of employees, list of floats
    :param bonuses: bonuses of employees, list of floats
    :param overtime_hours: overtime_hours worked by employees, list of floats
    :param hourly_rate: hourly_rate of employees, list of floats
    :param hours_worked: hours_worked by employees, list of floats
    :return: index of the employee with the biggest paycheck as integer 
    """
    max_paycheck = 0.00
    max_index = 0
    paycheck = 0.00 

    i = 0
    while i < len(is_salary):
        paycheck = calc_paycheck(i, is_salary, salary, bonuses, overtime_hours
                                , hourly_rate, hours_worked) 
        if paycheck > max_paycheck:
            max_index = i
            max_paycheck =  paycheck 
        i += 1
    
    return max_index


def calc_total_pay(is_salary, salary, bonuses, overtime_hours, hoursly_rate
                   , hours_worked):
    """
    calculates the total pay of all employees
    :param is_salary: says if employee is salary or hourly, list of booleans
    :param salary: salaries of employees, list of floats
    :param bonuses: bonuses of employees, list of floats
    :param overtime_hours: overtime_hours worked by employees, list of floats
    :param hourly_rate: hourly_rate of employees, list of floats
    :param hours_worked: hours_worked by employees, list of floats
    :return: total pay of all employees as float
    """
    total_pay = 0.00

    i = 0
    while i < len(is_salary):
        total_pay += calc_paycheck(i, is_salary, salary, bonuses, overtime_hours
                                   , hoursly_rate, hours_worked)
        i += 1
    return total_pay


def print_employee_list(name, is_salary, salary, bonuses, overtime_hours
                        , hourly_rate, hours_worked):
    """
    prints the list of employees, their paycheck and other information based
    on if their salary or hourly
    :param name: names of the employees, list of strings
    :param is_salary: says if employee is salary or hourly, list of booleans
    :param salary: salaries of employees, list of floats
    :param bonuses: bonuses of employees, list of floats
    :param overtime_hours: overtime_hours worked by employees, list of floats
    :param hourly_rate: hourly_rate of employees, list of floats
    :param hours_worked: hours_worked by employees, list of floats
    :return: none
    """
    i = 0
    paycheck = 0.00
    max_index = 0

    if len(is_salary) > 0:
        print('-' * 40)
        print(f'{"Employee list":^40}')
        print('-' * 40)
        print(f'{"Name":<23}{"Paycheck":<20}')
        print('-' * 40)

        while i < len(is_salary):
            paycheck = calc_paycheck(i, is_salary, salary, bonuses, overtime_hours
                                    , hourly_rate, hours_worked)
            print(f'{i + 1}. {name[i]:<20}{paycheck:<20.2f}')

            i += 1

        print('-' * 40)

        max_index = find_max_paycheck(is_salary, salary, bonuses
                            , overtime_hours, hourly_rate, hours_worked) 
        paycheck = calc_paycheck(max_index, is_salary, salary, bonuses, overtime_hours
                            , hourly_rate, hours_worked)
                    
        print('Highest paid employee:')
        print(f'   {name[max_index]:<20}{paycheck:<20.2f}')
        print('-' * 40)

    else:
        print('-' * 40)
        print(f'Employee list is empty!')
        print('-' * 40)


def print_total_pay(total_pay):
    """
    Prints total pay to all employees to the user
    :param total_pay: as float
    :return: none
    """
    print(f"\nTotal pay to all employees this month is $ {total_pay:.2f}\n")


def print_goodbye():
    """
    Prints goodbye message to the user
    :param: none
    :return: none
    """
    print("Thank you for using the Paycheck Calculator!\n")
    

main()