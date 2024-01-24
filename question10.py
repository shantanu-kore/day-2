import random
import sys
random_num=random.randint(1,100)
print("random number is:",random_num)
while True:
    number=int(input("enter a number between 1 to 100:"))
    if number == random_num:
        sys.exit(" your number matches the random number")
    elif number < random_num:
        print("too low")             
    else:
        print("too high")

