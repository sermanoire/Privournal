''' PRIVOURNAL STORES NO DATA EXCEPT ACCOUNT DETAILS.
ECRYPTIONS AND DECRYPTIONS PURELY DONE BY LOGIC AND ENCRYPTION DATA IN USER'S ACCOUNT.
ENCRYPTION DATA CAN BE ALSO PASSWORD PROTECTED.
NOTE : ENCRYPTED TEXT HAS TO BE GIVEN BY USER '''

#FOR MY REFENECE - DATA Fetchall -> List of different records and each column's info in a tuple.

#Imports :)
import random
import string
import json
import time
from datetime import date
status = 0




#DOTENV_CONNECTION
from dotenv import load_dotenv
import os
load_dotenv()

import mysql.connector as sql


#DB_CONNECTION
mycon = sql.connect(host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    database=os.getenv("DB_NAME"),
                    password=os.getenv("DB_PASSWORD"))

if mycon.is_connected():
    print("Connection's strong!")
else:
    print("Not connected.")

cursor = mycon.cursor()





def start():
    print()
    print()
    print("Welcome to Privournal!")
    print("We help your Journals stay Private and Safe :) ")
    print()
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


def exit():
    print("Thank you so much for using Privournal, Have a nice day!")
    print("Byeeeeee :)")


