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

dakey = {}

# Mark 1!
mark1 = {}
for i in range(26):
    mark1[chr(65 + i)] = " "
    mark1[chr(97 + i)] = " "

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
    input("Press Enter to continue...")
    print()
    print()
    startup()

def startup():

    divider()
    print("How would you want to continue?")
    print("1. With an account")
    print("2. Without an account")
    print()

    ques1 = int(input("Enter Choice (1 or 2) : ").strip())

    if ques1 == 1:
        print()
        divider()
        print("1.Log in")
        print("2.Sign up")
        ques2 = int(input("Enter Choice (1 or 2) : ").strip())
        if ques2 == 1:
            login()

        elif ques2 == 2:
            signup()

        else:
            print()
            print("Invalid Choice!")
            startup()

    if ques1 == 2:

        print()
        print()
        print("If you continue without an account,")
        print("- You will have to store (Copy-Paste) the *encryption keys* AND the *encrypted text* somewhere safe on your device manually")
        print("- You will NOT be able to use the Swiption feature")
        print("- No encryption data such as date of encyption, journal name and so on is saved")
        print()
        print()
        ques3 = input("Are you sure you'd like to continue without an account? (y/n) ")
        print()

        if ques3 == ("y" or "Y"):
            print("Alrightyyy!")
            input("Press Enter to continue...")
            Noacc_exp()

        elif ques3 == ("n" or "N"):
            print("Sure, let's get you an account then! ")
            time.sleep(2)
            signup()

        else:
            print("Invalid Choice!")
            startup()

def Noacc_exp():
    print()
    print("Redirecting to the Menu...")
    time.sleep(1)
    Menu2()

def login():
    clear()
    section("LOGIN")

    global user_name
    global pswd

    user_name = input("Enter Username : ").strip()
    pswd = input("Enter Password : ").strip()

    cursor.execute(
        "SELECT password FROM user_records WHERE username = ?",
        (user_name,)
    )

    acc_details = cursor.fetchall()

    if acc_details == []:
        print()
        print("No such Username found in the database!")
        time.sleep(1)
        login()

    else:
        if pswd == acc_details[0][0]:
            print()
            print("Logged in Successfully!")

            cursor.execute(
                "SELECT * FROM user_records WHERE username = ?",
                (user_name,)
            )

            acc_details = cursor.fetchall()
            global username
            global user_id
            global password
            global email
            global account_created

            user_id = acc_details[0][0]
            name = acc_details[0][1]
            username = acc_details[0][2]
            email = acc_details[0][3]
            account_created = acc_details[0][4]
            password = acc_details[0][5]

            print()
            print()

            #To know user's logged in
            global status
            status = 1

            print()

            time.sleep(1)
            Menu1()

        else:
            print()
            print("Wrong Password.")
            print()

            try:
                haw = int(input("Exit or Login again? (1 OR 2) : ").strip())

            except ValueError:
                print("Invalid Choice! Please enter a number.")
                time.sleep(1)
                login()
                return

            if haw == 1:
                print("Exiting...")
                time.sleep(1)
                exit()
            elif haw == 2:
                print("Redirecting to login page...")
                time.sleep(2)
                login()
            else:
                print("Invalid Choice!")
                print()
                time.sleep(1)
                login()

