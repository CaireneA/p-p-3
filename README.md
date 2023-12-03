# Personal Expenses Tracker
A Python script that tracks and analyzes personal expenses. Check out the [Live Site](https://personal-expenses-tracker-3ca08c296c82.herokuapp.com/).

## About
Personal Expenses Tracker is a command line Python application that allows users to keep track of their expenses by entering the amount, category, and date of each expense. The application is also capable of analyzing the expenses over a specified date range and providing insights such as total expenses, daily average, and the categories with the highest and lowest expenses. The application uses Google Sheets as a database to store and retrieve the expense data.

## APIs and External Libraries Used
This application makes use of the following APIs and external libraries:
- Google Drive API
- Google Sheets API
- gspread
- google-auth

## How To Use
When you run the script, you will be welcomed and presented with three options:

1. **Add an Expense**: The application will prompt you to enter the amount, category, and date of an expense. After entering the details, the expense will be saved in a Google Sheet.
   
   ![Add Expense](/views/add_expense.png)

2. **Analyze Expenses**: The application will ask you to enter a start and end date for the analysis. It will then calculate the total expenses within that range, the daily average, and display the categories with the highest and lowest expenses.
   
   ![Analyze Expenses](/views/analysis.png)

3. **Exit**: This option will terminate the application.

   ![Exit](/views/exit.png)

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
-------
## Testing

In this section, detailed testing methods are outlined to ensure the robustness and functionality of the Personal Expenses Tracker.

### Manual Testing

#### Add an Expense
- Test Case 1: Input incorrect data type. 
  - Expected Outcome: The program should prompt for valid input.
  - Actual Outcome: The program acted as expected and asked for a valid input.
  - ![Screenshot: Incorrect Data Type for Add Expense](/views/wrong_amount.png)

- Test Case 2: Input correct data.
  - Expected Outcome: The program logs the expense.
  - Actual Outcome: The program acted as expected and logged the expense.
  - ![Screenshot: Correct Data for Add Expense](/views/correct_amount.png)

#### Analyze Expenses
- Test Case 1: Input invalid data.
  - Expected Outcome: The program handles the error and asks for the correct data type.
  - Actual Outcome: The program handled the error as expected. 
  - ![Screenshot: Invalid Data for Analyze Expenses](/views/wrong_date.png)

- Test Case 2: Input valid data.
  - Expected Outcome: The program calculates and displays correct results.
  - Actual Outcome: The program calculated and displayed results as expected.
  - ![Screenshot: Valid Data for Analyze Expenses](/views/correct_date.png)
  - ![Screenshot: Data Verification for Analyze Expenses](/views/data_verif.png)

#### Exit
- Test Case: Attempting to exit the application.
  - Expected Outcome: The application should exit smoothly without errors.
  - Actual Outcome: The application exited as expected.
  - ![Screenshot: Exit Application](/views/correct_exit.png)
  - In cases of invalid input, the program asks for a valid input.
  - ![Screenshot: Invalid Input on Exit](/views/invalid_input.png)

---------
### Testing Site Responsiveness

- The application's responsiveness was tested using [Responsive Design Checker](https://responsivedesignchecker.com/) to ensure proper display and functionality across various devices and screen sizes.

#### Small Screen
- Description: Testing how the site looks on small screen devices like mobile phones.
- ![Screenshot: Small Screen Responsiveness](/views/small_screen.png)

#### Medium Screen
- Description: Testing the site's appearance on medium-sized screens such as tablets.
- ![Screenshot: Medium Screen Responsiveness](/views/med_screen.png)

#### Large Screen
- Description: Testing how the site is displayed on large screens like desktop monitors.
- ![Screenshot: Large Screen Responsiveness](/views/large_screen.png)

### Code Validation

- The application's code was validated to ensure compliance with web standards and to identify any potential issues.

#### HTML Validation
- The HTML code was validated using the [W3C HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpersonal-expenses-tracker-3ca08c296c82.herokuapp.com%2F).
- ![Screenshot: HTML Validation Results](/views/html.png)

#### CSS Validation
- The CSS code was validated using the [W3C CSS Validator](https://validator.w3.org/).
- ![Screenshot: CSS Validation Results](/views/css.png)

#### JavaScript
- No JavaScript was written for this project.

------

### Documentation of Bugs and Their Resolution


#### Bug 1: Amount Input Precision
- **Description**: The application initially accepted amount inputs with more than two decimal places.
- **Resolution**: Updated the application to ensure that the amount input is restricted to at most two decimal places. This was achieved by implementing a validation check on the amount input field.

   ![Screenshot: amount with three decimal points error handling](/views/decimal_amount.png)   

#### Bug 2: Category Input Validation
- **Description**: The application allowed empty inputs for the expense category.
- **Resolution**: Implemented a check to ensure that the category input is not left empty. A validation was added to prompt the user to enter a category if the input was initially left blank.

   ![Screenshot: empty input error handling error handling](/views/empty_input.png) 

#### Bug 3: Date Format Validation
- **Description**: Users were able to enter dates in incorrect formats, leading to potential errors in expense tracking.
- **Resolution**: Added data validation to ensure that users enter the date in the correct format (YYYY-MM-DD). This helped in maintaining consistency and accuracy in date inputs.

   ![Screenshot: Dates fromat validation](/views/dates_format.png) 

### Open Bugs

Currently, there are no known unresolved bugs in the Personal Expenses Tracker. The application has undergone thorough testing, and all identified bugs have been addressed. 


## Deployment
This project is a command-line application and can be run locally. You'll need to have Python installed and set up Google Sheets API credentials.

The steps for deployment are as follows:

1. Clone this repository.
2. Install the required libraries by running `pip install gspread google-auth`.
3. Set up Google Sheets API credentials and save them in a file named 'creds.json'.
4. Create aGoogle Sheet named 'expenses-tracker' with a worksheet named 'expenses'.
5. Run the script using the command `python <script_name>.py`.

## Resources Used
During the development of this project, the following resources were consulted to resolve issues:

- [error:No matching distribution found for python-apt==1.6.4 #5
](https://github.com/jason9693/MusicTransformer-tensorflow2.0/issues/5)
- [Heroku Build returning an error when deploy "backports.zoneinfo"](https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta)
- [IBM Documentation: RegEx](https://www.ibm.com/docs/en/cmofm/9.0.0?topic=SSEPCD_9.0.0/com.ibm.ondemand.mp.doc/arsa0257.html)

## Credits
- Thank you to Code Institute for all the help provided.

