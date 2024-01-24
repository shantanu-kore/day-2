def check_day(day): 
    if day <= 7 and day!=0:
        if day==1:
            print("monday")
        elif day==2:
            print("tuesday")
        elif day==3:
            print("wednesday")
        elif day==4:
            print("thursday")
        elif day==5:
            print("friday")
        elif day==6:
            print("saturday")
        else:
            print("sunday")

    else:
        print("enter day between 1 to 7")


i=0
while i==0:
    day=int(input("enter a day like 1 to 7:"))
    check_day(day)