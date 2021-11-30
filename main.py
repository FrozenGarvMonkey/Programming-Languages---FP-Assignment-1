from functools import reduce
from datetime import datetime
import json

############################################################################################

# Case Study Link: https://uxplanet.org/expenses-management-app-a-ux-case-study-caa01a61dd86
# Requirements
# 1. Print Expenses
# 2. Find SPECIFIC Expense
# 3. Calculate Expenses

"""
Functions:

1- Separating functions and data - ✓
2- Assigning a function to a variable - ✓
3- Create a list of functions and use that list ✓
4- Passing functions as arguments ✓
5- Returning functions ✓
6- Mapping ✓ 
7- Filtering ✓
8- Reducing ✓ 
9- Lambdas ✓
10- List Comprehensions ✓
11- Recursion ✓

"""
############################################################################################

expenses = None #Sample Dataset

#Validates an integer input
#1,2
def validate_int(msg):
    while True:
        try:
            intInput = int(input(msg))

        except ValueError:
            print("\nInvalid Input!\n")
            continue
        
        else:
            return intInput

#Read .json file into expenses
def read_data():
    global expenses
    file_name = input("Enter File Name: ")

    try:
        f = open(file_name,)
        expenses = json.load(f)
        f.close()

    except ValueError:
        print("\nInvalid File Format!")
        main()

    except FileNotFoundError:
        print("\nFile does not exist!")
        main()


#Sorts expenses by date and returns a new transformed list
def sort_by_date():
    try:
        return sorted(expenses,key=lambda x: datetime.strptime(x["date"], "%m/%d/%Y"),reverse=True)
    except ValueError:
        print("Invalid Date Format! Make sure all your data is valid (MM/DD/YYYY).")

#Print all expenses
#10
def print_expenses(length):
    print(*['{}'.format(iter) for iter in sort_by_date()[:length]], sep='\n')
    print_menu()


def return_by_id(val):
    try:
        return list(filter(lambda x: x["id"] == int(val), sort_by_date()))
    except ValueError:
        print("Value is not an Integer!")
        print_menu()

#7
def return_by_reference(val):
    return list(filter(lambda x: x["receiver_name"] is not None and x["transaction_reference"].lower() == val, sort_by_date()))

def return_by_receiver_name(val):
    return list(filter(lambda x: x["receiver_name"] is not None and x["receiver_name"].lower() == val, sort_by_date()))

def return_by_expense_type(val):
    return list(filter(lambda x: x["receiver_name"] is not None and x["expense_type"].lower() == val, sort_by_date()))

#3,5
def function_selector(ch):
    categories = [return_by_id,return_by_reference,return_by_receiver_name,return_by_expense_type]
    return categories[ch]

def find_expenses(ch, val):
    sorted_exp = function_selector(ch)(val.lower())
    print(*['{}'.format(iter) for iter in sorted_exp], sep='\n') if sorted_exp else print("Could not find that value!")

#8
def sum_expenses(val):
    return reduce(lambda x,y: x+y, map(lambda x: float(x['amount']), return_by_expense_type(val)))
#6
def return_expenditure():
    categories = ["entertainment","health","academics","accomodation","miscellaneous"]
    return list(zip(categories,map(sum_expenses,categories)))

def calc_expenses():
    print(*['{0} : {1:.2f}'.format(*iter) for iter in return_expenditure()], sep='\n')
    print_menu()

#1,2,11
def print_menu():
    GetInt = validate_int
    print("1. Print Expenses\n2. Find Transaction\n3. Calculate Expenses\n4. Exit")
    menu_in = GetInt("Select Option: ")

    if menu_in == 1:
        lim = -1
        while not (lim >= 0 and lim <= len(expenses)):
            lim = GetInt("Number of Expenses to print (1-1000): ")
        print_expenses(lim)

    elif menu_in == 2:
        ch = -1
        while not (ch >= 0 and ch <= 4):
            ch = GetInt("\n1. Transaction ID\n2. Transaction Reference\n3. Receiver Name\n4. Expense Type\n\nChoose a Category:")
        find_expenses(ch-1, input("\nEnter a value to search for: "))

    elif menu_in == 3:
        calc_expenses()

    elif menu_in == 4:
        exit()

    else:
        print("\nInvalid Selection!\n")
        print_menu()


def main():
    read_data()
    print_menu()


if __name__ == "__main__":
    main()
