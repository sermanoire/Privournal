''' PRIVOURNAL STORES NO DATA EXCEPT ACCOUNT DETAILS.
ECRYPTIONS AND DECRYPTIONS PURELY DONE BY LOGIC AND ENCRYPTION DATA IN USER'S ACCOUNT.
ENCRYPTION DATA CAN BE ALSO PASSWORD PROTECTED.
NOTE : ENCRYPTED TEXT HAS TO BE GIVEN BY USER IN CASE OF NO ACCOUNT'''

#FOR MY REFENECE - DATA Fetchall -> List of different records and each column's info in a tuple.
#THANK YOU

#Imports!

import random
import string
import json
import time
import os

from datetime import date
import textwrap

status = 0

# Mark 1!
mark1 = {}
for i in range(26):
  mark1[chr(65 + i)] = ""
  mark1[chr(97 + i)] = ""

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

#DB_CONNECTION
mycon = sql.connect(host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    database=os.getenv("DB_NAME"),
                    password=os.getenv("DB_PASSWORD"))

if mycon.is_connected():
    print("Connection's strong YAY!")
    print()
else:
    print("Not connected.")
    print()

cursor = mycon.cursor()




def start():
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
    print()
    ch = int(input("1 OR 2 OR 3? "))
    print()
    print()

    if ch == 1:
        En()
    elif ch == 2:
        De()
    elif ch == 3:
        exit()
    else:
        print("Invalid Choice")
        print("\n" * 100)
        Menu()


def exit():
    print("Thank you so much for using Privournal, Have a nice day!")
    print("Byeeeeee :)")
    print()

def De():
    print("Let's start Decryption!")
    if status == 1:

        CH = input("Do you want to Decrypt a Swiption-based Journal? (Y/N) : ")

        if CH == "y" or CH == "Y":
            SwipDe()
        elif CH == "n" or CH == "N":
            cursor.execute('''
                    SELECT jd.*
                    FROM journal_details jd
                    JOIN user_records ur
                    ON jd.user_id = ur.user_id
                    WHERE ur.username = %s
                    ''', (username,))

            j_data = cursor.fetchall()  # Fetching Journal Data

            global user_id
            user_id = (j_data[0][1])
            print("User_ID is", user_id)
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
            print("Journal_Names : ", j_name)
            print()
            print()

            global en_key
            en_key = []
            for i in range(len(j_data)):
                en_key.append(j_data[i][3])
            for j in en_key:
                print("Encryption Key : ", textwrap.fill(j, width=60))
                print()
                print()

            global en_date
            en_date = []
            for i in range(len(j_data)):
                en_date.append(j_data[i][4])
            for j in en_date:
                print("Date Created : ", j)
                print()

            which_j()

            print("Starting Decryption!")
            print()

            og_dict_key = json.loads(EN_KEY)

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
            print("Here's your Journal -> ", decrypted)
            print()
            print()
            print("You will be redirect to Menu in 10 seconds :) ")
            print()
            print("You can copy your decrypted journal and save it somewhere safe!")
            print()
            time.sleep(10)
            print("\n" * 100)
            Menu()

        else:
            print("Invalid Choice!")

    elif status != 1:
        Ch2 = input("Do you have an Account on Privournal? (Y/N) : ")
        print()

        if Ch2 == "y" or Ch2 == "Y":
            login()
        elif Ch2 == "n" or Ch2 == "N":

            print()
            print('''
            1. Basic Encryption
            2. Advanced Encryption 
            ''')
            print()

            Ch3 = int(input("Which Encryption does your Journal have? (1 OR 2) : "))
            print()
            if Ch3 == 1:
                    RAW = input("Enter the Encrypted text : ")
                    RAWlist = RAW.split(" ")
                    print()
                    print()
                    print("1. Mark 1 (A to Z from 1 to 26 respectively, and a to z from 27 to 52 respectively.)")
                    print("2. ASCII Version")
                    print("3. Mark 2 (A to Z from 26 to 1 respectively, and a to z from 52 to 26 respectively.)")
                    print("4. Mark 3 (A to Z from 2 to 52 respectively, even numbers only. \nAnd a to z from 1 to 51, odd numbers only.)")
                    print()
                    print("5. Mark 4 (A to Z from Z to A respectively and a to z from z to a respectively.)")
                    print()
                    global Ch4
                    Ch4 = int(input("Which one out of these? (1-5) : "))
                    print()
                    print("Decrypting...")
                    print()
                    print()
                    time.sleep(1)
                    basicDe()

            elif Ch3 == 2:

                Ch5 = input("Do you have the Encryption Key? (Y/N) : ")

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
                    print("Here's your Journal -> ", decrypted)
                    print()
                    print()
                    print("You will be redirect to Menu in 10 seconds :) ")
                    print()
                    time.sleep(1)
                    print("You can copy your decrypted journal and save it somewhere safe!")
                    print("Thank you for using Privournal!")
                    print()
                    time.sleep(10)
                    print("\n" * 100)
                    Menu()

                elif Ch5 == "n" or Ch5 == "N":
                    print("We're sorry, we cannot Decryption without the Key. \nBe sure to make an account on Privournal if you have trouble keeping Keys.")
                    print()
                    print("You will be redirected to the Menu Shortly.")
                    print()
                    time.sleep(3)
                    print("\n" * 100)
                    Menu()


                else:
                    print("Invalid choice!")
                    print()
                    De()


