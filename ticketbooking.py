import mysql.connector

mydb=mysql.connector.connect(
   host="localhost",
   user="root",
   password="Bala@2003",
   database="student"

)
mycursor=mydb.cursor()
#Ticketprice
chennai=1800
chennai_ac=2500
coimbatore=800
coimbatore_ac=1500
madhurai=600
madhurai_ac=900
nagercovil=300
nagercovil_ac=500
salem=700
salem_ac=1200
tuticorin=400
tuticorin_ac=800
virudhunagar=900
virudhunagar_ac=1300
#**********************************************************
def travel(Name,Phone_No,From_loc,To_loc,Tickets,Price):
    sql="insert into passenger_detail(Name,Phone_No,From_loc,To_loc,Tickets,Price) values (%s,%s,%s,%s,%s,%s)"
    val=(Name,Phone_No,From_loc,To_loc,Tickets,Price)
    mycursor.execute(sql,val)
    mydb.commit()

def ticketdetailes():
        print("")
        print("***************************************************")
        print("\t\t |**Ticket Detailes**|")
        print(f"Name:{Name}")
        print(f"Phone_No:{Phone_No}")
        print(f"From:{From_loc}")
        print(f"To:{To_loc}")
        print(f"Tickets:{Tickets}")
        print(f"Totel Price:{Price}")
        print("Your Tickets Was Booked \n Happy Journey")
        print("***************************************************")

user=input("Enter GO To Book Tickets:").lower().strip()
if user=="go":
    print("***Welcome To Ticket Booking***")
    Name=input("Enter Your Name:")
    Phone_No=int(input("Enter Your Phone_No:"))
    From_loc="Thirunelveli"
    print("")
    print("Thirunelveli To:\n1.Chennai\n2.Coimbatore\n3.Madhurai\n4.Nagercovil\n5.Salem\n6.Tuticorin\n7.Virudhunagar\n")
    To_loc=input("Enter Your Destination:").lower().strip()
    print("")
    print("1.A/c\n2.NON-A/C")
    print("")
    Type=int(input("Select Your Choice:"))
    if To_loc=="chennai" and Type==1:
        print(f"{From_loc}->Chennai")
        print(f"Ticket Price:{chennai_ac}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*chennai_ac
        ticketdetailes()
    elif To_loc=="chennai" and Type==2:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{chennai}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*chennai
        ticketdetailes()
    elif To_loc=="coimbatore" and Type==1:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{coimbatore}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*coimbatore
        ticketdetailes()
    elif To_loc=="coimbatore" and Type==2:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{coimbatore_ac}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*coimbatore_ac
        ticketdetailes()
    elif To_loc=="madhurai" and Type==1:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{madhurai}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*madhurai
        ticketdetailes()
    elif To_loc=="madhurai" and Type==2:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{madhurai_ac}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*madhurai_ac
        ticketdetailes()
    elif To_loc=="nagercovil" and Type==1:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{nagercovil}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*nagercovil
        ticketdetailes()
    elif To_loc=="nagercovil" and Type==2:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{nagercovil_ac}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*nagercovil_ac
        ticketdetailes()
    elif To_loc=="salem" and Type==1:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{salem}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*salem
        ticketdetailes()
    elif To_loc=="coimbatore" and Type==2:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{coimbatore_ac}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*coimbatore_ac
        ticketdetailes()
    elif To_loc=="tuticorin" and Type==1:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{tuticorin}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*tuticorin
        ticketdetailes()
    elif To_loc=="tuticorin" and Type==2:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{tuticorin_ac}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*tuticorin_ac
        ticketdetailes()
    elif To_loc=="virudhunagar" and Type==1:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{virudhunagar}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*virudhunagar
        ticketdetailes()
    elif To_loc=="virudhunagar" and Type==2:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{virudhunagar_ac}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*virudhunagar_ac
        ticketdetailes()
    else:
        print("")
        print("incorrect choice")
        print("")

else:
    print("")
    print("incorrect choice")
    print("")

travel(Name,Phone_No,From_loc,To_loc,Tickets,Price)