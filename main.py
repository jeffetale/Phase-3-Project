import fire
from model.models import User, Bill, Investment
from configuration.config import session, create_db

class Finntasker_CLI:
    def __init__(self):
        self.session = session

    def init_db(self):
        create_db()

if __name__ == '__main__':
    fire.Fire(Finntasker_CLI)
