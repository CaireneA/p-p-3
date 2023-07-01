import gspread
from google.oauth2.service_account import Credentials 

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
    
    # expense details
    amount = input("Enter the amount: $")
    category = input("Enter the category: ").strip().capitalize() # clear white space
    # category = cat.capitalize()
    date = input("Enter the date (YYYY-MM-DD): ")
    
    return [amount, category, date]

result = add_expense()
print(result)