''' PRIVOURNAL STORES NO DATA EXCEPT ACCOUNT DETAILS.
ECRYPTIONS AND DECRYPTIONS PURELY DONE BY LOGIC AND ENCRYPTION DATA IN USER'S ACCOUNT.
ENCRYPTION DATA CAN BE ALSO PASSWORD PROTECTED.
NOTE : ENCRYPTED TEXT HAS TO BE GIVEN BY USER '''

#DATABASE

#DATA Fetchall -- List of different records and each column's info in a tuple.

from dotenv import load_dotenv
import os
load_dotenv()

load_dotenv()
import mysql.connector as sql

mycon = sql.connect(host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    database=os.getenv("DB_NAME"),
                    password=os.getenv("DB_PASSWORD"))

if mycon.is_connected():
    print("Connection's strong!")
else:
    print("Not connected.")

cursor = mycon.cursor()

cursor.execute("SELECT * FROM records")
print(cursor.fetchall())

from datetime import date

today = date.today()

def optional():
    print("Do you want to save encryption details on our database for future decryptions and referencing records?")
    ch4 = input("(Y/N) : ")

    if ch4 == "Y" or ch3 == "y":
        basic()
    elif ch4 == "N" or ch4 == "n":
        print("Please have all the encryption details saved with you!")
        print(str(cover_dict))
        exit()
    else:
        print("Invalid input!")
        optional()

def exit():
    print()
    print("Thank you for using Privournal!")
    print("Be sure to keep your encrytion details in your memory or on some paper! \n(If you do not have an account)")
    print("Bye!")
    print()
    print()
    print()
    Menu()

def feed():
    journal = input("Please feed the Journal for Encryption : ")

    if journal:
        print("Empty Journal!")
    else:
        print("Journal Uploaded!")



def start():
    print()
    print()
    print("Welcome to Privournal!")
    print("We help your Journals stay Private and Safe :) ")
    Menu()



def Menu():
    print()
    print()
    print("What would you like to do today?")
    print()
    print("1. Encrypt a Journal Entry")
    print("2. Decrypt a Journal Entry")
    print("3. Exit")
    print("(Enter just 1 OR 2 OR 3)")
    print()
    ch = int(input("I want to : "))



    if ch == 1:
        En()
    elif ch == 2:
        De()
    elif ch == 3:
        exit()
    else:
        print("Invalid Choice")
        Menu()


def basic():
    ques = input("Do you have an account? (Y/N) : ")
    if ques == "y" or ques == "Y":
        login()
    elif ques == "N" or ques == "n":
        signup()
    else:
        print("Invalid Answer!")
        print()
        print()
        basic()

def En():


    print("Choose Mode of Encryption :) ")
    print("1. Basic (Weak but holds well if you have dummies tryna read your Journal)")
    print(
        "2. Advanced (Includes Swiption - Really strong encryption, holds well even if you have prodigies trying to read your Journal.")
    print()
    print("Which one? 1 OR 2?")
    ch2 = int(input("I choose : "))

    if ch2 == 1:
        print("Welcome to Basic Encryption!")
        print("Please choose one of the following : ")
        print()
        print("1. Mark 1 (A to Z from 1 to 26 respectively, and a to z from 27 to 52 respectively.)")
        print("2. ASCII Version")
        print("3. Mark 2 (A to Z from 26 to 1 respectively, and a to z from 52 to 26 respectively.)")
        print("4. Mark 3 (A to Z from 2 to 52 respectively, even numbers only. And a to z from 1 to 51, odd numbers only.)")
        print("5. Mark 4 (A to Z from Z to A respectively and a to z from z to a respectively.)")

    elif ch2 == 2:
        print("Advanced Encryption in progress.")
        print()
        ask = input("Do you want to enable Swiption for a stronger Encryption? (Y/N) : ")

        if ask == "Y" or ask == "y":
            m = 1
            print("swiptionEn()")


        elif ask == "N" or ask == "n":
            m = 2
            AdvEn()


        else:
            print("Invalid choice")



