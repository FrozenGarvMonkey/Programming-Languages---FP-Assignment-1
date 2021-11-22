from functools import reduce

############################################################################################

# Case Study Link: https://uxplanet.org/expenses-management-app-a-ux-case-study-caa01a61dd86
# WHAT DO YOU WANT TO DO WITH THIS
# 1. Print EXPENSES
# 2. Find SPECIFIC EXPENSE 

'''
Functions:

1- Separating functions and data 
2- Assigning a function to a variable 
3- Create a list of functions and use that list 
4- Passing functions as arguments 
5- Returning functions 
6- Mapping 
7- Filtering 
8- Reducing 
9- Lambdas 
10- List Comprehensions 
11- Recursion 

'''
############################################################################################

def print_expenses(expenses):
    
def find_expenses(expenses):

def calc_expenses(expenses):
    

def print_menu():
    
    print("1. Print Expenses\n2. Find Transaction\n3. Calculate Expenses")
    menu_in = int(input("Select Option: "))

    if(menu_in == 1):
        print_expenses()
        
    elif(menu_in == 2):            
        find_expenses()

    elif(menu_in == 3): 
        calc_expenses()

    else: 
        print("\nInvalid Selection!\n")
        print_menu()


