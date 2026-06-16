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
import textwrap


mark1 = {}
for i in range(26):
  mark1[chr(65 + i)] = str(i + 1)+" "
  mark1[chr(97 + i)] = str(27 + i)+" "

# ASCII Version!
asciiv = {}
for i in range(65, 91):
        asciiv[chr(i)] = str(i)+" "
for j in range(97, 123):
        asciiv[chr(i)] = str(i)+" "

# Mark 2
mark2 = {}
for i in range(26):
        mark2[chr(65 + i)] = str(26 - i)+" "
        mark2[chr(97 + i)] = str(52 - i)+" "

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


        global user_id
        user_id = (j_data[0][1])
        print("User_ID is",user_id)


        global j_id
        j_id = []
        for i in range(len(j_data)):
            j_id.append((j_data[i][0]))
            print("Journal_ID",i+1, j_id)

        global j_name
        j_name = []
        for i in range(len(j_data)):
            j_name.append(j_data[i][2])
            print("Journal_Name", i + 1,j_name)


        global en_key
        en_key = []
        for i in range(len(j_data)):
            en_key.append(j_data[i][3])
            print("Encryption_Key", i + 1,en_key)


        global en_date
        en_date = []
        for i in range(len(j_data)):
            en_date.append(j_data[i][4])
            print("Encryption_Date",i + 1,en_date)

            which_j()

            print("Starting Decryption!")

            og_dict_key = json.loads(KEY)
            RAW = input("Enter the raw encrypted journal : ")
            RAWlst = RAW.split(" ")

            tempstore = []
            for i in RAWlst:
                for key, value in og_dict_key.items():
                    if i == "":
                        tempstore.append(" ")
                        break

                    elif not i.isalnum():
                        tempstore.append(i)
                        break

                    elif (str(i)+" ") == value:
                        tempstore.append(key)
                        break
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

            Ch4 = int(input("Which Encryption does your Journal have? (1 OR 2) : "))
            if Ch4 == 1:

                Ch10 = input("Do you have the Encryption Key? (Y/N) : ")

                if Ch10 == "y" or Ch10 == "Y":


                    print()
                    print("1. Mark 1 (A to Z from 1 to 26 respectively, and a to z from 27 to 52 respectively.)")
                    print("2. ASCII Version")
                    print("3. Mark 2 (A to Z from 26 to 1 respectively, and a to z from 52 to 26 respectively.)")
                    print(
                        "4. Mark 3 (A to Z from 2 to 52 respectively, even numbers only. And a to z from 1 to 51, odd numbers only.)")
                    print("5. Mark 4 (A to Z from Z to A respectively and a to z from z to a respectively.)")
                    print()
                    print()

                    RAW = input("Enter the Encrypted text : ")
                    delist = []
                    Ch5 = input("Which one out of these? : ")
                    print("Decrypting...")
                    time.sleep(3)
                    basicEn()



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

                    RAW = input("Enter the raw encrypted journal : ")
                    RAWlst = RAW.split(" ")

                    tempstore = []
                    for i in RAWlst:
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


                else:
                    print("Invalid choice!")
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

        if fetchedetails == None:
            print("No such Username in our database found!")
        else:

            if pswd1 == fetchedetails[0][0]:
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
                print("You will be redirected to the menu shortly.")
                time.sleep(1)
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


def basicDe():



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
    for i in RAW:
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
    time.sleep(1)
    print()
    print(decrypted)
    print()
    print("Thank you for using Privournal!")
    print("Be sure to make an account for smoother experience in future :)")
    print("You will be redirected to the Menu in 10 seconds")
    time.sleep(10)
    Menu()



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
        print()
        print("1. Mark 1 (A to Z from 1 to 26 respectively, and a to z from 27 to 52 respectively.)")
        print("2. ASCII Version")
        print("3. Mark 2 (A to Z from 26 to 1 respectively, and a to z from 52 to 26 respectively.)")
        print("4. Mark 3 (A to Z from 2 to 52 respectively, even numbers only. And a to z from 1 to 51, odd numbers only.)")
        print("5. Mark 4 (A to Z from Z to A respectively and a to z from z to a respectively.)")

        global Ch5
        Ch5 = int(input("Choose one of these : "))

        if status != 1:

            Ch8 = input("Do you have an Account? (Y/N) : ")

            if Ch8 == "Y" or Ch8 == "y":
                print("You'll be redirected to Login page, please complete the login first :) ")
                time.sleep(3)
                login()

            elif Ch8 == "N" or Ch8 == "n":

                print(
                    "Do you want to save encryption details on our database for future decryptions and referencing records?")
                Ch7 = input("(Y/N) : ")

                if Ch7 == "Y" or Ch7 == "y":
                    signup()

                elif Ch7 == "N" or Ch7 == "n":
                    print("Please have all the encryption details saved with you then!")

                    RAW = input("Please feed the Journal for Encryption : ")

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
                    for i in RAW:
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
                    time.sleep(1)
                    print()
                    print(decrypted)
                    print()
                    print("Thank you for using Privournal!")
                    print("Be sure to make an account for smoother experience in future :)")
                    print("You will be redirected to the Menu in 10 seconds")
                    time.sleep(10)
                    Menu()

                else:
                    print("Invalid input!")
                    AdvEn()

        else:

            RAW = input("Please feed the Journal for Encryption : ")
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
            for i in RAW:
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
            print("Here's the encrypted Journal : ")
            print()
            print(decrypted)
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
                        print("What should be the cover for",x,"?")
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
                print()
                print("Successfully Encrypted!")
                print()
                print("Here's the encrypted Journal : ")
                print("--->", finalenlist)
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
        print()
        print("Successfully Encrypted!")


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
        print("Here's the encrypted Journal : ")
        print()
        print(finalenlist)
        print()
        print("Thank you for using Privournal!")
        print("You'll be redirected to the menu.")

        print()
        print()
        time.sleep(5)
        Menu()

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
                INSERT INTO user_records
                (user_id, first_name, username, email, account_created, password)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (user_id, name, username, email, account_created, password))
            mycon.commit()
            print()
            print("Account made succesfully!")
            print()
            print("You'll be redirected to the menu, you can now start Encrypting and Decrypting without hassle! ")
            time.sleep(3)
            print()
            Menu()


        else:
            print("The passwords don't match.")
            signup()

def which_j():
 Ch = int(input("Which Journal do you want to Decrypt? (Enter Journal_ID) : "))

 if Ch not in j_id:
            print("Journal not found. Check the ID again!")
            which_j()

 for i in range(len(j_id)):

        if j_id[i] == Ch:
                global KEY
                KEY = en_key[i]
        else:
                continue

start()

cursor.close()
mycon.close()



