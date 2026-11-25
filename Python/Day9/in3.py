
class Account:
    def get_interest_rate(self):
        return 4


class SavingsAccount(Account):
    def get_interest_rate(self):
        return 5


class FixedDeposit(Account):
    def get_interest_rate(self):
        return 7


account1 = Account()
account2 = SavingsAccount()
account3 = FixedDeposit()

accounts = [account1, account2, account3]

for account in accounts:
    print("Interest Rate:", account.get_interest_rate(), "%")