def De():
    print("Let's start Decryption!")

    if status == 1:

        cursor.execute('''
        SELECT jd.*
        FROM journal_details jd
        JOIN user_records ur
        ON jd.user_id = ur.user_id
        WHERE ur.username = %s
        ''', (username,))


        j_data = cursor.fetchall()

        user_id.append(j_data[0][0])
        print("User_ID is",user_id)

        j_id = []
        for i in j_data:
            j_id.append(j_data[i][1])
            print("Journal_ID",i+1, j_id)

        j_name = []
        for i in j_data:
            j_name.append(j_data[i][2])
            print("Journal_Name", i + 1, j_id)

        en_key = []
        for i in j_data:
            en_key.append(j_data[i][3])
            print("Encryption_Key", i + 1, j_id)

        en_date = []
        for i in j_data:
            en_date.append(j_data[i][4])
            print("Encryption_Date", i + 1, j_id)

            Ch = int(input("Which Journal do you want to Decrypt? (Enter Journal_ID) : "))

            if Ch not in en_key:
                print("Journal not found. Check the ID again!")
                which_j()

            for i in en_key:

                if en_key[i] == Ch:
                    KEY = en_key[i]
                else:
                    continue

            print("Starting Decryption!")

            og_dict_key = json.loads(KEY)
            RAW = input("Enter the raw encrypted journal : ")

            tempstore = []
            for i in RAW:
                for key, value in og_dict_key.items():
                    if not i.isalnum():
                        tempstore.append(i)

                    elif i == value:
                        tempstore.append(key)
                    else:
                        continue

            decrypted = "".join(tempstore)

            print()
            print("Decrypted!")
            print("Here's your Journal --> ", decrypted)
            print()
            print()
            print("You will be redirect to Menu in 15 seconds :) ")
            time.sleep(1)
            print("You can copy your decrypted journal and save it somewhere safe!")
            time.sleep(15)
            Menu()

        elif status != 1:
        Ch3 = input("Do you have an Account on Privournal? (Y/N) : ")

        if Ch3 == "y" or Ch3 == "Y":
            login()
        elif Ch3 == "n" or Ch3 == "N":

            print()
            print('''
                    1. Basic Encryption
                    2. Advanced Encryption 
                                        ''')

            Ch4 = input("Which Encryption does your Journal have? (1 OR 2) : ")
            if Ch4 == 1:

                Ch10 = input("Do you have the Encryption Key? (Y/N) : ")

                if Ch6 == "y" or Ch6 == "Y":

                    # Mark 1
                    mark1 = {}
                    for i in range(26):
                        mark1[chr(65 + i)] = i + 1
                        mark1[chr(97 + i)] = 27 + i

                    # ASCII Version!
                    asciiv = {}
                    for i in range(65, 91):
                        asciiv[chr(i)] = i
                    for j in range(97, 123):
                        ascivv[chr(i)] = i

                        # Mark 2
                    mark2 = {}
                    for i in range(26):
                        mark2[chr(65 + i)] = (26 - i)
                        mark2[chr(97 + i)] = 52 - i

                    # Mark 3
                    mark3 = {}
                    for i in range(26):
                        mark3[chr(65 + i)] = str(2 * (i + 1))+" "
                        mark3[chr(97 + i)] = str((2 * i) + 1)+" "

                    # Mark 4
                    mark4 = {}
                    for i in range(26):
                        mark4[chr(65 + i)] = chr(90 - i)+" "
                        mark4[chr(97 + i)] = chr(122 - i)+" "

                    print()
                    print("1. Mark 1 (A to Z from 1 to 26 respectively, and a to z from 27 to 52 respectively.)")
                    print("2. ASCII Version")
                    print("3. Mark 2 (A to Z from 26 to 1 respectively, and a to z from 52 to 26 respectively.)")
                    print(
                        "4. Mark 3 (A to Z from 2 to 52 respectively, even numbers only. And a to z from 1 to 51, odd numbers only.)")
                    print("5. Mark 4 (A to Z from Z to A respectively and a to z from z to a respectively.)")
                    print()
                    print()

                    Ch5 = input("Which one out of these? : ")

                    if Ch5 == 1:

                        RAW = input("Enter the Encrypted text : ")

                        for i in RAW:
                            if i in mark1:



                elif Ch10 == "n" or Ch10 == "N":
                    print(
                        "We're sorry, we cannot Decryption without the Key. \nBe sure to make an account on Privournal if you have trouble keeping Keys.")
                    print()
                    print("You will be redirected to the Menu Shortly.")
                    time.sleep(3)
                    Menu()














            elif Ch4 == 2:

                Ch6 = input("Do you have the Encryption Key? (Y/N) : ")

                if Ch6 == "y" or Ch6 == "Y":
                    given_dict_key = input("Enter the Encryption Key please : ")
                    og_dict_key = json.loads(given_dict_key)

                    RAW = input("Enter the raw encrypted journal please : ")

                    tempstore = []
                    for i in RAW:
                        for key, value in og_dict_key.items():
                            if not i.isalnum():
                                tempstore.append(i)

                            elif i == value:
                                tempstore.append(key)
                            else:
                                continue

                    decrypted = "".join(tempstore)

                    print()
                    print("Decrypted!")
                    print("Here's your Journal --> ", decrypted)
                    print()
                    print()
                    print("You will be redirect to Menu in 15 seconds :) ")
                    time.sleep(1)
                    print("You can copy your decrypted journal and save it somewhere safe!")
                    print("Thank you for using Privournal!")
                    time.sleep(15)
                    Menu()



                elif Ch6 == "n" or Ch6 == "N":
                    print(
                        "We're sorry, we cannot Decryption without the Key. \nBe sure to make an account on Privournal if you have trouble keeping Keys.")
                    print()
                    print("You will be redirected to the Menu Shortly.")
                    time.sleep(3)
                    Menu()

                    og_dict_key = json.loads(KEY)




                else:
                    print("Invalid choice!")
                    De()



def login():

        username1 = input("Enter Username : ")
        pswd1 = input("Enter Password : ")

        cursor.execute(
            "SELECT password FROM user_records WHERE username = %s",
            (username1,)
        )

        fetchedetails = cursor.fetchall()

        if fetchedetails == None:
            print("No such Username in our database found!")
        else:

            if pswd1 == result[0][0]:
                print("Logged in Successfully!")

                cursor.execute(
                    "SELECT * FROM user_records WHERE username = %s",
                    (username1,)
                )

                fetchedetails = cursor.fetchall()

                user_id = fetchedetails[0][0]
                name = fetchedetails[0][1]
                username = fetchedetails[0][2]
                email = fetchedetails[0][3]
                account_created = fetchedetails[0][4]
                password = fetchedetails[0][5]
                print()
                print()
                status = 1
                print("You will be redirected to the menu shortly.")
                time.sleep(3)
                Menu()



            else:
                print("Wrong Password.")
                print()
                exch = int(input("Exit or login again? (1/2) : "))
                if exch == 1:
                    exit()
                elif exch == 2:
                    login()
                else:
                    print("Invalid Choice!")





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

        #HEHE GOTTA FILL THIS THING

    elif ch2 == 2:
        print("Advanced Encryption it is then!")
        print()
        ask = input("Do you want to enable Swiption for a stronger Encryption? (Y/N) : ")

        if ask == "Y" or ask == "y":
            m = 1
            print("swiptionEn()")
            #IN PROGRESS


        elif ask == "N" or ask == "n":
            m = 2
            AdvEn()


        else:
            print("Invalid choice")
            En()


