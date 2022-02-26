class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        ds = int(input("Введите сумму, которую Вы хотите внести:\n"))
        self.balance += ds
        print(f"На счету {self.balance} тг.")

    def withdraw(self):
        ds = int(input("Введите сумму, которую хотите снять:\n"))
        if self.balance < ds:
            print(f"Вы не можете снять сумму {ds} тг.\n Максимально доступно {self.balance} тг.")
        else:
            self.balance -= ds
            print(f"На счету осталось {self.balance} тг.")

    def balance_info(self):
        print(f"Balance= {self.balance} тг")


bank_account = BankAccount("I", 56000)

while True:
    action = input("Press [1] to enrich balance\n"
                   "Press [2] to withdraw\n"
                   "Press [3] to view balance\n"
                   "Press [0] to stop\n")

    if action == "3":
        bank_account.balance_info()
    elif action == "2":
        bank_account.withdraw()
    elif action == "1":
        bank_account.deposit()
    elif action == "0":
        break