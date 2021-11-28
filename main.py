from functools import reduce
from datetime import datetime
import json
############################################################################################

# Case Study Link: https://uxplanet.org/expenses-management-app-a-ux-case-study-caa01a61dd86
# Requirements
# 1. Print Expenses
# 2. Find SPECIFIC Expense 
# 3. Calculate Expenses 

'''
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

'''
############################################################################################
expenses = None

def read_data():
    global expenses 
    file_name = input("Enter File Name: ")
    
    try:
        f = open(file_name,)
        expenses = json.load(f)
        
    except ValueError:
        print("\nInvalid File Format!")
        exit()

    except FileNotFoundError:
        print("\nFile does not exist!")
        exit()
        
    f.close()

def sortbyDate():
    try:
        return sorted(expenses, key=lambda x: datetime.strptime(x['date'],"%m/%d/%Y"), reverse=True)
    except ValueError:
        print("Invalid Date Format! Make sure all your data is valid (MM/DD/YYYY).")

def print_expenses(length):
    sorted_exp = sortbyDate()      
    print(json.dumps(sorted_exp[:length], indent=3, ensure_ascii=False))
    
def find_expenses():
    #7,10,6
    print("")

def calc_expenses():
    #2,3,4,5,8
    print("")

def print_menu():
    #11
    print("1. Print Expenses\n2. Find Transaction\n3. Calculate Expenses\n4. Exit")
    menu_in = int(input("Select Option: "))

    if(menu_in == 1):
        lim = -1
        while not (lim>=0 and lim<=len(expenses)):
            lim = int(input("\nNumber of Expenses to print (1-1000): "))
            
        print_expenses(lim)
        
    elif(menu_in == 2):            
        find_expenses()

    elif(menu_in == 3): 
        calc_expenses()

    elif(menu_in == 4):
        exit()

    else: 
        print("\nInvalid Selection!\n")
        print_menu()


def main():
    flag = True
    read_data()
    print_menu()
                

if __name__ == '__main__':
    main()    

