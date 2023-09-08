# FINNTASKER

## Introduction

`FINNTASKER` is a command-line interface (CLI) based financial management system designed to help individuals manage their personal finances efficiently. The application streamlines tasks such as tracking monthly bills, creating budgets and monitoring investments. It aims to reduce financial stress and enhance proactive financial management.

## Technologies Used

- Python
- SQLAlchemy (for database interaction)
- Alembic (for database migrations)
- Fire (for CLI)

## Installation

### Clone the Repository

```bash
git clone https://github.com/jeffetale/Phase-3-Project.git
cd Phase-3-Project
```
### Dependencies
Before running FINNTASKER, make sure you have the following dependencies installed:

Python (3.10 or higher)
Pipenv (for virtual environment)
To set up the virtual environment, run:
```bash
pipenv install
pipenv shell
```
### Usage
1. Creating a New User
```bash
pipenv run python main.py add_user --username johndoe --password secret
```
This will create a new user with the username johndoe and password secret.

2. Adding Bills
```bash
pipenv run python main.py add_bill --username johndoe --description Rent --amount 1000 --due_date 2023-09-30
```
This will add a bill with description Rent, amount 1000, and due date 2023-09-30 for the user johndoe.

3. Updating Bills or Investments
```bash
pipenv run python main.py update_bill --username johndoe --description Rent --new_amount 6000 --new_due_date 2023-09-30
```
This will update the bill with description Rent for the user johndoe with a new amount of 6000 and a new due date of 2023-09-30.
```bash
pipenv run python main.py update_investment --username johndoe --description Crypto --new_amount 65000 
```
This will update the investment with description Crypto for the user johndoe with a new amount of 65000.

4. Searching for Users, Bills or Investments
```bash
pipenv run python main.py search_user --username johndoe
```
This will search for a user with the username johndoe.
```bash
pipenv run python main.py search_bills --username johndoe
```
This will search for the bills of a user with the username johndoe.
```bash
pipenv run python main.py search_investments --username johndoe
```
This will search for the investments of a user with the username johndoe.

5. Deleting Users, Bills, and Investments
```bash
pipenv run python main.py delete_user --username johndoe
```
Deletes a user together with all their records.

To delete a bill for a user:
```bash
pipenv run python main.py delete_user_bill --username johndoe --description Rent
```
To delete an investment for a user:
```bash
pipenv run python main.py delete_user_investment --username johndoe --description Stocks
```
### Contributing
If you'd like to contribute to FINNTASKER, please follow these steps:

Fork the repository.
Create a new branch for your feature: git checkout -b feature-name.
Make your changes and commit them: git commit -m 'Add some feature'.
Push to your branch: git push origin feature-name.
Submit a pull request.

### Acknowledgements

Jeff Etale - Email[jeff.etale@student.moringaschool.com]
