''' PRIVOURNAL STORES NO DATA EXCEPT ACCOUNT DETAILS.
ECRYPTIONS AND DECRYPTIONS PURELY DONE BY LOGIC AND ENCRYPTION DATA IN USER'S ACCOUNT.
ENCRYPTION DATA CAN BE ALSO PASSWORD PROTECTED.
NOTE : ENCRYPTED TEXT HAS TO BE GIVEN BY USER '''

#DATABASE

import mysql.connector as sql

mycon = sql.connect(host="localhost",
                    user="root",
                    database="privournal",
                    password="manimonit09")

if mycon.is_connectedd():
    print("Connection's strong!")
else:
    print("Not connected.")

cursor = mycon.cursor()

cursor.execute("CREATE TABLE records (Name VARCHAR(255) NOTNULL, pswd VARCHAR(255) NOTNULL, email VARCHAT(255) NOTNULL, userid INT NOT NULL);")
def feed():
    journal = input("Please feed the Journal : ")

    if journal == "":
        print("Empty Journal!")
    else:
        print("Journal Uploaded!")


def start():
    print("Welcome to Privournal!")
    print("We help your Journals stay Private and Safe :) ")
    basic()



def Menu():
    print()
    print()
    print("What would you like to do today?")
    print()
    print("1. Encrypt a Journal Entry")
    print("2. Decrypt a Journal Entry")
    print("(Enter just 1 OR 2)")
    print()
    ch = int(input("I want to : "))


    if ch == 1:
        En()
    elif ch == 2:
        De()


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
            swiptionEn()

        elif ask == "N" or ask == "n":
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
        username = tusername


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
            pswd = tpswd
            print()
            print("Account made succesfully!")
            print()
            print()
            Menu()

        else:
            print("The passwords don't match.")
            signup()


def De():
    print("Let's start Decryption!")


def Endet():
    print("All encryption details should be pasted in a table format.")
    print("Should contain Date, ID, Name, Type of Encryption, Additional Password Protection (Optional)")



def login():

    username1 = input("Enter Username : ")
    pswd1 = input("Enter Password : ")

    print("Seach for username1 in db using traversing and check if it's pass is same as pswd1")

    if pswd1 == pswd:
        print("Logged in Successfully!")
        print()
        print()
        Endet()
        print()
        print()
        Menu()



    else:
        print("Wrong Password.")

    print()
    print()
    login()


def exit():
    basic()

start()
basic()

cursor.close()
mycon.close()