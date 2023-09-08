import fire
from datetime import datetime
from model.models import User, Bill, Investment
from configuration.config import session, create_db

class Finntasker_CLI:
    def __init__(self):
        self.session = session

    def init_db(self):
        create_db()

    def add_user(self, username, password):
        user = User(username= username, password= password)
        self.session.add(user)
        self.session.commit()
        print(f'User {username} added successfully.')

    def add_bill(self, username, description, amount, due_date):
        username = username.lower()
        user = session.query(User).filter_by(username=username).first()
        if user:
            due_date = datetime.strptime(due_date, '%Y-%m-%d')
            bill = Bill(description= description, amount= amount, due_date= due_date, user= user)
            self.session.add(bill)
            self.session.commit()
            print(f'Bill of {amount} created successfully for {username}.')
        else:
            print(f'No username by {username} found.')

    def add_investment(self, username, description, amount):
        username = username.lower()
        user = session.query(User).filter_by(username=username).first()
        if user:
            investment = Investment(description=description, amount=amount, user=user)
            self.session.add(investment)
            self.session.commit()
            print(f'{description} investment added successfully for {username}.')
        else:
            print(f'No username by {username} found.')

    def search_user(self, username):
        username = username.lower()
        user = session.query(User).filter_by(username=username).first()
        if user:
            username = username.lower()
            print(f'User Found')
            print(f'Username: {user.username}')
        else:
            print(f'No username by {username} found.')

    def search_bill(self, username):
        username = username.lower()
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
            print(f'No username by {username} found.')

    def search_investment(self, username):
        username = username.lower()
        user = session.query(User).filter_by(username=username).first()
        if user:
            investments = user.investments
            if investments:
                print(f'Investments for {username}')
                for investment in investments:
                    print(f'Description: {investment.description}, Amount: {investment.amount}')
            else:
                print(f'No investments found for {username}.')
        else:
            print("No username by {username} found.")

    def change_password(self, username, new_password):
        username = username.lower()
        user = session.query(User).filter_by(username=username).first()
        if user:
            user.password = new_password
            self.session.commit()
            print(f'Password for {username} updated successfully.')
        else:
            print('No username by {username} found.')

    def update_bill(self, username, description, new_amount, new_due_date):
        username = username.lower()
        print(f'Lowercased description: {description}')
        user = session.query(User).filter_by(username=username).first()
        if user:
            bill = session.query(Bill).filter(
            Bill.user == user,
            Bill.description.ilike(description)
        ).first()
            if bill:
                new_due_date = datetime.strptime(new_due_date, '%Y-%m-%d')
                bill.amount = new_amount
                bill.due_date = new_due_date
                self.session.commit()
                print(f"{description} bill for {username} updated successfully.")
            else:
                print(f"{description} bill for {username} not found.")
        else:
            print(f"No username by {username} found.")

    def update_investment(self, username, description, new_amount):
        username = username.lower()
        user = session.query(User).filter_by(username=username).first()
        if user:            
            investment = session.query(Investment).filter(
                Investment.user == user,
                Investment.description.ilike(description)).first()
            if investment:
                investment.amount = new_amount
                self.session.commit()
                print(f"The amount for {username}'s {description} investment has been updated successfully.")
            else:
                print(f"No {description} investment for {username} found.")
        else:
            print(f"No username by {username} found.")

    def delete_user(self, username):
        username = username.lower()
        user = session.query(User).filter_by(username=username).first()
        if user:
            self.session.query(Bill).filter_by(user= user).delete()
            self.session.query(Investment).filter_by(user=user).delete()
            self.session.delete(user)
            self.session.commit()
            print(f"{username} and all their records successfully deleted.")
        else:
            print(f"No username by {username} found.")

    def delete_bill(self, username, description):
        username = username.lower()
        user = session.query(User).filter_by(username = username).first()
        if user:
            bill = session.query(Bill).filter(
                    Bill.user == user,
                    Bill.description.ilike(description)).first()
            if bill:
                self.session.delete(bill)
                self.session.commit()
                print(f"{description} bill for {username} has been deleted.")
            else:
                print(f"No {description} bill for {username} found.")
        else:
            print(f"No username by {username} found.")

    def delete_investment(self, username, description):
        username = username.lower()
        user = session.query(User).filter_by(username = username).first()
        if user:
            investment = session.query(Investment).filter(
                Investment.user == user,
                Investment.description.ilike(description)).first()
            if investment:
                self.session.delete(investment)
                self.session.commit()
                print(f"{description} investment for {username} has been deleted.")
            else:
                print(f"No {description} investment for {username} found.")
        else:
            print(f"No username by {username} found.")

if __name__ == '__main__':
    fire.Fire(Finntasker_CLI)
