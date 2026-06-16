''' PRIVOURNAL STORES NO DATA EXCEPT ACCOUNT DETAILS.
ECRYPTIONS AND DECRYPTIONS PURELY DONE BY LOGIC AND ENCRYPTION DATA IN USER'S ACCOUNT.
ENCRYPTION DATA CAN BE ALSO PASSWORD PROTECTED.
NOTE : ENCRYPTED TEXT HAS TO BE GIVEN BY USER IN CASE OF NO ACCOUNT'''

#FOR MY REFENECE - DATA Fetchall -> List of different records and each column's info in a tuple.
#THANK YOU

#Imports :)
import random
import string
import json
import time

from datetime import date

import textwrap

status = 0


# Mark 1!
mark1 = {}
for i in range(26):
  mark1[chr(65 + i)] = str(i + 1)+" "
  mark1[chr(97 + i)] = str(27 + i)+" "

# ASCII Version!
asciiv = {}
for i in range(65, 91):
        asciiv[chr(i)] = str(i)+" "
for j in range(97, 123):
        asciiv[chr(j)] = str(j)+" "

# Mark 2!
mark2 = {}
for i in range(26):
        mark2[chr(65 + i)] = str(26 - i)+" "
        mark2[chr(97 + i)] = str(52 - i)+" "

# Mark 3!
mark3 = {}
for i in range(26):
        mark3[chr(65 + i)] = str(2 * (i + 1))+" "
        mark3[chr(97 + i)] = str((2 * i) + 1)+" "

# Mark 4!
mark4 = {}
for i in range(26):
        mark4[chr(65 + i)] = chr(90 - i)+" "
        mark4[chr(97 + i)] = chr(122 - i)+" "


#DOTENV_CONNECTION
from dotenv import load_dotenv
import os
load_dotenv()

import mysql.connector as sql

#DB_CONNECTIONNN
mycon = sql.connect(host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    database=os.getenv("DB_NAME"),
                    password=os.getenv("DB_PASSWORD"))

if mycon.is_connected():
    print("Connection's strong YAY!")
else:
    print("Not connected.")

cursor = mycon.cursor()





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

def exit():
    print("Thank you so much for using Privournal, Have a nice day!")
    print("Byeeeeee :)")
    print()

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


        global user_id
        user_id = (j_data[0][1])
        print("User_ID is",user_id)
        print()
        print()


        global j_id
        j_id = []
        for i in range(len(j_data)):
            j_id.append((j_data[i][0]))
        print("Journal_IDs : ", j_id)
        print()
        print()

        global j_name
        j_name = []
        for i in range(len(j_data)):
            j_name.append(j_data[i][2])
        print("Journal_Names : ",j_name)
        print()
        print()


        global en_key
        en_key = []
        for i in range(len(j_data)):
            en_key.append(j_data[i][3])
        for j in en_key:
            print("Encryption Key : ",textwrap.fill(j, width=80))
            print()
            print()


        global en_date
        en_date = []
        for i in range(len(j_data)):
            en_date.append(j_data[i][4])
        for j in en_date:
            print("Date Created : ",j)
            print()


        which_j()

        print("Starting Decryption!")
        print()

        og_dict_key = json.loads(KEY)

        RAW = input("Enter the raw encrypted journal : ")
        RAWlist = RAW.split(" ")

        tempstore = []
        for i in RAWlist:
            for key, value in og_dict_key.items():
                if i == "":
                    tempstore.append(" ")
                    break

                elif not i.isalnum():
                    tempstore.append(i)
                    break

                elif (str(i) + " ") == value:
                    tempstore.append(key)
                    break
                else:
                    continue

        decrypted = "".join(tempstore)

        print()
        print("Decrypted Successfully!")
        print("Here's your Journal --> ", decrypted)
        print()
        print()
        print("You will be redirect to Menu in 10 seconds :) ")
        print()
        time.sleep(1)
        print("You can copy your decrypted journal and save it somewhere safe!")
        print()
        time.sleep(10)
        Menu()

    elif status != 1:
        Ch3 = input("Do you have an Account on Privournal? (Y/N) : ")
        print()

        if Ch3 == "y" or Ch3 == "Y":
            login()
        elif Ch3 == "n" or Ch3 == "N":

            print()
            print('''
                    1. Basic Encryption
                    2. Advanced Encryption 
                                        ''')
            print()

            Ch4 = int(input("Which Encryption does your Journal have? (1 OR 2) : "))
            print()
            if Ch4 == 1:

                    global RAW2
                    RAW2 = input("Enter the Encrypted text : ")
                    delist = []
                    global Ch5
                    print()
                    print()
                    print("1. Mark 1 (A to Z from 1 to 26 respectively, and a to z from 27 to 52 respectively.)")
                    print("2. ASCII Version")
                    print("3. Mark 2 (A to Z from 26 to 1 respectively, and a to z from 52 to 26 respectively.)")
                    print(
                        "4. Mark 3 (A to Z from 2 to 52 respectively, even numbers only. \nAnd a to z from 1 to 51, odd numbers only.)")
                    print("5. Mark 4 (A to Z from Z to A respectively and a to z from z to a respectively.)")
                    print()
                    Ch5 = input("Which one out of these? (1-5) : ")
                    print()
                    print("Decrypting...")
                    print()
                    time.sleep(3)
                    basicDe()

            elif Ch4 == 2:

                Ch6 = input("Do you have the Encryption Key? (Y/N) : ")

                if Ch6 == "y" or Ch6 == "Y":
                    given_dict_key = input("Enter the Encryption Key please : ")

                    RAW = input("Enter the raw encrypted journal : ")
                    RAWlist = RAW.split(" ")

                    tempstore = []
                    for i in RAWlist:
                        for key, value in given_dict_key.items():
                            if i == "":
                                tempstore.append(" ")
                                break

                            elif not i.isalnum():
                                tempstore.append(i)
                                break

                            elif (str(i) + " ") == value:
                                tempstore.append(key)
                                break

                            else:
                                continue

                    decrypted = "".join(tempstore)
                    print()
                    print()
                    print("Decrypted!")
                    print("Here's your Journal --> ", decrypted)
                    print()
                    print()
                    print("You will be redirect to Menu in 15 seconds :) ")
                    print()
                    time.sleep(1)
                    print("You can copy your decrypted journal and save it somewhere safe!")
                    print("Thank you for using Privournal!")
                    print()
                    time.sleep(15)
                    Menu()



                elif Ch6 == "n" or Ch6 == "N":
                    print("We're sorry, we cannot Decryption without the Key. \nBe sure to make an account on Privournal if you have trouble keeping Keys.")
                    print()
                    print("You will be redirected to the Menu Shortly.")
                    print()
                    time.sleep(3)
                    Menu()


                else:
                    print("Invalid choice!")
                    print()
                    De()


