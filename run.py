import gspread
from google.oauth2.service_account import Credentials 
from datetime import datetime
from collections import Counter



SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('expenses-tracker')

expenses = SHEET.worksheet('expenses')

def add_expense():
    """    
    This function asks the user to input the amount, category, and date of an expense.
    
    Returns:
        amount (str): The amount of the expense entered by the user.
        category (str): The category of the expense entered by the user.
        date (str): The date of the expense entered by the user in YYYY-MM-DD format.
    """
    
    print('Welcome to your personal Expenses Tracker')
    
    # Expense details
    amount = input("Enter the amount: $")
    category = input("Enter the category: ").strip().capitalize() # Clear white space and capitalize first letter
    date = input("Enter the date (YYYY-MM-DD): ")
    
    return [amount, category, date]


def validate_input(expense_data):
    """
    Validates the user input for amount, category, and date.
    
    Parameters:
        expense_data (list): A list containing [amount, category, date].
        
    Returns:
        str:  f-string displaying the validated amount, category, and date.
    """
    # Unpack the list into variables
    amount, category, date = expense_data

    # Amount validation
    while True:
        try:
            # Convert amount to float to ensure it's a number
            amount_float = float(amount)
            
            # Ensure amount has at most 2 decimal places
            if '.' in amount and len(amount.split('.')[1]) > 2:
                raise ValueError
                
            break
            
        except ValueError:
            print("Please enter a valid amount.")
            amount = input("Enter the amount: $")

    # Category validation
    while not category:
        print("Category cannot be empty.")
        category = input("Enter the category: ").strip().capitalize()
    
    # Date validation
    while True:
        try:
            # Create a datetime object from the input string to ensure it's valid
            datetime.strptime(date, '%Y-%m-%d')
            break  
            
        except ValueError:
            print("Please enter a valid date in the format YYYY-MM-DD.")
            date = input("Enter the date (YYYY-MM-DD): ")
    
    return [amount, category, date]


def update_worksheet(data, worksheet_name):
    """
    Updates the specified worksheet with the provided data.
    
    Parameters:
        data (list): A list of data to be appended to the worksheet.
        worksheet_name (str): The name of the worksheet to be updated.
    """
    worksheet = SHEET.worksheet(worksheet_name)

    # Calculate ID column value and prepent it to the data list
    next_id = len(worksheet.get_all_values())
    data.insert(0, next_id)

    worksheet.append_row(data)



def get_expenses_in_date_range(start_date, end_date, worksheet):
    """
    Retrieves expenses within a given date range from the worksheet.
    
    Parameters:
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.
        worksheet (gspread Worksheet instance): The worksheet.
        
    Returns:
        list: A list of expenses within the date range.
    """
    # Convert date strings to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    # Get all expenses from the worksheet without the header
    all_expenses = worksheet.get_all_values()[1:]
    
    # Loop through data and filter based on data
    expenses_in_range = []
    for expense in all_expenses:
        expense_date = datetime.strptime(expense[3], '%Y-%m-%d')
        if start_date <= expense_date <= end_date:
            expenses_in_range.append(expense)
            
    return expenses_in_range

def get_date_range_from_user():
    """
    Prompts the user for the start and end dates of a range.
    
    Returns:
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.
    """
    print("Please enter a date range:")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    return start_date, end_date


def calculate_total_expenses(expenses):
    """
    Calculates total expenses for a given list of expenses.
    
    Parameters:
        expenses (list): A list of expenses.
        
    Returns:
        float: The total expenses.
    """
    # Add up the amounts from the expenses list
    return sum(float(expense[1]) for expense in expenses)


def display_total_expenses(total_expenses, start_date, end_date):
    """
    Displays total expenses in a formatted string.
    
    Parameters:
        total_expenses (float): The total expenses.
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.
        
    Returns:
        str: Formatted string displaying the total expenses.
    """
    return f'Total expenses in range from {start_date} to {end_date} is: ${total_expenses:.2f}'


def calculate_daily_average(total_expenses, num_days):
    """
    Calculates the daily average expense.
    
    Parameters:
        total_expenses (float): The total expenses.
        num_days (int): The number of days.
        
    Returns:
        float: The daily average.
    """
    return total_expenses / num_days


def find_category(expenses, find_highest=True):
    """
    Finds the category with the highest or lowest expenses.
    
    Parameters:
        expenses (list): A list of expenses.
        find_highest (bool): If True, find the category with the highest expenses.
                            If False, find the category with the lowest expenses.
        
    Returns:
        list: The category with the highest or lowest expenses and the amount.
    """
    
    categories = Counter()
    
    # Loop through expenses and add expenses to categories
    for expense in expenses:
        category = expense[2]  
        amount = float(expense[1])
        categories[category] += amount
    
    # Get second element of the list
    def custom_key(x):
        return x[1]
    
    if find_highest:
        highest_category = max(categories.items(), key=custom_key)
        return list(highest_category)
    else:
        lowest_category = min(categories.items(), key=custom_key)
        return list(lowest_category)




# expense_data = add_expense()
# validated_data = validate_input(expense_data)
# update_worksheet(validated_data,'expenses')
# print("Data successfully added to the expenses worksheet") 

worksheet_instance = SHEET.worksheet('expenses')
start_date, end_date = get_date_range_from_user()
expenses_in_range = get_expenses_in_date_range(start_date, end_date, worksheet_instance)
total_expenses_in_range = calculate_total_expenses(expenses_in_range)
print(display_total_expenses(total_expenses_in_range, start_date, end_date))

# Convert start_date and end_date to datetime objects for subtraction
start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

# Calculate number of days
num_of_days = (end_date_obj - start_date_obj).days + 1 # +1 to include the end_date

daily_average = calculate_daily_average(total_expenses_in_range, num_of_days)
# print(f"Daily average: ${daily_average:.2f}")

highest_category = find_category(expenses_in_range, find_highest=True)
print(f"Highest category: {highest_category}")

lowest_category = find_category(expenses_in_range, find_highest=False)
print(f"Lowesr category: {lowest_category}")