def AdvEn():

    if status != 1:

        Ch8 = input("Do you have an Account? (Y/N) : ")

        if Ch8 == "Y" or Ch8 == "y":
            print("You'll be redirected to Login page, please complete the login first :) ")
            time.sleep(3)
            login()

        elif Ch8 == "N" or Ch8 == "n":

            print("Do you want to save encryption details on our database for future decryptions and referencing records?")
            Ch7 = input("(Y/N) : ")

            if Ch7 == "Y" or Ch7 == "y":
                signup()

            elif Ch7 == "N" or Ch7 == "n":
                print("Please have all the encryption details saved with you then!")

                enlist = []
                cover_dict = {}
                feed()
                print("Choose cover for each letter!")

                for i in range(65, 91, 1):
                    cover_dict = {i: "" for i in range(65, 91)}
                for j in range(97, 123, 1):
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
                print("You'll be redirected to the a new page.")
                print()
                print()
                time.sleep(5)




            else:
                print("Invalid input!")
                AdvEn()


    else:
        enlist = []
        cover_dict = {}
        feed()
        print("Choose cover for each letter!")

        for i in range(65, 91, 1):
            cover_dict = {i: "" for i in range(65, 91)}
        for j in range(97, 123, 1):
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

        cursor.execute("Select user_id from user_records where ")

        user_id
        journal_name = jname
        encryption_key = json.dumps(key_dict)
        encryption_date = date.today()

        cursor.execute(
            """
            INSERT INTO journal_details
            (user_id, journal_name, encryption_key, encryption_date)
            VALUES (%s, %s, %s, %s)
            """,
            (userid, journal_name, encryption_key, encryption_date))


        print()
        print("Here's the encrypted Journal : ")
        print()
        print(finalenlist)
        print()
        print("Thank you for using Privournal!")
        print("You'll be redirected to the menu.")

        print()
        print()
        time.sleep(5)
        menu()


def feed():
    journal = input("Please feed the Journal for Encryption : ")
    jname = input("Please name your Journal : ")


    if journal:
        print("Empty Journal!")
        feed()
    else:
        print("Journal Uploaded!")



def optional():
    print("Do you want to save encryption details on our database for future decryptions and referencing records?")
    Ch7 = input("(Y/N) : ")

    if ch4 == "Y" or ch3 == "y":
        signup()

    elif ch4 == "N" or ch4 == "n":
        print("Please have all the encryption details saved with you then!")
        print(str(cover_dict))
        print()
        print("You'll be redirected to Advanced Encryption page")
        time.sleep(3)
        AdvEn()

    else:
        print("Invalid input!")
        optional()




def signup():

    cursor.execute("SELECT COUNT(DISTINCT username) FROM user_records")
    user_id = cursor.fetchone()[0]

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
            password = tpswd

            name = input("Enter your name : ")
            email = input("Enter email please : ")
            account_created = date.today()
            print()
            cursor.execute(
                """
                INSERT INTO journal_details
                (user_id, first_name, username, email, account_created, password)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (user_id, name, username, email, account_created, password))
            print()
            print("Account made succesfully!")
            print()
            print("You'll be redirected to the menu, you can now start Encrypting and Decrypting without hassle! ")
            time.sleep(3)
            print()
            menu()



        else:
            print("The passwords don't match.")
            signup()


start()
basic()

cursor.close()
mycon.close()