def signup():
    tusername = input("Set a username : ")

    if len(tusername)>16:
        print("Invalid! It should be at most 16 characters.")
        print()
        print()
        signup()

    elif " " in tusername:
        print("Spaces not allowed!")
        print()
        print()
        signup()

    elif len(tusername)<6:
        print("Should be atleast 6 characters long!")
        print()
        print()
        signup()

    else:
        username2 = tusername


    tpswd = input("Set a password : ")

    if len(tpswd)>16:
        print("Invalid! It should be at most 18 characters.")
        print()
        print()
        signup()

    elif " " in tpswd:
        print("Spaces not allowed!")
        print()
        print()
        signup()

    elif len(tpswd)<8:
        print("Should be atleast 8 characters long!")
        print()
        print()
        signup()

    elif tpswd==username:
        print("Username and password cannot be same!")

    else:
        t_conf_pswd = input("Confrim password : ")

        if t_conf_pswd == tpswd:
            pswd2 = tpswd
            print()
            print("Account made succesfully!")
            print()
            print()
            input("Name your Journal --> ")
            data = cursor.fetchall()
            user_id = len(data)
            print("Your user_id is ",user_id)
            if m == 1:
                encryptionmode = "Adv. Encryption with Swiption"

            elif m == 2:
                encryptionmode = "Adv. Encryption"
                encryptiondetails = str(cover_dict)


            date = today

            #ADD TO DATABASE!

            print("Successfully added to Database!")
            Menu()


        else:
            print("The passwords don't match.")
            signup()


def De():
    print("Let's start Decryption!")

    if status == 1:

    ch5 = input("Do you have an Account on Privournal? (Y/N) : ")
    if ch5 == "y" or ch5 == "Y":
        login()
    elif ch5 == "n" or ch5 == "N":
        ch6 = input("Do you remember the encryption detail or have it ritten down? (Y/N) ")
        if ch6 == "y" or ch6 == "Y":
            print("Select one. (1 or 2)")
            print('''
            1. Basic Encryption
            2. Advanced Ecryption 
            ''')

            ch7 = input("Enter Choice : ")
            if ch7 == 1:
                print("Choose an Ecryption : ")
                print()
                print("1. Mark 1 (A to Z from 1 to 26 respectively, and a to z from 27 to 52 respectively.)")
                print("2. ASCII Version")
                print("3. Mark 2 (A to Z from 26 to 1 respectively, and a to z from 52 to 26 respectively.)")
                print(
                    "4. Mark 3 (A to Z from 2 to 52 respectively, even numbers only. And a to z from 1 to 51, odd numbers only.)")
                print("5. Mark 4 (A to Z from Z to A respectively and a to z from z to a respectively.)")
                print()

            elif ch7 == 2:
                encryptedjournal = input("Please enter the raw encrypted Journal in text format : ")
                enjournal = list(encryptedjournal)
                encryptiondetails = input("Enter the encryption details provided by Privournal :")

                cover_dict1 = dict(encryptiondetails)


                for k in enjournal:
                        y = cover_dict1[ord(k)]

                        index = enjournal.index(k)
                        enjournal[index] = y

                    finaloutput = "".join(enjournal)
                    print()
                    print("Here is your decrypted text :)")
                    print(finaloutput)
                    print()
                    print("Thank you so much for using Privournal.")
                    print("You'll be redirected to the menu...")
                    Menu()



def Endet():
    print("All encryption details should be pasted in a table format.")
    print("Should contain Date, ID, Name, Type of Encryption, Additional Password Protection (Optional)")


def login():

    username1 = input("Enter Username : ")
    pswd1 = input("Enter Password : ")

    cursor.execute(
        "SELECT password FROM records WHERE username = %s",
        (username,)
    )

    result = cursor.fetchone()

    if result == None:
        print("No such Username in our database found!")
    else:


      pswd = result[0]


    if pswd1 == pswd:
        print("Logged in Successfully!")
        print()
        print()
        status = 1
        Menu()



    else:
        print("Wrong Password.")

    print()
    exch = int(input("Exit or login again? (1/2) : "))
    if exch == 1:
        exit()
    elif exch = 2:
        login()
    else:
        print("Wrong.")



def exit():
    basic()

def AdvEn():

    enlist = []
    feed()
    print("Choose cover for each letter!")
    ch3 = input("Do you want to keep capitals and smalls seperate? (Y/N) ")

    if ch3 == "Y" or ch3 == "y":
        for i in range(65,91,1):
            cover_dict = {i: "" for i in range(65, 91)}
        for j in range(97,123,1):
            cover_dict.update({i: "" for i in range(97, 123)})

        for x in journal:
            if text.isalpha():
                x1 = ord(x)
                m = cover_dict[x1]
                enlist.append(m)
            else:
                enlist.append(m)

    finalenlist = "".join(enlist)
    print()
    print("Successfully Encrypted!")
    print()
    print("Here's the encrypted Journal : ")
    print(finalenlist)
    print()
    print()
    optional()

start()
basic()

cursor.close()
mycon.close()
