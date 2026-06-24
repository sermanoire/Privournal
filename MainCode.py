''' PRIVOURNAL STORES NO DATA EXCEPT ACCOUNT DETAILS.
ECRYPTIONS AND DECRYPTIONS PURELY DONE BY LOGIC AND ENCRYPTION DATA IN USER'S ACCOUNT.
ENCRYPTION DATA CAN BE ALSO PASSWORD PROTECTED.
NOTE : ENCRYPTED TEXT HAS TO BE GIVEN BY USER IN CASE OF NO ACCOUNT'''

# FOR MY REFENECE - DATA Fetchall -> List of different records and each column's info in a tuple.
# THANK YOU
# Imports!

import random
import string
import json
import time
import os

from datetime import date
import textwrap

# Making the pretty format!
def note():
    print(""" 
    Welcome to Privournal! 
    
    PRIVOURNAL STORES NO DATA EXCEPT ACCOUNT DETAILS LIKE ENCRYPTION KEY.
    ECRYPTIONS AND DECRYPTIONS PURELY DONE BY LOGIC AND ENCRYPTION DATA IN USER'S ACCOUNT.
    
    NOTE : ENCRYPTED TEXT AND THE KEY HAS TO BE GIVEN BY USER IN CASE OF NO ACCOUNT!
              
    Also, for swiption feature having an account is mandatory!
    
    And to give you a sigh of relief, this is so secure that even if someone has the Key,
    they CANNOT get your journal IF they don't have the raw encrypted one. :)
    
""")

    time.sleep(3)
    clear()

def clear():
    print("\n" * 100)

def divider():
    print("─" * len(sec))

def section(title):
    print()
    print()

    global sec
    sec = "-" * 50 + title + "-" * 50
    print(sec)

def show_output(label, text):
    divider()
    print(f"{label} :")
    print()
    print(text)
    print()
    divider()


# Kinda like the main code!
status = 0

# Mark 1!
mark1 = {}
for i in range(26):
    mark1[chr(65 + i)] = ""
    mark1[chr(97 + i)] = ""

# ASCII Version!
asciiv = {}
for i in range(65, 91):
    asciiv[chr(i)] = str(i) + " "
for j in range(97, 123):
    asciiv[chr(j)] = str(j) + " "

# Mark 2!
mark2 = {}
for i in range(26):
    mark2[chr(65 + i)] = str(26 - i) + " "
    mark2[chr(97 + i)] = str(52 - i) + " "

# Mark 3!
mark3 = {}
for i in range(26):
    mark3[chr(65 + i)] = str(2 * (i + 1)) + " "
    mark3[chr(97 + i)] = str((2 * i) + 1) + " "

# Mark 4!
mark4 = {}
for i in range(26):
    mark4[chr(65 + i)] = chr(90 - i) + " "
    mark4[chr(97 + i)] = chr(122 - i) + " "

# DB_CONNECTION
import sqlite3
from pathlib import Path

