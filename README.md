# Summer Break - Income & Expenses Tracker

## Overview

This project is a simple Flask web service to track income and expenses. It allows users to upload a CSV file of transactions and generate a report summarizing gross revenue, expenses, and net revenue.

## Environment Setup and Running the Code

### Prerequisites

- **Python 3.x** installed on your system.
- Unix-like Environment: **Linux, MacOS, Git Bash**

### Instructions 

1. Navigate to the project directory
2. Run `./setup.sh` to set up virtual environment and install dependencies
3. Start the flask app by running `python app.py`
4. To run tests, run `./test.sh` to send data.csv file to `/transactions` endpoint

## More Info

### Solution and Approach
- CSV Upload: The /transactions endpoint accepts a CSV file with transactions formatted: date, type, amount, memo. The data is validated and stored in memory.
- Report Generation: The /report endpoint calculates and returns a JSON report of gross revenue, expenses, and net revenue by processing the stored transactions.

### Assumptions:
- The CSV file will always contain exactly four columns in the order of: Date, Type, Amount, and Memo.
- Any row that does not follow that format is skipped.
- The Type field contains either "Income" or "Expense."
- The application stores data in memory, meaning the data is lost upon server restart.
- The data only consists of a single individual's/business' transactions. 

### Shortcomings
- No Authentication: There is no user authentication or security implemented, making the service open to any user with access to the endpoints.
- In-Memory Storage: The application does not persist data, meaning data is lost when the server is stopped.
- Limited Validation: The application does minimal validation on the data, assuming the CSV format is correct.

### Future Improvements
- Persistent Storage: Implement a database to store transaction data across sessions.
- Validation: Improve validation for the CSV data: checking for proper formatting, handling of edge cases, verifying data integrity, etc...
- User Authentication: Authentication mechanisms to secure the endpoints, ensuring that only authorized users can upload transactions and generate reports.
- Multi-User: Modify the data handling to support multiple users, instead of only single-user usage.
- Improved Reporting Features: Functionality on things other than just returning gross-revenue, expenses, and net-revenue, such as filtering by date, categorizing expenses by memo, notification of negative net-revenue, or flagging any concerning transactions. 
