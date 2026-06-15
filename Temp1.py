RAW = input("Enter the Encrypted text : ")

delist = []
for i in RAW:
    if i in mark1:
        for keys, values in mark1.items():
            if keys == i:
                delist.append(values)
            else:
                continue
    else:
        delist.append(i)
