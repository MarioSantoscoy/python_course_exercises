from datetime import datetime, timezone

class BankAccount:
    def __init__(self, first_name, last_name, account_number, balance=0, is_overdraft_allow=False):
        self._first_name = first_name
        self._last_name = last_name
        self._account_number = account_number
        self._balance = balance
        self.is_overdraft_allow = is_overdraft_allow
        self.transactions = []

    @property
    def first_name(self):
        print('Calling First Name...')
        return f'{self._first_name}'

    @property
    def last_name(self):
        print('Calling Last Name...')
        return f'{self._last_name}'

    @property
    def account_number(self):
        print('Calling Account Number...')
        return f'{self._account_number}'

    @property
    def balance(self):
        print('Calling getter Balance...')
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        print('Balance Setter Called...')
        if new_balance < 0:
            raise ValueError('Balance cannot be negative')
        self._balance = new_balance

    def _record_transaction(self, type, amount):
        transaction_record = (
            datetime.strftime(datetime.now(timezone.utc), '%Y-%m-%d %H:%M:%S'),
            type,
            amount,
            self.balance
        )
        self.transactions.append(transaction_record)

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")

        if self.balance < amount and not self.is_overdraft_allow:
            raise ValueError("Insufficient funds.")
        self.balance = self.balance - amount
        self._record_transaction("withdraw", amount)

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")

        self.balance = self.balance + amount

        self._record_transaction("deposit", amount)