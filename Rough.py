import random
import string
import json
import time
from datetime import date


#RANDOM AS SEPERATE, RANDOMLY ADV AND SWIPTION

def randomEe():
    enlistrandom = []
    for x in journal:
        if x not in mydictrandom:
            if text.isalpha():
                code = "".join(random.choice(
                    string.ascii_letters + string.digits,
                    k=6
                ))
                m = code
                mydictrandom[x] = m
                # Only for unique ones, like if x not already in mydict
                # DO YOU WANT TO SAVE ENCRYPTION DETAILS OR ACC?
                enlistrandom.append(m)

            else:
                enlistrandom.append(m)

        else:
            enlistrandom.append(mydictrandom[x])

finalenlistrandom = " ".join(enlistrandom)
print()
print("Here's your encrypted text!")
print(finalenlistrandom)
print()

def randomDn():


