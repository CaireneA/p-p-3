import gspread
from google.oauth2.service_account import Credentials 
from datetime import datetime


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
    
    # Cate validation
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


# expense_data = add_expense()
# validated_data = validate_input(expense_data)
# update_worksheet(validated_data,'expenses')
# print("Data successfully added to the expenses worksheet") 

worksheet_instance = SHEET.worksheet('expenses')
expenses_in_range = get_expenses_in_date_range('2023-07-01', '2023-07-03', worksheet_instance)
print(expenses_in_range)
