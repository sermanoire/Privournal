
def feed():
    journal = input("Please feed the Journal : ")

    if journal == "":
        print("Empty Journal!")
    else:
        print("Journal Uploaded!")

def Menu():
    print("Welcome to Privournal!")
    print("We help your Journals stay Private and Safe :) ")
    print()
    print()
    print("What would you like to do today?")
    print()
    print("1. Encrypt a Journal Entry")
    print("2. Decrypt a Journal Entry")

    ch = int(input("I want to : "))
    print("(Enter just 1 OR 2)")

    if ch == 1:
        print("Let's get our hands into some Encryption!")

        def En():

            print("Choose Mode of Encryption :) ")
            print("1. Basic (Weak but holds well if you have dummies tryna read your Journal)")
            print("2. Advanced (Includes Swiption - Really strong encryption, \nholds well even if you have prodigies trying to read your Journal.")
            print()
            print("Which one? 1 OR 2?")
            ch2 = int(input("I choose : "))

            if ch2 == 1:






