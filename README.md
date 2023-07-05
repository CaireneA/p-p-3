# Personal Expenses Tracker
A Python script that tracks and analyzes personal expenses.

## About
Personal Expenses Tracker is a command line Python application that allows users to keep track of their expenses by entering the amount, category, and date of each expense. The application is also capable of analyzing the expenses over a specified date range and providing insights such as total expenses, daily average, and the categories with the highest and lowest expenses. The application uses Google Sheets as a database to store and retrieve the expense data.

## How To Use
When you run the script, you will be welcomed and presented with three options:

1. **Add an Expense**: The application will prompt you to enter the amount, category, and date of an expense. After entering the details, the expense will be saved in a Google Sheet.

2. **Analyze Expenses**: The application will ask you to enter a start and end date for the analysis. It will then calculate the total expenses within that range, the daily average, and display the categories with the highest and lowest expenses.

3. **Exit**: This option will terminate the application.

## Features

### Existing Features
- **Personalized Data Storage**: The application uses Google Sheets to store expenses, making it easy for users to view and manage their data.
- **Data Validation**: The application validates user input for amount, category, and date to ensure that they are in the correct format.
- **Expense Analysis**: Users can analyze expenses over a given date range to understand their spending habits better.
- **Command Line Interface**: Easy to use command line interface for inputting and analyzing expenses.

### Future Features
- **Budgeting**: Allow users to set budgets for different categories and notify them when they are close to or have exceeded their budget.
- **Visualizations**: Generate charts and graphs to visualize spending trends and category distribution.
- **Export Data**: Allow users to export their expense data in various formats such as CSV, Excel, or PDF.
- **Recurring Expenses**: Add support for automatically tracking recurring expenses such as subscriptions or rent.

## Testing

### Manual Testing
- When an amount is expected, tried entering letters and special characters. The application displayed an error message and asked to try again.
- Entered an incorrect date format. The application validated the date and asked for a valid format (YYYY-MM-DD).
- Analyzed expenses with a start date later than the end date. The application still correctly identified expenses within the range.
- Checked that the total expenses calculation is accurate and that daily average is correct.
- Checked that the category with the highest and lowest expenses is correctly identified.

### Bugs/Updates after Testing
- Ensured that the amount has at most two decimal places.
- Made sure that category input is not empty.
- Added data validation for the date format.

## Deployment
This project is a command-line application and can be run locally. You'll need to have Python installed and set up Google Sheets API credentials.

The steps for deployment are as follows:

1. Clone this repository.
2. Install the required libraries by running `pip install gspread google-auth`.
3. Set up Google Sheets API credentials and save them in a file named 'creds.json'.
4. Create a Google Sheet named 'expenses-tracker' with a worksheet named 'expenses'.
5. Run the script using the command `python <script_name>.py`.

## Credits
- This project uses the [gspread](https://gspread.readthedocs.io/en/latest/) library for interacting with Google Sheets.
- Thank you to all who have provided feedback and suggestions for improving this Personal Expenses Tracker application.
