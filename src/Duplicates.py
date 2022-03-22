l = []
while(1):
    a = int(input("Enter number : "))
    try:
        if a not in l and len(str(a)) == 2:
            l.append(a)
        else:
            raise Exception
    except:
        print("Duplicates are not allowed and number should have 2 digits")
        break