def login():
        global username
        global pswd
        username1 = input("Enter Username : ")
        pswd1 = input("Enter Password : ")

        cursor.execute(
            "SELECT password FROM user_records WHERE username = %s",
            (username1,)
        )

        fetchedetails = cursor.fetchall()

        if fetchedetails == []:
            print()
            print("No such Username found in our database!")
        else:

            if pswd1 == fetchedetails[0][0]:
                print()
                print("Logged in Successfully!")

                cursor.execute(
                    "SELECT * FROM user_records WHERE username = %s",
                    (username1,)
                )

                fetchedetails = cursor.fetchall()

                global user_id
                global username
                global pswd
                global email
                global account_created

                user_id = fetchedetails[0][0]
                name = fetchedetails[0][1]
                username = fetchedetails[0][2]
                email = fetchedetails[0][3]
                account_created = fetchedetails[0][4]
                password = fetchedetails[0][5]
                print()
                print()
                global status
                status = 1
                print()
                print("You will be redirected to the menu shortly :) ")
                time.sleep(1)
                Menu()



            else:
                print()
                print("Wrong Password.")
                print()
                exch = int(input("Exit or Login again? (1 OR 2) : "))
                if exch == 1:
                    exit()
                elif exch == 2:
                    login()
                else:
                    print("Invalid Choice!")


def basicDe():

    dakey = {}

    if Ch5 == 1:
        dakey = mark1
    elif Ch5 == 2:
        dakey = asciiv
    elif Ch5 == 3:
        dakey = mark2
    elif Ch5 == 4:
        dakey = mark3
    elif Ch5 == 5:
        dakey = mark4
    else:

        print("Invalid Option!")

    delist = []
    for i in RAW2:
        if i in dakey:
            for keys, values in dakey.items():
                if keys == i:
                    delist.append(values)
                else:
                    continue
        else:
            delist.append(i)

    decrypted = "".join(delist)
    print("Succesfully Decrypted!")
    print()
    print()
    time.sleep(1)
    print("Here's you Decrypted text --> ",decrypted)
    print()
    print("Thank you for using Privournal!")
    print("Be sure to make an account for smoother experience in the future :) ")
    print()
    print("You will be redirected to the Menu in 10 seconds. ")
    print()
    time.sleep(10)
    Menu()


