# \n\n for para 
# \n sentence base chunk 
# words level pe 
# charatcter level pe
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

code = """
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print(f"Current Balance: ₹{self.balance}")


account = BankAccount("Rajesh", 10000)

account.show_balance()
account.deposit(5000)
account.withdraw(3000)
account.show_balance()
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0,
)

chunks = splitter.split_text(code)

print(chunks[0])
print(len(chunks))