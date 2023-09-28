inp = int(input("Enter some year\n"))
if not inp % 4:
    if not((inp % 100) and (inp % 400)):
        print("This year is leap")
    else:
        print("This year isn't leap")
else:
    print("This year isn't leap")