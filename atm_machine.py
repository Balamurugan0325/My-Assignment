import mysql.connector
import datetime
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bala@2003",
    database="bala_db",
)
mycursor=mydb.cursor()

def insert_data(name,account_number,password,amount):
    sql="insert into customers_details (name,account_number,password,amount) values (%s,%s,%s,%s)"
    val=(name,account_number,password,amount)
    mycursor.execute(sql,val)
    mydb.commit()

print("\t\t\t Welcome To IOB Bank ATM \t\t\t")
print("1.deposite amount")
print("2.withdraw amount")
print("3.pin change")
print("\n")

x=datetime.datetime.now()
print(x)

print("1.English \n2.Tamil \n3.Hindi")

Language=int(input("select the language:"))

if Language==1:
    print("your language english")
elif Language==2:
    print("your language tamil")
elif Language==3:
    print("your language hindi")
else:
    print("incorrect choice")

try:
    print("select operations \n1.deposite\n2.withdraw\n3.pin change")

    user=int(input("select the number:"))

    if user==1:

        name=input("Enter your Name:").lower().strip()
        account_number=int(input("Enter your account_Number:"))
        password=int(input("Enter your Password:"))
        amount=int(input("Enter deposite amount:"))
        print("your amount is successfully deposited")
        print("thank you and come again")
        insert_data(name,account_number,password,amount)

    elif user==2:

        name=input("Enter your Name:").lower().strip()
        account_number=int(input("Enter your account_number:"))
        password=int(input("Enter your Password:"))
        amount=int(input("Enter withdraw amount:"))
        print("you are successfully withdraw the amount")
        print("thank you and come again")
        insert_data(name,account_number,password,amount)

    elif user==3:

        name=input("Enter yuor Name:").lower().strip()
        account_number=int(input("ENter your account number:"))
        password=int(input("Enter your Password:"))
        mobile_number=int(input("Enter your mobile number:"))
        print("Your password has been successfully changed")
        print("thank you and come again")
        insert_data(name,account_number,mobile_number,password)

    else:
        print("choice only 1 to 3")    
except:
    print("Give me number only ")