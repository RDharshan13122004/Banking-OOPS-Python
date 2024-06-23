from code import BankAccount

def main():
    
    name = input("enter the name:").strip().lower()
    age = int(input("enter the age:"))
    d = input("enter the dob:")
    phone = input("enter the phoneno:").strip()
    addr = input("enter the address:").strip()
    Acc = int(input("enter the Acc_no:"))
    ps = int(input("enter the password:"))
    Amount = float(input("enter the amount to initail depost:"))


    us = BankAccount(name,age,d,phone,addr,Acc,ps,Amount)
    print(us)
    

    #or
    
    #us = BankAccount("vaishunavi",25,"23/05/2001","9040074560","egdhe,egee,erhhe",10010011,6896,10000)
    #print(us)



    #===================== view your account detail ==============#
    
    BankAccount.view_account()

    #+++++++++++++++++++ deposit +++++++++++++++++++++#

    BankAccount.deposit()

    #+++++++++++++++++++++ withdraw ++++++++++++++++++#

    BankAccount.withdraw()

    #+++++++++++++++++++++ veiw all +++++++++++++++++++#

    BankAccount.Veiw_all()

    #++++++++++++++ transaction ++++++++++++++++++++++=#

    BankAccount.transaction()

if __name__ == "__main__":
    main()