def connect_db():

    db_path = Path.home() / ".privournal"
    db_path.mkdir(exist_ok=True)
    mycon = sqlite3.connect(db_path / "privournal.db")
    cursor = mycon.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS user_records (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    username TEXT UNIQUE,
    email TEXT,
    account_created TEXT,
    password TEXT
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS journal_details (
    journal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    journal_name TEXT,
    encryption_key TEXT,
    encryption_date TEXT
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS swiption_details (
    swiption_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    journal_name TEXT,
    encryption_date TEXT,
    encryption_key TEXT,
    life INTEGER
)
""")
    mycon.commit()
    return mycon, cursor

def start():
    global mycon, cursor
    mycon, cursor = connect_db()
    section("WELCOME!")
    banner()
    print()
    print()
    time.sleep(3)
    Menu()

def Menu():
    clear()
    section("MENU")
    print("What would you like to do today?")
    print()
    print("1. Encrypt a Journal Entry")
    print("2. Decrypt a Journal Entry")
    print("3. Guide")
    print("4. Exit")
    divider()
    raw = input("1 OR 2 OR 3 OR 4 : ")
    try:
        ch = int(raw)
    except ValueError:
        print()
        print("Invalid Choice! Please enter a number.")
        print()
        time.sleep(1)
        Menu()
        return
    print()
    print()

    if ch == 1:
        En()
    elif ch == 2:
        De()
    elif ch == 3:
        guide()
    elif ch ==4:
        exit()
    else:
        print("Invalid Choice!")
        print()
        time.sleep(1)
        Menu()


def exit():
    clear()
    section("GOODBYE")
    print("Thank you so much for using Privournal, Have a nice day!")
    print("Byeeeeee :)")
    print()


def De():

    clear()
    section("DECRYPTION")
    print()

    if status == 1:

        CH = input("Do you want to Decrypt a Swiption-based Journal? (y/n) : ")
        print()
        print()

        if CH == "y" or CH == "Y":
            SwipDe()
        elif CH == "n" or CH == "N":
            cursor.execute('''
                    SELECT jd.*
                    FROM journal_details jd
                    JOIN user_records ur
                    ON jd.user_id = ur.user_id
                    WHERE ur.username = ?
                    ''', (username,))

            j_data = cursor.fetchall()  # Fetching Journal Data

            global user_id
            user_id = (j_data[0][1])
            print("User_ID is", user_id)
            print()

            global j_id
            j_id = []
            for i in range(len(j_data)):
                j_id.append((j_data[i][0]))
            print("Journal_IDs : ", j_id)
            print()

            global j_name
            j_name = []
            for i in range(len(j_data)):
                j_name.append(j_data[i][2])
            print("Journal_Names : ", j_name)
            print()

            global en_key
            en_key = []
            for i in range(len(j_data)):
                en_key.append(j_data[i][3])
            for t in en_key:
                print("Encryption Key : ", t)
                print()

            global en_date
            en_date = []
            for i in range(len(j_data)):
                en_date.append(j_data[i][4])
            for t in en_date:
                print("Date Created : ", t)
                print()

            which_j()

            print("Starting Decryption!")
            print()

            og_dict_key = json.loads(EN_KEY)

            RAW = input("Enter the raw encrypted journal : ")
            global RAWlist
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
            print("Decrypting...")
            print()
            print("Decrypted Successfully!")
            print()
            print()
            time.sleep(1)
            clear()
            show_output("Here's your Journal", decrypted)
            print()
            print("You can copy your decrypted journal and save it somewhere safe!")
            print()
            time.sleep(4)
            Menu()

        else:
            print("Invalid Choice!")
            print()
            time.sleep(1)
            Menu()

    else:
        Ch2 = input("Do you have an Account on Privournal? (y/n) : ")
        print()

        if Ch2 == "y" or Ch2 == "Y":
            login()
        elif Ch2 == "n" or Ch2 == "N":

            print()
            print('''
1. Basic Encryption
2. Advanced Encryption 
3. Exit
            ''')
            print("Note that to Decrypt a Swiption based journal, you need an account. ")
            print()
            print()

            try:
                Ch3 = int(input("Which Encryption does your Journal have? (1 OR 2) : "))
            except ValueError:
                print()
                print("Invalid Choice! Please enter a number.")
                print()
                time.sleep(1)
                De()
                return
            print()
            if Ch3 == 1:
                print()
                RAW = input("Enter the Encrypted text : ")
                RAWlist = RAW.split(" ")
                print()
                time.sleep(1)
                clear()
                print()

                which_mode()

                time.sleep(1)
                basicDe()

            elif Ch3 == 2:

                Ch5 = input("Do you have the Encryption Key? (y/n) : ")
                print()

                if Ch5 == "y" or Ch5 == "Y":
                    given_dict_key = input("Enter the Encryption Key please : ")
                    try:
                        given_dict_key = json.loads(given_dict_key)
                    except json.decoder.JSONDecodeError:
                        print(
                            "That doesn't look like a valid Encryption Key. Please check and paste it exactly as given.")
                        print()
                        De()
                        return

                    print()
                    RAW = input("Enter the raw encrypted journal : ")
                    print()
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
                    print("Decrypting...")
                    print()
                    print("Decrypted Successfully!")
                    print()
                    print()
                    time.sleep(1)
                    clear()

                    show_output("Here's your Journal", decrypted)
                    print()
                    print()
                    print("You can copy your decrypted journal and save it somewhere safe.")
                    print("Thank you for using Privournal!")
                    print()
                    time.sleep(4)
                    Menu()

                elif Ch5 == "n" or Ch5 == "N":
                    print()
                    print("We're sorry, we cannot Decryption without the Key. \nBe sure to make an account on Privournal if you have trouble keeping Keys.")
                    print()
                    print("You will be redirected to the Menu Shortly.")
                    print()
                    time.sleep(3)
                    Menu()


                else:
                    print("Invalid Choice!")
                    print()
                    time.sleep(1)
                    De()

            elif Ch3 == 3:
                exit()
            else:
                print("Invalid Choice!")
                time.sleep(1)
                De()

def login():
    clear()
    section("LOGIN")
    global username1
    global pswd
    username1 = input("Enter Username : ")
    pswd1 = input("Enter Password : ")

    cursor.execute(
        "SELECT password FROM user_records WHERE username = ?",
        (username1,)
    )

    acc_d = cursor.fetchall()

    if acc_d == []:
        print()
        print("No such Username found in the database!")

    else:
        if pswd1 == acc_d[0][0]:
            print()
            print("Logged in Successfully!")

            cursor.execute(
                "SELECT * FROM user_records WHERE username = ?",
                (username1,)
            )

            acc_d = cursor.fetchall()

            global user_id
            global username
            global password
            global email
            global account_created

            user_id = acc_d[0][0]
            name = acc_d[0][1]
            username = acc_d[0][2]
            email = acc_d[0][3]
            account_created = acc_d[0][4]
            password = acc_d[0][5]

            print()
            print()
            global status
            status = 1
            print()

            time.sleep(1)
            Menu()

        else:
            print()
            print("Wrong Password.")
            print()
            try:
                exch = int(input("Exit or Login again? (1 OR 2) : "))
            except ValueError:
                print("Invalid Choice! Please enter a number.")
                time.sleep(1)
                login()
                return
            if exch == 1:
                exit()
            elif exch == 2:
                login()
            else:
                print("Invalid Choice!")
                print()
                time.sleep(1)
                login()


def basicDe():
    dakey = {}

    if Ch4 == 1:
        dakey = mark1
    elif Ch4 == 2:
        dakey = asciiv
    elif Ch4 == 3:
        dakey = mark2
    elif Ch4 == 4:
        dakey = mark3
    elif Ch4 == 5:
        dakey = mark4
    else:
        print("Invalid Option!")
        basicDe()

    print()
    print("Decrypting...")
    print()

    delist = []

    for i in RAWlist:
        if i == "":
            delist.append(" ")
        else:
            for keys, values in dakey.items():
                if values.strip() == i:
                    delist.append(keys)
                else:
                    continue
            if not i.isalnum() and i != "":
                delist.append(i)

    decrypted = "".join(delist)
    print("Successfully Decrypted!")
    print()
    print()
    time.sleep(1)
    clear()
    show_output("Here's your Journal", decrypted)
    print()
    print("Thank you for using Privournal!")
    print("Be sure to make an account for smoother experience in the future :) ")
    print()
    print()
    time.sleep(4)
    Menu()


def En():
    clear()
    section("ENCRYPTION")

    if status != 1:

        Ch8 = input("Do you have an Account? (y/n) : ")
        print()

        if Ch8 == "Y" or Ch8 == "y":
            print("You'll be redirected to Login page, please complete the login first :) ")
            print()
            time.sleep(1)
            login()

        elif Ch8 == "N" or Ch8 == "n":
            global Ch7
            Ch7 = input("Do you want to make an account? for more ease and referencing records? (y/n) : ")
            print()

            if Ch7 == "Y" or Ch7 == "y":
                signup()

            elif Ch7 == "N" or Ch7 == "n":

                print("Choose Mode of Encryption : ")
                print()
                print("1. Basic (Weak but holds well if you have dummies tryna read your Journal lol)")
                print("2. Advanced (Includes Swiption And Randomised Mode - Really strong encryption, \nholds well even if you have prodigies trying to read your Journal.")
                print()
                print()

                try:
                    Ch6 = int(input("Which one? (1 OR 2) : "))

                except ValueError:
                    print("Invalid Choice!")
                    time.sleep(1)
                    En()
                    return

                if Ch6 == 1:
                    print()
                    print("Welcome to Basic Encryption!")
                    print()
                    print("1. Mark 1 (A to Z from 1 to 26 respectively, and a to z from 27 to 52 respectively.)")
                    print("2. ASCII Version")
                    print("3. Mark 2 (A to Z from 26 to 1 respectively, and a to z from 52 to 26 respectively.)")
                    print("4. Mark 3 (A to Z from 2 to 52 respectively, even numbers only. \nAnd a to z from 1 to 51, odd numbers only.)")
                    print()
                    print("5. Mark 4 (A to Z from Z to A respectively and a to z from z to a respectively.)")
                    print()

                    try:
                        Ch7 = int(input("Which mode? (1-5) "))
                    except ValueError:
                        print("Invalid Choice!")
                        time.sleep(1)
                        En()
                        return

                    if Ch7 == 1:
                        dakey = mark1
                    elif Ch7 == 2:
                        dakey = asciiv
                    elif Ch7 == 3:
                        dakey = mark2
                    elif Ch7 == 4:
                        dakey = mark3
                    elif Ch7 == 5:
                        dakey = mark4
                    else:
                        print("Invalid Option!")

                    global j
                    j = input("Please feed the Journal for Encryption : ")
                    print()
                    print("Encrypting...")
                    time.sleep(1)
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
                    print()
                    print("Succesfully Encrypted!")
                    print()
                    print()
                    time.sleep(1)
                    clear()
                    show_output("Here's your Encrypted text", encrypted)
                    print()
                    print("Please copy this and paste it somewhere, you'll need it while decrypting.")
                    print()
                    print("Thank you for using Privournal! ")
                    print("Be sure to make an account for smoother experience in future :) ")
                    print()
                    print("You will be redirected to the menu shortly.")
                    time.sleep(8)
                    clear()

                    Menu()

                elif Ch6 == 2:
                    print()
                    print()
                    divider()
                    print("Advanced Encryption it is then!")
                    print()
                    print()

                    swiption = input("Do you want to enable Swiption for a stronger Encryption? (y/n) : ")

                    print()
                    print()
                    if swiption == "Y" or swiption == "y":
                        Swiption()

                    elif swiption == "N" or swiption == "n":
                        AdvEn()

                    else:
                        print("Invalid Choice!")
                        print()
                        time.sleep(1)
                        En()

                else:
                    print("Invalid input!")
                    time.sleep(1)
                    En()
            else:
                print("Invalid input!")
                time.sleep(1)
                En()
        else:
            print("Invalid Choice!")
            time.sleep(1)
            En()

    else:

        print("Choose Mode of Encryption : ")
        print()
        print("1. Basic (Weak but holds well if you have dummies tryna read your Journal lol)")
        print("2. Advanced (Includes Swiption And Randomised Mode - Really strong encryption, \nholds well even if you have prodigies trying to read your Journal.")
        print()
        print()

        try:
            Ch6 = int(input("Which one? (1 OR 2) : "))
        except ValueError:
            print("Invalid Choice!")
            time.sleep(1)
            En()
            return

        if Ch6 == 1:
            print()
            print("Welcome to Basic Encryption!")
            print()
            print("1. Mark 1 (A to Z from 1 to 26 respectively, and a to z from 27 to 52 respectively.)")
            print("2. ASCII Version")
            print("3. Mark 2 (A to Z from 26 to 1 respectively, and a to z from 52 to 26 respectively.)")
            print(
                "4. Mark 3 (A to Z from 2 to 52 respectively, even numbers only. \nAnd a to z from 1 to 51, odd numbers only.)")
            print()
            print("5. Mark 4 (A to Z from Z to A respectively and a to z from z to a respectively.)")
            print()

            try:
                Ch7 = int(input("Choose one of these (1-5) : "))
            except ValueError:
                print("Invalid Choice! Please enter a number.")
                time.sleep(1)
                En()
                return
            print()

            j = input("Please feed the Journal for Encryption : ")
            print()
            journal = list(j)
            print()

            j_name = input("Please name your Journal : ")

            if Ch7 == 1:
                dakey = mark1
            elif Ch7 == 2:
                dakey = asciiv
            elif Ch7 == 3:
                dakey = mark2
            elif Ch7 == 4:
                dakey = mark3
            elif Ch7 == 5:
                dakey = mark4
            else:
                print("Invalid Option!")

            print()
            print("Encrypting...")
            time.sleep(1)
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
            print()

            journal_name = j_name
            encryption_key = json.dumps(dakey)
            encryption_date = str(date.today())

            cursor.execute(
                """
                INSERT INTO journal_details
                (user_id, journal_name, encryption_key, encryption_date)
                VALUES (?, ?, ?, ?)
                """,
                (user_id, journal_name, encryption_key, encryption_date))

            mycon.commit()
            print()
            print("Successfully Encrypted!")
            print()
            print("Please copy this and paste it somewhere, you'll need it while decrypting!")
            print()
            print()
            time.sleep(1)
            clear()
            show_output("Here's your Encrypted text", encrypted)
            print()
            print("Thank you for using Privournal!")
            print("You'll be redirected to the menu shortly.")
            print()
            print()

            time.sleep(8)
            Menu()

        elif Ch6 == 2:
            print()
            print()
            print("Advanced Encryption it is then!")
            print()
            print()

            swiption = input("Do you want to enable Swiption for a stronger Encryption? (y/n) : ")

            print()
            if swiption == "Y" or swiption == "y":
                Swiption()

            elif swiption == "N" or swiption == "n":
                AdvEn()

            else:
                print("Invalid Choice! Please enter a number.")
                print()
                time.sleep(1)
                En()
        else:
            print("Invalid input!")
            AdvEn()

def AdvEn():
    global journal
    global enlist

    Ch_rand = input("Do you want to enable Randomised Encryption for more ease and security? (y/n) ")
    print()

    if Ch_rand == "y" or Ch_rand == "Y":
        AdvRand()

    elif Ch_rand == "n" or Ch_rand == "N":
        if status != 1:

            enlist = []
            global cover_dict
            cover_dict = {}

            feed()

            if not journal:
                print("Empty Journal!")
                feed()
            else:
                print("Journal Uploaded!")
                time.sleep(1)
                clear()

            print("Choose cover for each letter!")
            print()

            global trackHEH
            trackHEH = []

            global x

            for x in journal:
                if x.isalpha() and x not in cover_dict:
                    coverr()

                elif x in cover_dict:
                    cover = cover_dict[x]
                    enlist.append(cover)
                    trackHEH.append(cover)
                else:
                    enlist.append(x)

            print()
            print("Encrypting...")
            time.sleep(1)
            finalenlist = "".join(enlist)
            print()
            print("Successfully Encrypted!")
            print()
            time.sleep(1)
            clear()
            show_output("Here's the encrypted Journal", finalenlist)
            print()
            print("Please copy this and paste it somewhere, you'll need it while decrypting!")
            print()
            print()
            print("AND Here's the Encryption Key : ")
            print(json.dumps(cover_dict))
            print()
            print("Please copy this key too! It's Important! Since you don't have an account.")
            print()
            print("You'll be redirected the menu shortly in 10 seconds.")
            print()
            print()
            time.sleep(10)
            Menu()

        else:

            enlist = []

            cover_dict = {}

            journal = input("Please feed the Journal for Encryption : ")
            print()
            j_name = input("Please name your Journal : ")
            print()
            print()

            if not journal:
                print("Empty Journal!")
                feed()
            else:
                print("Journal Uploaded!")

            print("Choose cover for each letter!")
            print()

            for x in journal:
                if x.isalpha() and x not in cover_dict:
                    print("What should be the cover for", x, "?")
                    print()
                    cover = input("Cover = ")
                    cover = cover + " "
                    cover_dict[x] = cover
                    enlist.append(cover)
                elif x in cover_dict:
                    cover = cover_dict[x]
                    enlist.append(cover)
                else:
                    enlist.append(x)

            print()
            print("Encrypting...")
            time.sleep(1)
            finalenlist = "".join(enlist)

            journal_name = j_name

            encryption_key = json.dumps(cover_dict)
            encryption_date = str(date.today())

            cursor.execute(
                """
                INSERT INTO journal_details
                (user_id, journal_name, encryption_key, encryption_date)
                VALUES (?, ?, ?, ?)
                """,
                (user_id, journal_name, encryption_key, encryption_date))
            mycon.commit()

            print()
            print("Successfully Encrypted!")
            print()
            print()
            time.sleep(1)
            clear()
            show_output("Here's your Encrypted text", finalenlist)
            print()
            print("Please copy this and paste it somewhere, you'll need it while decrypting!")
            print()
            print("You'll be redirected to the menu shortly.")
            print()
            print()
            time.sleep(8)
            Menu()

    else:
        print("Invalid input!")
        AdvEn()

def feed():
    global journal
    global j_name
    journal = input("Please feed the Journal for Encryption : ")
    print()
    j_name = input("Please name your Journal : ")


def coverr():
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
        print("2 letters can't have the same cover hon! ")
        coverr()

def signup():
    clear()
    section("SIGN UP")
    print()
    cursor.execute("SELECT COALESCE(MAX(user_id), 0) + 1 FROM user_records")
    global user_id
    user_id = cursor.fetchone()[0]

    tusername = input("Set a username : ")
    print()
    if len(tusername) > 16:
        print("Invalid! It should be at most 16 characters.")
        print()
        print()
        time.sleep(1)
        signup()

    elif " " in tusername:
        print("Spaces not allowed!")
        print()
        print()
        time.sleep(1)
        signup()

    elif len(tusername) < 6:
        print("Should be atleast 6 characters long!")
        print()
        print()
        time.sleep(1)
        signup()

    else:
        global username
        username = tusername

    tpswd = input("Set a password : ")
    print()

    if len(tpswd) > 16:
        print("Invalid! It should be at most 18 characters.")
        print()
        print()
        time.sleep(1)
        signup()

    elif " " in tpswd:
        print("Spaces not allowed!")
        print()
        print()
        time.sleep(1)
        signup()

    elif len(tpswd) < 8:
        print("Should be atleast 8 characters long!")
        print()
        print()
        time.sleep(1)
        signup()

    elif tpswd == username:
        print("Username and password cannot be same!")
        time.sleep(1)
        signup()

    else:
        t_conf_pswd = input("Confrim password : ")
        print()

        if t_conf_pswd == tpswd:
            password = tpswd

            name = input("Enter your name : ")
            print()
            email = input("Enter email please : ")
            account_created = str(date.today())
            print()
            cursor.execute(
                """
                INSERT INTO user_records
                (user_id, first_name, username, email, account_created, password)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (user_id, name, username, email, account_created, password))
            mycon.commit()
            print()
            print("Account made succesfully!")
            global status
            status = 1
            print()
            print("You'll be redirected to the menu, you can now start Encrypting and Decrypting without hassle! ")
            time.sleep(2)
            print()
            Menu()

        else:
            print("The passwords don't match.")
            signup()

def which_j():
    try:
        Ch = input("Which Journal do you want to Decrypt? (Enter Journal name) : ")
    except ValueError:
        print()
        print("Invalid Choice! Please enter the journal name.")
        print()
        time.sleep(1)
        which_j()
        return
    print()

    if Ch not in j_name:
        print("Journal not found. Check the name again!")
        which_j()

    else:
        for i in range(len(j_name)):

            if j_name[i] == Ch:
                global EN_KEY
                EN_KEY = en_key[i]
            else:
                continue

def Swiption():
    clear()
    section("SWIPTION ENCRYPTION")
    print()
    print("Welcome to Swiption Encryption - Our most secure form of Encryption!")
    print()
    print("Note that Swiption by default takes use of Randomised Mode.")
    print()

    if status != 1:
        print("For Swiption, having an account is mandatory!")
        print()
        Ch20 = input("Do you have an Account (y/n) : ")
        print()

        if Ch20 == "Y" or Ch20 == "y":
            print("Then first please Login :) ")
            print()
            login()
        elif Ch20 == "N" or Ch20 == "n":
            print("For Swiption, having an account is mandatory! ")
            print("Please signup or continue without Swiption :) ")
            print()
            print("You will be redirected in 3 seconds")
            time.sleep(3)
            print()
            print()
            print()
            print()

            divider()
            print("""
            
            What do you want to do?
            
            1. Signup
            2. Login
            3. Menu
            4. Exit
            
            """)

            choice()

            time.sleep(2)
            Menu()

        else:
            print("Invalid Choice! Please enter a number.")
            print()
            time.sleep(1)
            Swiption()

    else:

        print("A life is NUMBER, it means at what occurrence would the letter's cover be changed in the encryption.")
        print()

        global l
        try:
            l = int(input("Choose life : "))
        except ValueError:
            print()
            print("Invalid Choice! Please enter a number.")
            print()
            time.sleep(1)
            Swiption()
            return
        if l <= 0:
            print()
            print("Invalid Choice! Life must be a number greater than 0.")
            print()
            time.sleep(2)
            Swiption()
            return
        print()

        enlist = []

        cover_dict = []
        for i in range(l + 10):
            cover_dict.append({})

        j = input("Please feed the Journal for Encryption : ")
        print()
        j_name = input("Please name your Journal : ")

        if not j:
            print("Empty Journal!")
            Swiption()
        else:
            print("Journal Uploaded!")

        print()
        print("Encrypting...")
        time.sleep(1)

        m = 0

        global ldict
        ldict = {}

        for i in range(26):
            ldict[chr(65 + i)] = 0
            ldict[chr(97 + i)] = 0

        for i in j:

            if i.isalpha():
                place = ldict[i] // l

                if i.isalpha() and i not in cover_dict[place]:

                    ldict[i] += 1

                    if (place * l) + 1 == ldict[i] and ldict[i] != 0:
                        cover_dict.append({})

                    cover = "".join(
                        random.choices(string.ascii_letters + string.digits, k=6)
                    )

                    cover = cover + " "

                    cover_dict[place][i] = cover
                    enlist.append(cover)


                elif i in cover_dict[place]:

                    cover = cover_dict[place][i]
                    enlist.append(cover)

                    ldict[i] += 1

                else:
                    continue

            elif i == " ":
                enlist.append(i)

            else:
                enlist.append(i)

        finalenlist = "".join(enlist)

        journal_name = j_name

        encryption_key = json.dumps(cover_dict)
        encryption_date = str(date.today())

        cursor.execute(
            """
            INSERT INTO swiption_details
            (user_id, journal_name, encryption_date,
             encryption_key, life)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                user_id,
                journal_name,
                encryption_date,
                encryption_key,
                l
            )
        )

        mycon.commit()
        mycon.commit()

        print()
        print("Successfully Encrypted!")
        print()
        time.sleep(1)
        clear()
        show_output("Here's your Encrypted text", finalenlist)
        print()
        print("Please copy this and paste it somewhere, you'll need it while decrypting!")
        print()
        print("You'll be redirected to the menu shortly.")
        print()
        print()
        time.sleep(8)
        Menu()


def SwipDe():
    clear()
    cursor.execute(
        '''
        SELECT sd.*
        FROM swiption_details sd
        JOIN user_records ur
        ON sd.user_id = ur.user_id
        WHERE ur.username = ?
        ''',
        (username,)
    )

    j_data = cursor.fetchall()

    print("User_ID is", user_id)

    print()

    global s_id
    s_id = []
    for i in range(len(j_data)):
        s_id.append(j_data[i][0])

    print("Swiption_IDs :", s_id)

    print()

    global j_name
    j_name = []
    for i in range(len(j_data)):
        j_name.append(j_data[i][2])

    print("Journal_Names :", j_name)
    print()

    global en_date
    en_date = []
    for i in range(len(j_data)):
        en_date.append(j_data[i][3])

    for j in en_date:
        print("Date Created :", j)
        print()

    global en_key
    en_key = []
    for i in range(len(j_data)):
        en_key.append(j_data[i][4])

    for t in en_key:
        print(t)
        print()

    global life
    life = []
    for i in range(len(j_data)):
        life.append(j_data[i][5])

    print("Life Values :", life)
    print()

    Ch = input("Which Journal do you want to Decrypt? (Enter it's name) : ")

    if Ch not in j_name:
        print("Journal not found. Check the ID again!")
        time.sleep(1)
        SwipDe()

    else:
        global l
        idx = j_name.index(Ch)
        l = life[idx]

        for i in range(len(j_name)):

            if j_name[i] == Ch:
                global EN_KEY
                EN_KEY = en_key[i]
            else:
                continue
    clear()
    print("Starting Decryption!")
    print()
    print("Decrypting...")
    print()
    time.sleep(1)

    og_dict_key = json.loads(EN_KEY)

    RAW = input("Enter the raw encrypted journal : ")
    RAWlist = RAW.split(" ")

    tempstore = []

    for i in RAWlist:

        if i == "":
            tempstore.append(" ")
            continue

        elif not i.isalnum():
            tempstore.append(i)
            continue

        for d in og_dict_key:
            for key, value in d.items():

                if i == value.strip():
                    tempstore.append(key)
                    break
            else:
                continue

            break

    decrypted = "".join(tempstore)
    print()
    print("Decrypted Successfully!")
    print()
    print()
    time.sleep(1)
    clear()
    show_output("Here's your Decrypted text", decrypted)
    print()
    print("You can copy your decrypted journal and save it somewhere safe!")
    print()
    print("You will be redirected to menu shortly.")
    print()
    time.sleep(5)
    Menu()


def AdvRand():
    clear()
    section("RANDOMISED ENCRYPTION")
    if status == 1:

        enlist = []
        cover_dict = {}

        feed()

        if not journal:
            print("Empty Journal!")
            feed()
        else:
            print("Journal Uploaded!")

        print()

        trackHEH = []

        for x in journal:
            if x.isalpha() and x not in cover_dict:

                cover = "".join(random.choices(
                    string.ascii_letters + string.digits,
                    k=6
                ))
                print()
                cover = cover + " "
                cover_dict[x] = cover
                enlist.append(cover)
                trackHEH.append(cover)

            elif x in cover_dict:
                cover = cover_dict[x]
                enlist.append(cover)
                trackHEH.append(cover)
            else:
                enlist.append(x)

        print()
        print("Encrypting...")
        time.sleep(1)

        journal_name = j_name

        encryption_key = json.dumps(cover_dict)
        encryption_date = str(date.today())

        cursor.execute(
            """
            INSERT INTO journal_details
            (user_id, journal_name, encryption_key, encryption_date)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, journal_name, encryption_key, encryption_date))
        mycon.commit()

        finalenlist = "".join(enlist)
        print()
        print("Successfully Encrypted!")
        print()
        print()
        time.sleep(1)
        clear()
        show_output("Here's your Encrypted text", finalenlist)
        print()
        print("Please copy this and paste it somewhere, you'll need it while decrypting!")
        print()
        print("You'll be redirected to the menu shortly.")
        print()
        print()
        time.sleep(8)

        Menu()

    else:
        enlist = []
        cover_dict = {}

        feed()

        if not journal:
            print("Empty Journal!")
            feed()
        else:
            print("Journal Uploaded!")

        print()

        trackHEH = []

        for x in journal:
            if x.isalpha() and x not in cover_dict:

                cover = "".join(random.choices(
                    string.ascii_letters + string.digits,
                    k=6
                ))

                print()
                cover = cover + " "
                cover_dict[x] = cover
                enlist.append(cover)
                trackHEH.append(cover)


            elif x in cover_dict:
                cover = cover_dict[x]
                enlist.append(cover)
                trackHEH.append(cover)
            else:
                enlist.append(x)

        print()
        print("Encrypting...")
        time.sleep(1)

        finalenlist = "".join(enlist)
        print()
        print("Successfully Encrypted!")
        print()
        print()
        time.sleep(1)
        clear()
        show_output("Here's your Encrypted text", finalenlist)
        print()
        print("Please copy this and paste it somewhere, you'll need it while decrypting!")
        print()
        print()
        print("Here's the Encryption Key : ",json.dumps(cover_dict))
        print()
        print("Please copy this key too! It's important! Since you don't have an account.")
        print()
        print("You'll be redirected to the menu shortly in 10 seconds.")
        print()

        time.sleep(10)
        Menu()

