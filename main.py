import fire
from datetime import datetime
from model.models import User, Bill, Investment
from configuration.config import session, create_db

class Finntasker_CLI:
    def __init__(self):
        self.session = session

    def init_db(self):
        create_db()

    # In your CLI script (cli.py)
    def add_user(self, username, password):
        user = User(username= username, password= password)
        self.session.add(user)
        self.session.commit()
        print(f'User {username} added successfully.')

    def create_bill(self, username, description, amount, due_date):
        user = session.query(User).filter_by(username=username).first()
        if user:
            due_date = datetime.strptime(due_date, '%Y-%m-%d')
            bill = Bill(description= description, amount= amount, due_date= due_date, user= user)
            self.session.add(bill)
            self.session.commit()
            print(f'Bill of {amount} created successfully for {username}.')
        else:
            print(f'User {username} not found.')

    def manage_investment(self, username, description, amount):
        user = session.query(User).filter_by(username=username).first()
        if user:
            investment = Investment(description=description, amount=amount, user=user)
            self.session.add(investment)
            self.session.commit()
            print(f'Investment managed successfully for {username}.')
        else:
            print(f'User {username} not found')

    def search_users(self, username):
        user = session.query(User).filter_by(username=username).first()
        if user:
            print(f'User Found')
            print(f'Username: {user.username}')
        else:
            print(f'User {username} not found.')

    def search_bills(self, username):
        user = session.query(User).filter_by(username = username).first()
        if user:
            bills = user.bills
            if bills:
                print(f'Bills for {username}')
                for bill in bills:
                    print(f'Description: {bill.description}, Amount: {bill.amount}, Due Date: {bill.due_date}')
            else:
                print(f'No bills found for {username}.')
        else:
            print(f'User {username} not found.')


if __name__ == '__main__':
    fire.Fire(Finntasker_CLI)
