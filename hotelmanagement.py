
import datetime

Date_and_Time=datetime.datetime.now()


import mysql.connector

mydb=mysql.connector.connect(
   host="localhost",
   user="root",
   password="Bala@2003",
   database="mydb"

)
mycursor=mydb.cursor()#Breakfast time menucard
menu_breakfast=["idly","dhosa","pongal","casari","vada","boori"]
idly=8
dhosa=15
pongal=35
casari=10
vada=6
boori=20
#lunch time menucard
menu_lunch=["biriyani","fullmeals","parotta","curdrice"]
biriyani=180
fullmeals=120
parotta=15
curdrice=35
#Dinner time menucard
menu_dinner=["chappathi","noodlles","parotta","friedrice"]
chappathi=15
noodlles=90
parotta=15
friedrice=140


def breakfast_data(Name,Mobile_No,Time,Food,Bill):
    sql="insert into hotel_bill(Name,Mobile_No,Time,Food,Bill) values (%s,%s,%s,%s,%s)"
    val=(Name,Mobile_No,Time,Food,Bill)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Get Your Bill")
    print("**************************************************")
    print(f"\t\t\t{Date_and_Time}")
    print(f"Name:{Name}\n\nMobile No:{Mobile_No}\n\nTime:{Time}\n\nFood:{Food}\n\nTotal Bill:{Bill}")
    print("**************************************************")


user=input("Enter **go** to Order:").lower().strip()
if user=="go":
    Name=input("Enter Your Name:").lower().strip()
    Mobile_No=int(input("Enter Your Mobile No:"))
    print("***Enter your choice breakfast or lunch or dinner***")
    Time=input("Enter Time:").lower().strip()
    if(Time=="breakfast"):
        print("")
        print("***Breakfast List***")
        print("idly\ndhosa\npongal\ncasari\nvada\nboori")
        print("")
        Food=input("Enter your order:").lower().strip()
        if(Food in menu_breakfast):
            if(Food=="idly"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*idly
            elif(Food=="boori"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*boori
            elif(Food=="dhosa"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*dhosa
            elif(Food=="pongal"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*pongal
            elif(Food=="casari"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*casari
            elif(Food=="vada"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*vada

    elif(Time=="lunch"):
        print("")
        print("***Lunch List***")
        print("biriyani\nfullmeals\nparotta\ncurdrice")
        print("")
        Food=input("Enter your order:").lower().strip()
        if(Food in menu_lunch):
            if(Food=="biriyani"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*biriyani
            elif(Food=="fullmeals"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*fullmeals
            elif(Food=="parotta"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*parotta
            elif(Food=="curdrice"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*curdrice

    elif(Time=="dinner"):
        print("")
        print("***Dinner List***")
        print("chappathi\nnoodlles\nparotta\nfriedrice")
        print("")
        Food=input("Enter your order:").lower().strip()
        if(Food in menu_dinner):
            if(Food=="chappathi"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*chappathi
            elif(Food=="noodlles"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*noodlles
            elif(Food=="parotta"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*parotta
            elif(Food=="friedrice"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*friedrice
    else:
        print("")
        print("Enter Correctly")
        print("")
else:
    print("")
    print("Enter Start Correctly")
    print("")
            
breakfast_data(Name,Mobile_No,Time,Food,Price)
    