def signup():

    clear()
    section("SIGN UP")
    print()
    cursor.execute("SELECT COALESCE(MAX(user_id), 0) + 1 FROM user_records")
    global user_id
    user_id = cursor.fetchone()[0]

    temp_username = input("Set a username : ").strip()
    print()

    if len(temp_username) > 16:
        print("Invalid! It should be at most 16 characters.")
        print()
        print()
        time.sleep(1)
        signup()

    elif " " in temp_username:
        print("Spaces not allowed!")
        print()
        print()
        time.sleep(1)
        signup()

    elif len(temp_username) < 6:
        print("Should be atleast 6 characters long!")
        print()
        print()
        time.sleep(1)
        signup()

    else:
        global username
        username = temp_username

    temp_pswd = input("Set a password : ").strip()
    print()

    if len(temp_pswd) > 16:
        print("Invalid! It should be at most 18 characters.")
        print()
        print()
        time.sleep(1)
        signup()

    elif " " in temp_pswd:
        print("Spaces not allowed!")
        print()
        print()
        time.sleep(1)
        signup()

    elif len(temp_pswd) < 6:
        print("Should be atleast 6 characters long!")
        print()
        print()
        time.sleep(1)
        signup()

    elif temp_pswd == username:
        print("Username and password cannot be same!")
        time.sleep(1)
        signup()

    else:
        t_conf_pswd = input("Confirm password : ").strip()
        print()

        if t_conf_pswd == temp_pswd:
            password = temp_pswd

            name = input("Enter your name : ").strip()
            print()
            email = input("Enter email please : ").strip()
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

            #To know user's logged in.
            global status
            status = 1

            print()
            print("You'll be redirected to the menu, you can now start Encrypting and Decrypting without any hassle! ")
            time.sleep(2)
            print()
            Menu1()

        else:
            print("The passwords don't match.")
            signup()

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

    input("Press Enter...")
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
    input("Press Enter...")
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
    input("Press Enter...")
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
    input("Press Enter...")
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
    input("Press Enter...")
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
    input("Press Enter...")
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
    input("Press Enter...")
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

    input("Press Enter to return to the menu...").strip()
    if status == 1:
        Menu1()
    else:
        Menu2()

def exit():
    clear()
    section("GOODBYE")
    print("Thank you so much for using Privournal, Have a nice day!")
    print("Byeeeeee :)")
    print()

def En():
        clear()
        section("ENCRYPTION")

        if status != 1:

                    print("Choose Mode of Encryption : ")
                    print()
                    print("1. Basic (Weak but holds well if you have dummies tryna read your Journal lol)")
                    print("2. Advanced (Randomised or Manual) Mode - Really strong encryption, \nholds well even if you have Patrick Jane tryna crack encryption to read your Journal.")
                    print()
                    print()

                    try:
                        ques5 = int(input("Which one? (1 OR 2) : ").strip())

                    except ValueError:
                        print("Invalid Choice!")
                        time.sleep(1)
                        En()
                        return

                    if ques5 == 1:

                        clear()
                        section("Basic Encryption")

                        print("Welcome!")
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
                            ques6 = int(input("Which mode? (1-5) ").strip())
                        except ValueError:
                            print("Invalid Choice!")
                            time.sleep(1)
                            En()
                            return

                        if ques6 == 1:
                            dakey = mark1
                        elif ques6 == 2:
                            dakey = asciiv
                        elif ques6 == 3:
                            dakey = mark2
                        elif ques6 == 4:
                            dakey = mark3
                        elif ques6 == 5:
                            dakey = mark4
                        else:
                            print("Invalid Option!")

                        global j
                        j = input("Please feed the Journal for Encryption : ").strip()
                        print()
                        print("Encrypting...")
                        time.sleep(1)
                        journal = list(j)
                        de_list = []

                        for i in journal:
                            if i in dakey:
                                for keys, values in dakey.items():
                                    if keys == i:
                                        de_list.append(values)
                                    else:
                                        continue
                            else:
                                de_list.append(i)

                        encrypted = "".join(de_list)
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
                        input("Press enter to return to the menu...")
                        Menu2()

                    elif ques5 == 2:
                        print()
                        print()
                        divider()
                        print("Advanced Encryption it is then!")
                        print()
                        print()
                        AdvEn2()

        else:

            print("Choose Mode of Encryption : ")
            print()
            print("1. Basic (Weak but holds well if you have dummies tryna read your Journal lol)")
            print(
                  "2. Advanced (Includes Swiption, Randomised And Manual) Mode - Really strong encryption, \nholds well even if you have Patrick Jane tryna crack the encryption to read your Journal.")
            print()
            print()

            try:
                ques7 = int(input("Which one? (1 OR 2) : ").strip())
            except ValueError:
                print("Invalid Choice!")
                time.sleep(1)
                En()
                return

            if ques7 == 1:
                clear()
                section("Basic Encryption")

                print("Welcome!")
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
                    ques8 = int(input("Choose one of these (1-5) : ").strip())
                    if ques8 not in [1,2,3,4,5]:
                        print()
                        print("Invalid Choice!")
                        time.sleep(1)
                        En()

                except ValueError:
                    print("Invalid Choice! Please enter a number.")
                    time.sleep(1)
                    En()
                    return
                print()

                j = input("Please feed the Journal for Encryption : ").strip()
                print()
                journal = list(j)

                j_name = input("Please name your Journal : ").strip()

                if ques8 == 1:
                    dakey = mark1
                elif ques8 == 2:
                    dakey = asciiv
                elif ques8 == 3:
                    dakey = mark2
                elif ques8 == 4:
                    dakey = mark3
                elif ques8 == 5:
                    dakey = mark4
                else:
                    print("Invalid Option!")

                print()
                print("Encrypting...")
                time.sleep(1)
                de_list = []

                for i in journal:
                    if i in dakey:
                        for keys, values in dakey.items():
                            if keys == i:
                                de_list.append(values)
                            else:
                                continue
                    else:
                        de_list.append(i)

                encrypted = "".join(de_list)
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
                input("Press enter to return to the menu...")
                Menu1()

            elif ques7 == 2:
                print()
                print()
                divider()
                print("Advanced Encryption it is then!")
                print()
                print()

                AdvEn2()

                swiption = input("Do you want to enable Swiption for a stronger Encryption? (y/n) : ").strip()

                print()
                if swiption == "Y" or swiption == "y":
                    Swiption()

                elif swiption == "N" or swiption == "n":
                    AdvEn1()

                else:
                    print("Invalid Choice! Please enter a number.")
                    print()
                    time.sleep(1)
                    En()
            else:
                print("Invalid input!").strip()
                AdvEn1()