def choice():

    Ch21 = int(input(" 1 OR 2 OR 3 : "))

    if Ch21 == 1:
            signup()
    elif Ch21 == 2:
            login()
    elif Ch21 == 3:
            Menu()
    elif Ch21 == 4:
            exit()
    else:
        print("Invalid choice!")
        choice()

def which_mode():
    print("1. Mark 1 (A to Z from 1 to 26 respectively, and a to z from 27 to 52 respectively.)")
    print("2. ASCII Version")
    print("3. Mark 2 (A to Z from 26 to 1 respectively, and a to z from 52 to 26 respectively.)")
    print("4. Mark 3 (A to Z from 2 to 52 respectively, even numbers only. \nAnd a to z from 1 to 51, odd numbers only.)")
    print()
    print("5. Mark 4 (A to Z from Z to A respectively and a to z from z to a respectively.)")
    print()
    global Ch4
    try:
        Ch4 = int(input("Which encryption mode out of these did your journal have? (1-5) : "))
        print()
    except ValueError:
        print()
        print("Invalid Choice! Please enter a number.")
        print()
        time.sleep(1)
        which_mode()
        return

def guide():
    clear()
    section("GUIDE")
    print("""
    Welcome to the Privournal Guide!
    Here's everything you need to know before diving in.
    """)
    time.sleep(2)

    print("""
──────────────────────────────────────────────────────────────────────────────
  WHAT IS PRIVOURNAL?
──────────────────────────────────────────────────────────────────────────────

  Privournal is a private journal encryption tool.
  It converts your journal text into an unreadable encrypted form,
  and only you can decrypt it back using the right key.

  Privournal stores NOTHING except your account details.
  Your journal content never gets saved anywhere — only the encryption
  key is stored (in your account), not the journal itself.
""")
    time.sleep(2)

    print("""
──────────────────────────────────────────────────────────────────────────────
  DO I NEED AN ACCOUNT?
──────────────────────────────────────────────────────────────────────────────

  No, but having one makes life much easier.

  WITHOUT an account:
    - You can still encrypt and decrypt journals.
    - BUT you must manually save and provide the Encryption Key yourself.
    - Swiption is NOT available.

  WITH an account:
    - Your encryption keys are saved automatically.
    - You can look up past journals by name.
    - Swiption is available.
""")
    time.sleep(2)

    print("""
──────────────────────────────────────────────────────────────────────────────
  ENCRYPTION MODES
──────────────────────────────────────────────────────────────────────────────
""")

    print("""  1. BASIC ENCRYPTION
  ───────────────────
  Simple and fast. Each letter is mapped to a number or another letter.
  Good enough if you just want casual privacy.

  There are 5 Basic modes:

    Mark 1     → A-Z maps to 1-26,  a-z maps to 27-52
    ASCII      → Each letter maps to its ASCII number (A=65, B=66... z=122)
    Mark 2     → A-Z maps to 26-1,  a-z maps to 52-27  (reverse of Mark 1)
    Mark 3     → A-Z maps to 2,4,6...52 (even),  a-z maps to 1,3,5...51 (odd)
    Mark 4     → A maps to Z, B maps to Y... (mirror alphabet)

  Remember which mode you used — you'll need to pick the same one to decrypt!
""")
    time.sleep(2)

    print("""  2. ADVANCED ENCRYPTION
  ──────────────────────
  Much stronger. You (or the system) assigns a unique "cover" to each letter.
  The cover is what appears in the encrypted text instead of the letter.

  There are 2 Advanced modes:

    Manual     → You type the cover for each letter yourself.
                 e.g. You decide A = "apple", B = "mango", etc.
                 Every letter must have a UNIQUE cover.

    Randomised → The system auto-generates a random 6-character cover
                 for each letter. Fast and very secure.

  The Encryption Key (a dictionary mapping letters to their covers)
  is what you need to decrypt. Save it if you don't have an account!
""")
    time.sleep(2)

    print("""  3. SWIPTION ENCRYPTION  ★ Most Secure ★
  ────────────────────────────────────────
  Swiption is Privournal's most powerful feature. It requires an account.

  The idea: a letter's cover CHANGES after it appears a certain number
  of times. That number is called the LIFE.

  Example with Life = 2:
    - First 2 times 'A' appears → it gets Cover 1
    - Next 2 times 'A' appears  → it gets a brand new Cover 2
    - And so on...

  This means even if someone notices a pattern, the pattern keeps changing!

  Life = 1  → Cover changes every single occurrence (maximum rotation)
  Life = 3  → Cover stays for 3 occurrences, then changes
  Life = 10 → Cover stays for 10 occurrences before changing

  Swiption always uses Randomised covers (auto-generated).
  Your Swiption key and Life value are saved to your account automatically.
""")
    time.sleep(2)

    print("""
──────────────────────────────────────────────────────────────────────────────
  HOW TO ENCRYPT
──────────────────────────────────────────────────────────────────────────────

  Step 1 → Go to "Encrypt a Journal Entry" from the Menu.
  Step 2 → Login or choose to proceed without an account.
  Step 3 → Choose Basic or Advanced encryption.
  Step 4 → If Advanced, choose Manual, Randomised, or Swiption.
  Step 5 → Paste or type your journal when prompted.
  Step 6 → Name your journal (if logged in).
  Step 7 → Copy the encrypted output and save it somewhere safe!
            If you don't have an account, copy the Encryption Key too!
""")
    time.sleep(2)

    print("""
──────────────────────────────────────────────────────────────────────────────
  HOW TO DECRYPT
──────────────────────────────────────────────────────────────────────────────

  Step 1 → Go to "Decrypt a Journal Entry" from the Menu.
  Step 2 → Login (if you have an account) or proceed without one.

  WITH an account:
    - Choose whether it's a Swiption journal or a regular one.
    - Your journals will be listed by name.
    - Enter the journal name, then paste your encrypted text.
    - Done!

  WITHOUT an account:
    - Choose Basic or Advanced.
    - For Basic: paste encrypted text, then pick the same Mark/mode used.
    - For Advanced: paste encrypted text AND provide your saved Key.
    - Done!
""")
    time.sleep(2)

    print("""
──────────────────────────────────────────────────────────────────────────────
  TIPS
──────────────────────────────────────────────────────────────────────────────

  ★ Always copy and save your encrypted journal text after encrypting.
    Privournal does not store your journal content — only the key.

  ★ If you don't have an account, save your Encryption Key somewhere safe.
    Without it, there is NO way to decrypt your journal.

  ★ For maximum security, use Swiption with a Life of 1 or 2.

  ★ For quick casual use, Basic Mark 4 is simple and easy to remember.

──────────────────────────────────────────────────────────────────────────────
""")
    time.sleep(1)

    input("Press Enter to go back to the Menu...")
    Menu()

def banner():
    print('''
    ██████╗ ██████╗ ██╗██╗   ██╗ ██████╗ ██╗   ██╗██████╗ ███╗   ██╗ █████╗ ██╗
    ██╔══██╗██╔══██╗██║██║   ██║██╔═══██╗██║   ██║██╔══██╗████╗  ██║██╔══██╗██║
    ██████╔╝██████╔╝██║██║   ██║██║   ██║██║   ██║██████╔╝██╔██╗ ██║███████║██║
    ██╔═══╝ ██╔══██╗██║╚██╗ ██╔╝██║   ██║██║   ██║██╔══██╗██║╚██╗██║██╔══██║██║
    ██║     ██║  ██║██║ ╚████╔╝ ╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║██║  ██║███████╗
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝ TM 

               Give your journals the privacy they deserve :) 
                We help your Journals stay Private and Safe
    ''')

if __name__ == "__main__":
    note()
    start()

    cursor.close()
    mycon.close()
