#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

class ATM:

    def __init__(self, name, pin):
        self.name = name
        self.__pin = pin
        self.file = f"{self.name}_account.txt"
        self.__balance = 0
        self.__transactions = []
        self.load_data()  # Load previous data if exists

    # 🔐 PIN Check
    def check_pin(self):
        attempt = 1
        user_pin = int(input("🔑 Enter Your PIN: "))
        while True:
            if self.__pin == user_pin:
                return True
            else:
                print(f"❌ Incorrect PIN! {3-attempt} attempts left")
                if attempt >= 3:
                    print("🚫 Your Card is Blocked!")
                    return False
                user_pin = int(input("🔑 Enter Your PIN Again: "))
                attempt += 1

    # 💰 Check Balance
    def check_balance(self):
        if self.check_pin():
            print(f"💰 Your Current Balance is Rs.{self.__balance}/-")

    # 💵 Deposit Money
    def deposit(self):
        if self.check_pin():
            amount = int(input("💵 Enter Amount to Deposit: "))
            if amount <= 0:
                print("⚠️ Please Enter a Valid Amount!")
            else:
                self.__balance += amount
                self.__transactions.append(f"Deposited: Rs.{amount}/-")
                self.save_data()
                print(f"✅ Rs.{amount}/- Credited Successfully!")
                print(f"💰 Updated Balance: Rs.{self.__balance}/-")

    # 💸 Withdraw Money
    def withdraw(self):
        if self.check_pin():
            amount = int(input("💸 Enter Amount to Withdraw: "))
            if amount <= 0:
                print("⚠️ Please Enter a Valid Amount!")
            elif amount > self.__balance:
                print("❌ Insufficient Balance!")
            else:
                self.__balance -= amount
                self.__transactions.append(f"Withdrawn: Rs.{amount}/-")
                self.save_data()
                print(f"✅ Rs.{amount}/- Debited Successfully!")
                print(f"💰 Updated Balance: Rs.{self.__balance}/-")

    # 🔄 Change PIN
    def change_pin(self):
        if self.check_pin():
            new_pin = int(input("🔄 Enter New PIN: "))
            confirm_pin = int(input("🔄 Confirm New PIN: "))
            if new_pin == confirm_pin:
                self.__pin = new_pin
                self.save_data()
                print("✅ PIN Changed Successfully!")
            else:
                print("❌ PIN Does Not Match!")

    # 🧾 Mini Statement (Last 5 Transactions)
    def mini_statement(self):
        if self.check_pin():
            print("\n📜 ---- Mini Statement ----")
            if len(self.__transactions) == 0:
                print("No transactions yet.")
            else:
                for t in self.__transactions[-5:]:
                    print("•", t)

    # 💾 Save Data to File
    def save_data(self):
        with open(self.file, "w") as f:
            f.write(str(self.__balance) + "\n")
            f.write(str(self.__pin) + "\n")
            for t in self.__transactions:
                f.write(t + "\n")

    # 📂 Load Data from File
    def load_data(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                lines = f.readlines()
                if len(lines) >= 2:
                    self.__balance = int(lines[0].strip())
                    self.__pin = int(lines[1].strip())
                    self.__transactions = [line.strip() for line in lines[2:]]

    # 🏧 ATM Menu Interface
    def menu(self):
        while True:
            print("\n========== 🏧 ATM MENU ==========")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Mini Statement")
            print("5. Change PIN")
            print("6. Exit")
            print("=================================")

            choice = input("Enter Your Choice: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.mini_statement()
            elif choice == "5":
                self.change_pin()
            elif choice == "6":
                print("🙏 Thank You for Using Our ATM,", self.name)
                break
            else:
                print("⚠️ Invalid Choice! Please Try Again.")


# 🚀 Run ATM System
name = input("👤 Enter Account Holder Name: ")
pin = int(input("🔐 Set Your ATM PIN: "))

user = ATM(name, pin)
print(f"\n🎉 Welcome to Python ATM System, {name}!")
user.menu()


# In[ ]:




