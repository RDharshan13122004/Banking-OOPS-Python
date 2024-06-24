# Banking System in Python using OOP

## Introduction

This project is a simple banking system implemented in Python using Object-Oriented Programming (OOP) concepts. It simulates basic banking operations such as creating accounts, depositing, withdrawing, and checking balances.

## Features

* Create a Bank account
* Depositing money into an account
* Withdraw money from an account
* Transfer money between two accounts
* Check account balance
* Viewing all account detail

## Installation

To run this project, you'll need to have Python installed on your system. You can download Python from the official website.

1. **Clone the repository:**

    https://github.com/RDharshan13122004/Banking-OOPS-Python.git

2. **Navigate to the project directory:**

    cd Banking-OOPS-Python

## Usage

You can run the banking system from the command line. Here's an example of how to use it:

python main.py

## Class Structure

The project is structured into two classes to represent the different entities in the banking system.

1.**user_create Class:**

* Getting the user basic user information

* Acting as super class

2.**BankAccount Class:**

* Represents the bank itself.

* Manages multiple bank accounts.

* Also represents a single bank account.

* Contains methods for depositing, withdrawing, checking the balance,transaction between accounts and view all account detail.

* Represents a bank customer.

* Contains customer details and associated accounts.

## Examples

### 1. Creating a new bank account

    us = BankAccount(name,age,d,phone,addr,Acc,ps,Amount)
    print(us)

### 2. Depositing money

    BankAccount.deposit()

### 3. Withdrawing money

    BankAccount.withdraw()

### 4. Checking balance

    BankAccount.view_account()

### 5. Viewing all account details

    BankAccount.Veiw_all()

### 6. Transaction between accounts

    BankAccount.transaction()

## Dependencies

* csv (comes pre-installed with python)
* re (comes pre-installed with python)
* pandas (install it using pip install pandas)

### Project structure

Banking-oops-python/
├── code.py
├── data.csv
├── main.py
├── README.md

Here's a brief overview of each file and directory:

* **code.py**:Script for setting up the project. It can be used to install the package. Contains the BankAccount class implementation.

* **data.csv**: Contains all account details.

* **main.py**:Contains the main script for running the project.

* **README.md**:Project documentation.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.