def AdvEn1():

    global journal
    global en_list

    Ch_rand = input("Do you want to enable Randomised Encryption for more ease and security? (y/n) ").strip()
    print()

    if Ch_rand == "y" or Ch_rand == "Y":
        AdvRand()

    elif Ch_rand == "n" or Ch_rand == "N":

            en_list = []

            cover_dict = {}

            print()
            journal = input("Please feed the Journal for Encryption : ").strip()
            print()
            j_name = input("Please name your Journal : ").strip()
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
                    cover = input("Cover = ").strip()
                    cover = cover + " "
                    cover_dict[x] = cover
                    en_list.append(cover)
                elif x in cover_dict:
                    cover = cover_dict[x]
                    en_list.append(cover)
                else:
                    en_list.append(x)

            print()
            print("Encrypting...")
            time.sleep(1)
            finalenlist = "".join(en_list)

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
            print("Thank you for using Privournal!")
            input("Press Enter to return to the menu...").strip()
            print()
            Menu1()

    else:
        print("Invalid input!")
        AdvEn1()

def AdvEn2():

    global journal
    global en_list

    en_list = []
    global cover_dict
    cover_dict = {}

    Ch_rand = input("Do you want to enable Randomised Encryption for more ease and security? (y/n) ").strip()
    print()

    if Ch_rand == "y" or Ch_rand == "Y":

        AdvRand()

    elif Ch_rand == "n" or Ch_rand == "N":

        feed()

        if not journal:
            print("Empty Journal!")
            feed()

        print()
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
                en_list.append(cover)
                trackHEH.append(cover)
            else:
                en_list.append(x)

        print()
        print("Encrypting...")
        time.sleep(1)
        finalenlist = "".join(en_list)
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
        print("Thank you for using Privournal!")
        input("Press Enter to return to the menu...").strip()
        print()
        Menu2()