def En():
    print("Choose Mode of Encryption : ")
    print("1. Basic (Weak but holds well if you have dummies tryna read your Journal lol)")
    print("2. Advanced (Includes Swiption - Really strong encryption, \nholds well even if you have prodigies trying to read your Journal.")
    print()
    print()
    ch2 = int(input("Which one? (1 OR 2) : "))

    if ch2 == 1:
        print()
        print("Welcome to Basic Encryption!")
        print()
        print("1. Mark 1 (A to Z from 1 to 26 respectively, and a to z from 27 to 52 respectively.)")
        print("2. ASCII Version")
        print("3. Mark 2 (A to Z from 26 to 1 respectively, and a to z from 52 to 26 respectively.)")
        print("4. Mark 3 (A to Z from 2 to 52 respectively, even numbers only. \nAnd a to z from 1 to 51, odd numbers only.)")
        print("5. Mark 4 (A to Z from Z to A respectively and a to z from z to a respectively.)")
        print()

        global Ch5
        Ch5 = int(input("Choose one of these (1-5) : "))

        if status != 1:

            Ch8 = input("Do you have an Account? (Y/N) : ")

            if Ch8 == "Y" or Ch8 == "y":
                print("You'll be redirected to Login page, please complete the login first :) ")
                time.sleep(3)
                login()

            elif Ch8 == "N" or Ch8 == "n":
                print()
                Ch7 = input("Do you want to save encryption details on our database, \nfor future decryptions and referencing records? (Y/N) : ")

                if Ch7 == "Y" or Ch7 == "y":
                    signup()

                elif Ch7 == "N" or Ch7 == "n":
                    print()
                    print("Please have all the encryption details saved with you then!")
                    print()

                    if Ch5 == 1:
                        dakey = mark1
                    elif Ch5 == 2:
                        dakey = asciiv
                    elif Ch5 == 3:
                        dakey = mark2
                    elif Ch5 == 4:
                        dakey = mark3
                    elif Ch5 == 5:
                        dakey = mark4
                    else:
                        print("Invalid Option!")

                    j = input("Please feed the Journal for Encryption : ")
                    print()
                    journal = list(j)
                    delist = []

                    for i in journal:
                        if i in dakey:
                            for keys, values in dakey.items():
                                if keys == i:
                                    delist.append(values)
                                else:
                                    continue
                        else:
                            delist.append(i)

                    encrypted = "".join(delist)
                    print("Succesfully Encrypted!")
                    time.sleep(1)
                    print()
                    print()
                    print("Here's you Encrypted text --> ",encrypted)
                    print()
                    print("Thank you for using Privournal!")
                    print("Be sure to make an account for smoother experience in future :) ")
                    print("You will be redirected to the Menu in 10 seconds")
                    print()
                    time.sleep(10)
                    Menu()

                else:
                    print("Invalid input!")
                    AdvEn()

        else:

            j = input("Please feed the Journal for Encryption : ")
            journal = list(j)
            jname = input("Please name your Journal : ")

            if Ch5 == 1:
                dakey = mark1
            elif Ch5 == 2:
                dakey = asciiv
            elif Ch5 == 3:
                dakey = mark2
            elif Ch5 == 4:
                dakey = mark3
            elif Ch5 == 5:
                dakey = mark4
            else:
                print("Invalid Option!")

            delist = []
            for i in journal:
                if i in dakey:
                    for keys, values in dakey.items():
                        if keys == i:
                            delist.append(values)
                        else:
                            continue
                else:
                    delist.append(i)

            encrypted = "".join(delist)
            print("Succesfully Encrypted! ")
            time.sleep(1)

            journal_name = jname

            encryption_key = json.dumps(dakey)
            encryption_date = date.today()

            cursor.execute(
                """
                INSERT INTO journal_details
                (user_id, journal_name, encryption_key, encryption_date)
                VALUES (%s, %s, %s, %s)
                """,
                (user_id, journal_name, encryption_key, encryption_date))
            mycon.commit()

            print()
            print()
            print("Here's you Encrypted Journal --> ",encrypted)
            print()
            print("Thank you for using Privournal!")
            print("You'll be redirected to the menu.")

            print()
            print()
            time.sleep(5)
            Menu()


    elif ch2 == 2:
        print("Advanced Encryption it is then!")
        print()
        ask = input("Do you want to enable Swiption for a stronger Encryption? (Y/N) : ")
        print()

        if ask == "Y" or ask == "y":
            m = 1
            print("swiptionEn() in progress.")
            # IN PROGRESS

        elif ask == "N" or ask == "n":
            m = 2
            AdvEn()

        else:
            print("Invalid choice")
            En()


