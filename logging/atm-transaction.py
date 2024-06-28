import logging
import random
import sys

# Setup logging configuration
formatter = logging.Formatter('%(asctime)s - %(message)s')
file_handler = logging.FileHandler('formatted.log')
stream_handler = logging.StreamHandler(sys.stdout)
logger = logging.getLogger(__name__)
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

class BankAccount:
    def __init__(self):
        self.balance = 100.0
        self.correct_pin = 1234
        logger.info("Hello! Welcome to the ATM Depot!")  # Log welcome message

    def authenticate(self) -> None:
        # Authenticate user by asking for PIN
        pin = int(input("\nEnter account pin: "))
        while pin != self.correct_pin:
            logger.error("Invalid pin.")  # Log invalid PIN attempt
            pin = int(input("\nTry again: "))
        logger.info("Authentication successful.")  # Log successful authentication

    def deposit(self) -> None:
        try:
            amount = float(input("Enter amount to be deposited: "))
            if amount < 0:
                logger.warning("Negative amount entered for deposit.")  # Log negative deposit attempt
                return
            self.balance += amount
            self._log_transaction("Amount Deposited", amount, "Successful")  # Log successful deposit
        except ValueError:
            logger.error("Non-numeric value entered for deposit.")  # Log non-numeric deposit attempt
            self._log_transaction("Amount Deposited", None, "Failed")  # Log failed deposit

    def withdraw(self) -> None:
        try:
            amount = float(input("Enter amount to be withdrawn: "))
            if amount < 0:
                logger.warning("Negative amount entered for withdrawal.")  # Log negative withdrawal attempt
                return
            if self.balance >= amount:
                self.balance -= amount
                self._log_transaction("Amount Withdrawn", amount, "Successful")  # Log successful withdrawal
            else:
                logger.error("Insufficient balance for withdrawal.")  # Log insufficient balance
                self._log_transaction("Amount Withdrawn", amount, "Failed")  # Log failed withdrawal
        except ValueError:
            logger.error("Non-numeric value entered for withdrawal.")  # Log non-numeric withdrawal attempt
            self._log_transaction("Amount Withdrawn", None, "Failed")  # Log failed withdrawal

    def display(self) -> None:
        logger.info(f"Available Balance = {self.balance}")  # Log current balance

    def _log_transaction(self, transaction_type: str, amount: float, status: str) -> None:
        # Log detailed transaction information
        logger.info(f"{transaction_type}: {amount if amount is not None else 'N/A'}")
        logger.info("Transaction Info:")
        logger.info(f"Status: {status}")
        logger.info(f"Transaction #{random.randint(10000, 1000000)}")

def main():
    acct = BankAccount()
    acct.authenticate()
    acct.deposit()
    acct.withdraw()
    acct.display()

if __name__ == "__main__":
    main()