def AdvRand():
    clear()
    section("RANDOMISED ENCRYPTION")

    if status == 1:

        en_list = []
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
                en_list.append(cover)
                trackHEH.append(cover)

            elif x in cover_dict:
                cover = cover_dict[x]
                en_list.append(cover)
                trackHEH.append(cover)
            else:
                en_list.append(x)

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

        finalenlist = "".join(en_list)
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
        print("Thank you for using Privournal!")
        input("Press Enter to return to the menu...").strip()
        print()
        Menu1()

    else:
        en_list = []
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
                en_list.append(cover)
                trackHEH.append(cover)


            elif x in cover_dict:
                cover = cover_dict[x]
                en_list.append(cover)
                trackHEH.append(cover)
            else:
                en_list.append(x)

        print()
        print("Encrypting...")
        time.sleep(1)

        finalenlist = "".join(en_list)
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
        print("AND Here's the Encryption Key : ")
        print(json.dumps(cover_dict))
        print()
        print("Please copy this key too! It's Important! Since you don't have an account.")
        print()
        print("Thank you for using Privournal!")
        input("Press Enter to return to the menu...").strip()
        print()
        Menu2()

def Swiption():
    clear()
    section("SWIPTION ENCRYPTION")
    print()
    print("Welcome to Swiption Encryption - Our most secure form of Encryption!")
    print()
    print("A life is NUMBER, it means at what occurrence would the letter's cover be changed in the encryption. (Eg. 2,3,...) ")
    print()

    global l
    try:
        l = int(input("Choose life : ").strip())
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

    en_list = []

    cover_dict = []
    for i in range(l + 10):
        cover_dict.append({})

    j = input("Please feed the Journal for Encryption : ").strip()
    print()
    j_name = input("Please name your Journal : ").strip()

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
                en_list.append(cover)

            elif i in cover_dict[place]:

                cover = cover_dict[place][i]
                en_list.append(cover)

                ldict[i] += 1

            else:
                continue

        elif i == " ":
            en_list.append(i)

        else:
            en_list.append(i)

    finalenlist = "".join(en_list)

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
    print("Thank you for using Privournal!")
    input("Press Enter to return to the menu...").strip()
    print()
    Menu1()

def De2():

    clear()
    section("DECRYPTION")
    print()

    global RAWlist
    RAWlist = []

    print()
    print("1. Basic Encryption")
    print("2. Advanced (Randomised/Manual) Encryption ")
    print("3. Exit")
    print()
    print("Note that to Decrypt a Swiption based journal, you need an account. ")
    print()
    print()

    try:
        Ch3 = int(input("Which Encryption does your Journal have? (1 OR 2) : ").strip())
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
        RAW = input("Enter the Encrypted text : ").strip()
        RAWlist = RAW.split(" ")
        print()
        time.sleep(1)
        clear()
        print()

        which_mode()

        time.sleep(1)
        basicDe()

    elif Ch3 == 2:

        Ch5 = input("Do you have the Encryption Key? (y/n) : ").strip()
        print()

        if Ch5 == "y" or Ch5 == "Y":
            given_dict_key = input("Enter the Encryption Key please : ").strip()
            try:
                given_dict_key = json.loads(given_dict_key)
            except json.decoder.JSONDecodeError:
                print(
                    "That doesn't look like a valid Encryption Key. Please check and paste it exactly as given.")
                print()
                De()
                return

            print()
            RAW = input("Enter the raw encrypted journal : ").strip()
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
            print()
            print("Decrypting...")
            print()
            print("Decrypted Successfully!")
            print()
            time.sleep(1)
            clear()
            show_output("Here's your Journal", decrypted)
            print()
            print("You can copy your decrypted journal and save it somewhere safe!")
            print()
            print("Thank you for using Privournal!")
            input("Press Enter to return to the menu...").strip()
            print()
            Menu2()

        elif Ch5 == "n" or Ch5 == "N":
            print()
            print("We're sorry, we cannot Decryption without the Key. \nBe sure to make an account on Privournal if you have trouble keeping Keys.")
            print()
            print("Thank you for using Privournal!")
            input("Press Enter to return to the menu...").strip()
            print()
            Menu2()

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