def login():
        global username1
        global pswd
        username1 = input("Enter Username : ")
        pswd1 = input("Enter Password : ")

        cursor.execute(
            "SELECT password FROM user_records WHERE username = %s",
            (username1,)
        )

        acc_d = cursor.fetchall()

        if acc_d == []:
            print()
            print("No such Username found in our database!")

        else:
            if pswd1 == acc_d[0][0]:
                print()
                print("Logged in Successfully!")

                cursor.execute(
                    "SELECT * FROM user_records WHERE username = %s",
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
                print("You will be redirected to the menu shortly :) ")
                print("\n" * 100)
                time.sleep(3)
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
                    logic()

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
    print("Here's you Decrypted Journal -> ",decrypted)
    print()
    print("Thank you for using Privournal!")
    print("Be sure to make an account for smoother experience in the future :) ")
    print()
    print("You will be redirected to the Menu in 10 seconds. ")
    print()
    time.sleep(10)
    print("\n" * 100)
    Menu()

def En():

        if status != 1:

            Ch8 = input("Do you have an Account? (Y/N) : ")

            if Ch8 == "Y" or Ch8 == "y":
                print("You'll be redirected to Login page, please complete the login first :) ")
                time.sleep(1)
                login()

            elif Ch8 == "N" or Ch8 == "n":
                print()
                global Ch7
                Ch7 = input("Do you want to save encryption details on our database, \nfor future decryptions and referencing records? (Y/N) : ")
                print()

                if Ch7 == "Y" or Ch7 == "y":
                    signup()

                elif Ch7 == "N" or Ch7 == "n":

                    print("Choose Mode of Encryption : ")
                    print("1. Basic (Weak but holds well if you have dummies tryna read your Journal lol)")
                    print("2. Advanced (Includes Swiption And Randomised Mode - Really strong encryption, \nholds well even if you have prodigies trying to read your Journal.")
                    print()
                    print()

                    Ch6 = int(input("Which one? (1 OR 2) : "))
                    if Ch6 == 1:
                        print()
                        print("Welcome to Basic Encryption!")
                        print()
                        print("1. Mark 1 (A to Z from 1 to 26 respectively, and a to z from 27 to 52 respectively.)")
                        print("2. ASCII Version")
                        print("3. Mark 2 (A to Z from 26 to 1 respectively, and a to z from 52 to 26 respectively.)")
                        print("4. Mark 3 (A to Z from 2 to 52 respectively, even numbers only. \nAnd a to z from 1 to 51, odd numbers only.)")
                        print("5. Mark 4 (A to Z from Z to A respectively and a to z from z to a respectively.)")
                        print()

                        Ch7 = int(input("Which one out of these? (1-5) "))

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
                        print("Here's you Encrypted text --> ", encrypted)
                        print()
                        print("Thank you for using Privournal!")
                        print("Be sure to make an account for smoother experience in future :) ")
                        print("You will be redirected to the Menu in 10 seconds")
                        print()
                        time.sleep(10)
                        print("\n" * 100)
                        Menu()

                    elif Ch6 == 2:
                        print("Advanced Encryption it is then!")
                        print()

                        swiption = input("Do you want to enable Swiption for a stronger Encryption? (Y/N) : ")

                        print()
                        if swiption == "Y" or swiption == "y":
                            Swiption()

                        elif swiption == "N" or swiption == "n":
                            AdvEn()

                        else:
                            print("Invalid choice")
                            En()

                    else:
                        print("Invalid input!")
                        En()


        else:

            print("Choose Mode of Encryption : ")
            print("1. Basic (Weak but holds well if you have dummies tryna read your Journal lol)")
            print("2. Advanced (Includes Swiption And Randomised Mode - Really strong encryption, \nholds well even if you have prodigies trying to read your Journal.")
            print()
            print()

            Ch6 = int(input("Which one? (1 OR 2) : "))

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


                Ch7 = int(input("Choose one of these (1-5) : "))

                j = input("Please feed the Journal for Encryption : ")
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
                print("Successfully Encrypted!")
                time.sleep(1)

                journal_name = j_name
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
                print("Here's you Encrypted Journal -> ", encrypted)
                print()
                print("Thank you for using Privournal!")
                print("You'll be redirected to the menu.")
                print()
                print()

                time.sleep(5)
                print("\n" * 100)
                Menu()


            elif Ch6 == 2:
                print("Advanced Encryption it is then!")
                print()

                swiption = input("Do you want to enable Swiption for a stronger Encryption? (Y/N) : ")

                print()
                if swiption == "Y" or swiption == "y":
                    Swiption()

                elif swiption == "N" or swiption == "n":
                    AdvEn()

                else:
                    print("Invalid choice")
                    En()

            else:
                print("Invalid input!")
                AdvEn()

def AdvEn():

    global journal

    Ch_rand = input("Do you want to enable Randomised Encryption for more ease and security? ")

    if Ch_rand == "y" or Ch_rand == "Y":
        AdvRand()

    elif Ch_rand == "n" or Ch_rand == "N":
        if status != 1:

            global enlist
            enlist = []
            global cover_dict
            cover_dict = {}

            feed()

            if not journal:
                print("Empty Journal!")
                feed()
            else:
                print("Journal Uploaded!")

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

            finalenlist = "".join(enlist)
            print()
            print("Successfully Encrypted!")
            print()
            print("Here's the encrypted Journal --> ", finalenlist)
            print()
            print("Here's the Encryption Key : ",json.dumps(cover_dict))
            print()
            print("You'll be redirected to the a new page.")
            print()
            print()
            time.sleep(10)
            print("\n" * 100)
            Menu()

        else:
            enlist = []

            cover_dict = {}

            journal = input("Please feed the Journal for Encryption : ")
            j_name = input("Please name your Journal : ")

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

            journal_name = j_name

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
            print("\n" * 100)
            Menu()

    else:
         print("Invalid input!")
         AdvEn()

def feed():
    global journal
    global j_name
    journal = input("Please feed the Journal for Encryption : ")
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
        print("2 letters can't have the same cover na! ")
        coverr()

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
            print("\n" * 100)
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

 else:
     for i in range(len(j_id)):

        if j_id[i] == Ch:
                global EN_KEY
                EN_KEY = en_key[i]
        else:
                continue

def Swiption():

    print("Welcome to Swiption Encryption - Our most secure form of Encryption!")
    print()
    print("Note that Swiption by default takes use of Randomised Mode.")
    print()

    if status != 1:
        print("For Swiption, having an account is mandatory!")
        Ch20 = input("Do you have an Account (Y/N) : ")

        if Ch20 == "Y" or Ch20 == "y":
            print("Then first please Login :) ")
            print()
            login()
        elif Ch20 == "N" or Ch20 == "n":
            print("Please Signup or continue without Swiption :) ")
            print("You'll be redirected to the menu ")
            print()
            time.sleep(3)
            Menu()
        else:
            print("Invalid Choice!")
            Swiption()

    else:
        print("A life is at what occurrence would the letter's cover be changed.")
        global l
        l = int(input("Choose life : "))
        print()

        enlist = []

        cover_dict = []
        for i in range(l+10):
            cover_dict.append({})

        journal = input("Please feed the Journal for Encryption : ")
        j_name = input("Please name your Journal : ")

        if not journal:
            print("Empty Journal!")
            feed()
        else:
            print("Journal Uploaded!")

        m = 0

        global ldict
        ldict = {}
        for i in range(26):
            ldict[chr(65 + i)] = 0
            ldict[chr(97 + i)] = 0

        for i in journal:

            if i.isalpha():
                place = ldict[i] // l

                if i.isalpha() and i not in cover_dict[place]:

                    ldict[i] += 1

                    if (place*l)+1 == ldict[i] and ldict[i] != 0 :
                        cover_dict.append({})

                    cover = "".join(
                        random.choices(string.ascii_letters + string.digits, k=6)
                    )


                    cover_dict[place][i] = cover
                    enlist.append(cover)


                elif i in cover_dict[place]:

                    cover = cover_dict[place][i]
                    enlist.append(cover)

                    ldict[i] += 1
            else:
                enlist.append(i)

        finalenlist = "".join(enlist)

        journal_name = j_name

        encryption_key = json.dumps(cover_dict)
        encryption_date = date.today()

        cursor.execute(
            """
            INSERT INTO swiption_details
            (user_id, journal_name, encryption_date,
             encryption_key, life)
            VALUES (%s, %s, %s, %s, %s)
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
        print("Here's the encrypted Journal --> ", finalenlist)
        print()
        print()
        print("You'll be redirected to the a new page.")
        print()
        print()
        time.sleep(5)
        print("\n" * 100)
        Menu()

def SwipDe():
    cursor.execute(
        '''
        SELECT sd.*
        FROM swiption_details sd
        JOIN user_records ur
        ON sd.user_id = ur.user_id
        WHERE ur.username = %s
        ''',
        (username,)
    )

    j_data = cursor.fetchall()

    global user_id
    user_id = j_data[0][1]
    print("User_ID is", user_id)
    print()
    print()

    global s_id
    s_id = []
    for i in range(len(j_data)):
        s_id.append(j_data[i][0])

    print("Swiption_IDs :", s_id)
    print()
    print()

    global j_name
    j_name = []
    for i in range(len(j_data)):
        j_name.append(j_data[i][2])

    print("Journal_Names :", j_name)
    print()
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

    for j in en_key:
        print("Encryption Key :", textwrap.fill(j, width=60))
        print()
        print()

    global life
    life = []
    for i in range(len(j_data)):
        life.append(j_data[i][5])

    print("Life Values :", life)
    print()

    Ch = int(input("Which Journal do you want to Decrypt? (Enter Swiption_ID) : "))
    print()

    global l
    l = life[Ch-1]

    if Ch not in s_id:
        print("Journal not found. Check the ID again!")
        which_j()

    else:
        for i in range(len(s_id)):

            if s_id[i] == Ch:
                global EN_KEY
                EN_KEY = en_key[i]
            else:
                continue

    print("Starting Decryption!")
    print()

    og_dict_key = json.loads(EN_KEY)

    RAW = input("Enter the raw encrypted journal : ")
    RAWlist = RAW.split(" ")


    ldict2 = {}

    for d in og_dict_key:
        for cover in d.values():
            ldict2[cover.strip()] = 0

    tempstore = []
    for i in RAWlist:

        if i == "":
            tempstore.append(" ")
            continue
        elif not i.isalnum():
            tempstore.append(i)
            continue

        place = (ldict2[i] // l)

        for key, value in og_dict_key[place].items():

            if (str(i) + " ") == value:
                tempstore.append(key)
                ldict2[value.strip()] += 1
                continue

    decrypted = "".join(tempstore)

    print()
    print("Decrypted Successfully!")
    print("Here's your Journal -> ", decrypted)
    print()
    print()
    print("You will be redirect to Menu in 10 seconds :) ")
    print()
    print("You can copy your decrypted journal and save it somewhere safe!")
    print()
    time.sleep(10)
    print("\n" * 100)
    Menu()

def AdvRand():
    global enlist
    enlist = []
    global cover_dict
    cover_dict = {}

    feed()

    if not journal:
        print("Empty Journal!")
        feed()
    else:
        print("Journal Uploaded!")

    print()

    global trackHEH
    trackHEH = []

    global x

    for x in journal:
        if x.isalpha() and x not in cover_dict:

            global cover
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

    finalenlist = "".join(enlist)
    print()
    print("Successfully Encrypted!")
    print()
    print("Here's the encrypted Journal --> ", finalenlist)
    print()
    print("Here's the Encryption Key : ", json.dumps(cover_dict))
    print()
    print("You'll be redirected to the a new page.")
    print()
    print()
    time.sleep(10)
    print("\n" * 100)
    Menu()

start()

cursor.close()
mycon.close()


