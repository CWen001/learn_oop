from datetime import datetime
from math import e

# Define the date format, for example "YYYY-MM-DD"
date_format = '%Y-%m-%d'
CATEGORIES_dict = {'I': 'income', 'E': 'expense'}


def get_date(prompt="Date (YYYY-MM-DD): ", allow_default=True):
    """
    Prompts the user for a date and returns it as a datetime object.
    If allow_default is True, the user can enter "default" to use the current date.
    """
    date_str = input(prompt)
    
    # 如果输入为空，则返回当前日期
    if allow_default and not date_str:
        date_str = datetime.now().strftime(date_format)
        print(f"Using default date: {date_str}")
        return date_str
    # 如果输入不为空，则检查日期格式是否正确
    else:
        try:
            date_str = datetime.strptime(date_str, date_format).strftime(date_format)
            return date_str
        except ValueError:
            print("Invalid date format. Please use the format YYYY-MM-DD.")
            return get_date(prompt, allow_default)
        
    
def get_amount(prompt="Amount (a number greater than 0): "):
    """
    Prompts the user for an amount and returns it as a float.
    """
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                raise ValueError("Amount cannot be negative. Please enter a positive number.")    
            return amount
        
        except ValueError as e:
            print(e)
            print("Invalid amount. Please enter a number.")   

def get_category(prompt="Category (I for income, E for expense): "):
    """
    Prompts the user for a category and returns it as a string.
    """
    
    while True:
        try:
            category = input(prompt)
            if category in CATEGORIES_dict:
                return CATEGORIES_dict[category]
        
        except ValueError as e:
            print(e)
            print('Input should be I or E. I is for income, E is for expense.')


def get_description(prompt="Insert Your Description: "):
    """
    Prompts the user for a description and returns it as a string.
    """
    description = input(prompt)
    return description