def De1():
    clear()
    section("DECRYPTION")
    print()

    CH = input("Do you want to Decrypt a Swiption based Journal? (y/n) : ").strip()
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

        RAW = input("Enter the raw encrypted journal : ").strip()

        global RAWlist

        RAWlist = []

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
        print()
        print("Decrypting...")
        print()
        print("Decrypted Successfully!")
        print()
        time.sleep(1)
        clear()
        show_output("Here's your Journal", decrypted)
        print()
        print("You can copy your decrypted journal and save it somewhere safe!")
        print()
        print("Thank you for using Privournal!")
        input("Press Enter to return to the menu...").strip()
        print()
        Menu1()

    else:
        print("Invalid Choice!")
        print()
        time.sleep(1)
        De1()

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

    de_list = []

    for i in RAWlist:
        if i == "":
            de_list.append(" ")
        else:
            for keys, values in dakey.items():
                if values.strip() == i:
                    de_list.append(keys)
                else:
                    continue
            if not i.isalnum() and i != "":
                de_list.append(i)

    decrypted = "".join(de_list)
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
    input("Press Enter to return to the menu...").strip()
    print()

    if status == 1:
        Menu1()
    else:
        Menu2()

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

    Ch = input("Which Journal do you want to Decrypt? (Enter it's name) : ").strip()

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
    time.sleep(1)

    og_dict_key = json.loads(EN_KEY)

    RAW = input("Enter the raw encrypted journal : ").strip()
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
    print("Decrypting...")
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
    input("Thank you for using Privournal!")
    input("Press Enter to go back to the menu...")
    print()
    Menu1()

def Menu1():
    clear()
    section("MENU")
    print("What would you like to do today?")
    print()
    print("1. Encrypt a Journal Entry")
    print("2. Decrypt a Journal Entry")
    print("3. Guide")
    print("4. Exit")
    divider()
    ques4 = int(input("1 OR 2 OR 3 OR 4 : ").strip())

    try:
        ch = int(ques4)
    except ValueError:
        print()
        print("Invalid Choice! Please enter a number.")
        print()
        time.sleep(1)
        Menu1()
        return
    print()
    print()

    if ch == 1:
        En()
    elif ch == 2:

        if status == 1:
            De1()
        else:
            De2()

    elif ch == 3:
        guide()
    elif ch ==4:
        exit()
    else:
        print("Invalid Choice!")
        print()
        time.sleep(1)
        Menu1()

def Menu2():
    clear()
    section("MENU")
    print("What would you like to do today?")
    print()
    print("1. Encrypt a Journal Entry")
    print("2. Decrypt a Journal Entry")
    print("3. Guide")
    print("4. Exit")
    divider()
    raw = input("1 OR 2 OR 3 OR 4 : ").strip()
    try:
        ch = int(raw)
    except ValueError:
        print()
        print("Invalid Choice! Please enter a number.")
        print()
        time.sleep(1)
        Menu2()
        return
    print()
    print()

    if ch == 1:
        En()
    elif ch == 2:
        if status == 1:
            De1()
        else:
            De2()

    elif ch == 3:
        guide()
    elif ch == 4:
        exit()
    else:
        print("Invalid Choice!")
        print()
        time.sleep(1)
        Menu2()

def feed():
    global journal
    global j_name
    journal = input("Please feed the Journal for Encryption : ").strip()

    if status == 1:
        j_name = input("Please name your Journal : ").strip()

def coverr():
    print("What should be the cover for", x, "?")
    global cover
    cover = input("Cover = ").strip()

    if cover not in trackHEH:
        print()
        cover = cover + " "
        cover_dict[x] = cover
        en_list.append(cover)
        trackHEH.append(cover)
    else:
        print("2 letters can't have the same cover hon! ")
        coverr()

def which_j():
    try:
        Ch = input("Which Journal do you want to Decrypt? (Enter Journal name) : ").strip()
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
        Ch4 = int(input("Which encryption mode out of these did your journal have? (1-5) : ").strip())
        print()
    except ValueError:
        print()
        print("Invalid Choice! Please enter a number. ")
        print()
        time.sleep(1)
        which_mode()
        return

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

