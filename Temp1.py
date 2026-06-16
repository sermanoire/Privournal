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

            RAW = input("Please feed the Journal for Encryption : ")

            if Ch5 == 1:
                dakey = mark1
            elif Ch5 == 1:
                dakey = asciiv
            elif Ch5 == 1:
                dakey = mark2
            elif Ch5 == 1:
                dakey = mark3
            elif Ch5 == 1:
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
    elif Ch5 == 1:
        dakey = asciiv
    elif Ch5 == 1:
        dakey = mark2
    elif Ch5 == 1:
        dakey = mark3
    elif Ch5 == 1:
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

# OLD CODE FOR DE

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
    print("Invalid Option! HEHE")

JOURNAL = input("Enter your Journal to encrypt it.")
normal_journal = []
for i in JOURNAL:
    if i.upper() in dakey:
        normal_journal.append(dakey[i.upper()])
    else:
        normal_journal.append(i)

finalnormal_journal = "".join(normal_journal)
print(textwrap.fill(finalnormal_journal, width=50))
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













def cover():
         print("What should be the cover for",x,"?")
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