def AdvEn():

    if status != 1:
        print()
        Ch8 = input("Do you have an Account? (Y/N) : ")
        print()

        if Ch8 == "Y" or Ch8 == "y":
            print("You'll be redirected to Login page, please complete the login first :) ")
            time.sleep(3)
            login()

        elif Ch8 == "N" or Ch8 == "n":

            print("Do you want to save encryption details on our database, \nfor future decryptions and referencing records?")
            Ch7 = input("Do you want to save encryption details on our database, \nfor future decryptions and referencing records? (Y/N) : ")

            if Ch7 == "Y" or Ch7 == "y":
                signup()

            elif Ch7 == "N" or Ch7 == "n":
                print()
                print("Please have all the encryption details saved with you then!")

                enlist = []
                cover_dict = {}

                journal = input("Please feed the Journal for Encryption : ")
                jname = input("Please name your Journal : ")

                if not journal:
                    print("Empty Journal!")
                    feed()
                else:
                    print("Journal Uploaded!")

                print("Choose cover for each letter man!")
                print()

                trackHEH = []

                for x in journal:
                    if x.isalpha() and x not in cover_dict:
                        cover()

                    elif x in cover_dict:
                        cover = cover_dict[x]
                        enlist.append(cover)
                    else:
                        enlist.append(x)

                finalenlist = "".join(enlist)
                print()
                print("Successfully Encrypted!")
                print()
                print("Here's the encrypted Journal --> ",finalenlist)
                print()
                print()
                print("You'll be redirected to the a new page.")
                print()
                print()
                time.sleep(5)
                Menu()

            else:
                print("Invalid input!")
                AdvEn()

    else:
        enlist = []
        cover_dict = {}

        journal = input("Please feed the Journal for Encryption : ")
        jname = input("Please name your Journal : ")

        if not journal:
            print("Empty Journal!")
            feed()
        else:
            print("Journal Uploaded!")

        print("Choose cover for each letter man!")
        print()

        for x in journal:
            if x.isalpha() and x not in cover_dict:
                print("What should be the cover for", x, "?")
                cover = input("Cover = ")
                cover = cover + " "
                cover_dict[x] = cover
                enlist.append(cover)
            elif x in cover_dict:
                cover = cover_dict[x]
                enlist.append(cover)
            else:
                enlist.append(x)

        finalenlist = "".join(enlist)

        journal_name = jname

        encryption_key = json.dumps(cover_dict)
        encryption_date = date.today()

        cursor.execute(
            """
            INSERT INTO journal_details
            (user_id, journal_name, encryption_key, encryption_date)
            VALUES (%s, %s, %s, %s)
            """,
            (user_id, journal_name, encryption_key, encryption_date))
        mycon.commit()

        print()
        print("Successfully Encrypted!")
        print()
        print("Here's the encrypted Journal --> ", finalenlist)
        print()
        print()
        print("You'll be redirected to the a new page.")
        print()
        print()
        time.sleep(5)
        Menu()

def signup():

    cursor.execute("SELECT COUNT(DISTINCT username) FROM user_records")
    global user_id
    user_id = cursor.fetchone()[0]

    tusername = input("Set a username : ")
    print()
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
    print()

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
                INSERT INTO user_records
                (user_id, first_name, username, email, account_created, password)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (user_id, name, username, email, account_created, password))
            mycon.commit()
            print()
            print("Account made succesfully!")
            global status
            status = 1
            print()
            print("You'll be redirected to the menu, you can now start Encrypting and Decrypting without hassle! ")
            time.sleep(1)
            print()
            Menu()


        else:
            print("The passwords don't match.")
            signup()

def which_j():
 Ch = int(input("Which Journal do you want to Decrypt? (Enter Journal_ID) : "))
 print()

 if Ch not in j_id:
            print("Journal not found. Check the ID again!")
            which_j()

 for i in range(len(j_id)):

        if j_id[i] == Ch:
                global KEY
                KEY = en_key[i]
        else:
                continue
 def cover():
     print("What should be the cover for", x, "?")
     global cover
     cover = input("Cover = ")
     if cover not in trackHEH:
         print()
         cover = cover + " "
         cover_dict[x] = cover
         enlist.append(cover)
         trackHEH.append(cover)
     else:
         print("2 letters can't have the same cover na! ")
         cover()

start()

cursor.close()
mycon.close()



