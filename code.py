import csv
import re
import pandas as pd

class user_create:
    def __init__(self,name:str,age:int,dob:str,phone:str,address:str):
        if not name or not dob or not address:
            raise ValueError("missing values")
        
        assert re.fullmatch(r'[6-9][0-9]{9}$',phone),"the phone number should be 10 values"
        
        assert age >= 18 ,"the age should be above 18 or equal to 18"  

        self.name = name
        self.age = age
        self.dob = dob
        self.phone = phone
        self.addr = address


class BankAccount(user_create):

    def __init__(self,name,age,dob,phone,address,accno: int,password:int,balance :float = 0):
        super().__init__(name,age,dob,phone,address)
        
        exe:bool = False
        ex:bool = False

        assert re.search(r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$",dob),"enter the date of birth properly"
    
        assert re.fullmatch(r"^[0-9]{8}$",str(accno)),"the character of the account is less than 8 or more than 8 it should be equal to 8 character"

        assert re.fullmatch(r"^[0-9]{4}$",str(password)),"the password should have 4 integer character"

        assert balance >= 0, f"the balance should not be in negative"

        self.accno = accno
        self.balance = balance
        self.password = password

        with open("data.csv") as f:
            reader = csv.DictReader(f,fieldnames=["name","age","dob","phone","address","account_no","password","balance"])
            for row in reader:
                if str(self.accno) in row["account_no"] :
                    exe = True

                if str(self.phone) in row["phone"]:
                    ex = True
                
        
        if exe == True:
            print(f"{self.accno} is already exists please re-enter the account number ")

            
        elif ex == True:
            print(f"{self.phone} is already exists with another account kindly check")
    
        else:
            print(f"the account is successfully opened in the bank")
            
            with open("data.csv","a") as f:
                write = csv.DictWriter(f,fieldnames=["name","age","dob","phone","address","account_no","password","balance"])
                write.writerow({"name":self.name,"age":self.age,"dob":self.dob,"phone":self.phone,"address":self.addr,"account_no":self.accno,"password":self.password,"balance":self.balance})
        

    def __str__(self):
        return f"NAME: {self.name.capitalize()} \nAGE:{self.age} \nDOB:{self.dob} \nPHONE: {self.phone} \nADDRESS:{self.addr}\nACC_NO: {self.accno}\nbalance :{self.balance}"
    
    @classmethod
    def deposit(cls):
        dep_acc_no = input("enter the Account number to deposit:").strip() 
        dep_password = int(input("enter the password:"))
        deposit_amount = float(input("enter the amount to deposit:"))

        try:
            assert re.fullmatch(r"^[0-9]{8}$",dep_acc_no)
        except AssertionError:
            print("the character of the account is less than 8 or more than 8 it should be equal to 8 character")

        try:
            assert re.fullmatch(r"^[0-9]{4}$",str(dep_password))
        except AssertionError:
            print("the password should have 4 integer character")

        account_present:bool = False
        password_correct:bool = False
        new_balance:float = 0.0

        with open("data.csv") as f:
            reader = csv.DictReader(f)
            accounts = list(reader)

        for rows in accounts:
            if dep_acc_no == rows["account_no"]:
                account_present = True
                if str(dep_password) == rows["password"]:
                    password_correct = True
                    current_balance = float(rows["balance"])
                    new_balance = current_balance + deposit_amount
                    rows["balance"] = new_balance
                    print(f"TOTAL AMOUNT of your ACCOUNT : {new_balance}")
                    
        if not account_present:
            print(f"INCORRECT ACCOUNT NUMBER:{dep_acc_no}")

        if not password_correct:
            print(f"INCORRECT PASSWORD:{dep_password}")
        
        if account_present == True and password_correct == True:
            with open("data.csv","w") as fw:
                write = csv.DictWriter(fw,fieldnames=["name","age","dob","phone","address","account_no","password","balance"])
                write.writeheader()  
                write.writerows(accounts)
            
    @classmethod         
    def withdraw(cls):
        wd_acc_no = input("Enter your Account number to withdraw:")
        wd_pass = int(input("Enter the password:"))
        wd_amount = float(input("Enter the amount to withdraw:"))

        try:
            assert re.fullmatch(r"^[0-9]{8}$",wd_acc_no)
        except AssertionError:
            print("the character of the account is less than 8 or more than 8 it should be equal to 8 character")

        try:
            assert re.fullmatch(r"^[0-9]{4}$",str(wd_pass))
        except AssertionError:
            print("the password should have 4 integer character")

        account_correct:bool = False
        password_correct:bool = False

        with open("data.csv") as file:
            read = csv.DictReader(file,fieldnames=["name","age","dob","phone","address","account_no","password","balance"])
            account = list(read)
        
        for row in account:
            if wd_acc_no in row["account_no"]:
                account_correct = True
                if str(wd_pass) in row["password"]:
                    password_correct = True
                    current_amount = float(row["balance"])
                    if wd_amount > current_amount:
                        print(f"your current balance:{current_amount} is less than your withdraw amount:{wd_amount}")
                    else:
                        new_balance = current_amount - wd_amount
                        row["balance"] = new_balance
                        print(f"Your current balance of your Account:{new_balance}")
                        row["balance"] = new_balance
                    
        if not account_correct:
            print(f"INCORRECT ACCOUNT NUMBER:{wd_acc_no}")

        if not password_correct:
            print(f"INCORRECT PASSWORD:{wd_pass}")

        if account_correct == True and password_correct == True:

            with open("data.csv","w") as files:
                write = csv.DictWriter(files,fieldnames=["name","age","dob","phone","address","account_no","password","balance"])
                write.writerows(account)
        
    @classmethod
    def transaction(cls):

        sender_account_no = input("Enter your Account number:")
        send_pin = int(input("Enter your password:"))
        Amount_Tras = float(input("Enter the amount to transfer:"))
        transfer_acc_no = input("Enter the sender's account nmuber:")

        try:
            assert re.fullmatch(r"^[0-9]{8}$",sender_account_no)
        except AssertionError:
            print("the character of the account is less than 8 or more than 8 it should be equal to 8 character")

        try:
            assert re.fullmatch(r"^[0-9]{8}$",transfer_acc_no)
        except AssertionError:
            print("the character of the account is less than 8 or more than 8 it should be equal to 8 character")

        try:
            assert re.fullmatch(r"^[0-9]{4}$",str(send_pin))
        except AssertionError:
            print("the password should have 4 integer character")

        sender:bool = True
        s_pin:bool = True
        reciver:bool = True

        with open("data.csv") as f:
            reader = csv.DictReader(f,fieldnames=["name","age","dob","phone","address","account_no","password","balance"])
            detail = list(reader)

        for row in detail:

            if  sender_account_no in row["account_no"]:
                sender = True

                if str(send_pin) in row["password"]:
                    s_pin = True 
                    current_amount = float(row["balance"])
                    if Amount_Tras > current_amount:
                        print(f"your current balance:{current_amount} is less than your withdraw amount:{Amount_Tras}")
                    else:    
                        new_balance = current_amount - Amount_Tras
                        print(f"CURRENT BALANCE:{new_balance} of your account")
                        row["balance"] = new_balance

        for row in detail:               

            if transfer_acc_no in row["account_no"] :
                reciver = True

                reciver_curr_amt = float(row["balance"])
                rev_balance = reciver_curr_amt + Amount_Tras
                row["balance"] = rev_balance

        if not sender:
            print(f"INCORRECT ACCOUNT NUMBER:{sender_account_no}")

        if not s_pin:
            print(f"INCORRECT PASSWORD:{send_pin}")

        if not reciver:
            print(f"INCORRECT ACCOUNT NUMBER:{transfer_acc_no}")

        if sender == True and s_pin == True and reciver == True:

            with open("data.csv","w") as files:
 
                write_t = csv.DictWriter(files,fieldnames=["name","age","dob","phone","address","account_no","password","balance"])
                write_t.writerows(detail)


    @classmethod
    def view_account(cls):
        
        va_account = input("enter the Account no: ")
        va_pass = input("enter the password: ")

        try:
            assert re.fullmatch(r"^[0-9]{8}$",va_account)
        except AssertionError:
            print("the character of the account is less than 8 or more than 8 it should be equal to 8 character")

        try:
            assert re.fullmatch(r"^[0-9]{4}$",va_pass)
        except AssertionError:
            print("the password should have 4 integer character")

        account_present:bool = False
        password_correct:bool = False

        with open("data.csv") as f:
            reader = csv.DictReader(f,fieldnames=["name","age","dob","phone","address","account_no","password","balance"])
            account = list(reader)
            
        for row in account:
            if va_account in row["account_no"]:
                account_present = True
                if va_pass in row["password"]:
                    password_correct = True
                    print(f"NAME: {row['name']}\nACC_NO: {va_account}\nbalance :{row["balance"]}")
    
        if not account_present:
            print(f"INVALID ACCOUNT NO:{va_account}")

        if not password_correct:
            print(f"INCORRECT PASSWORD:{va_pass}")

    @classmethod
    def Veiw_all(cls):

        data_view = pd.read_csv("data.csv")

        print(data_view)
