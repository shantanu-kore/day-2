import random
import sys
random_num=random.randint(1,100)
print("random number is:",random_num)

max_trial=6

for x in range(1,max_trial+1):
    number=int(input("guess a number between 1 to 100:"))
    if number == random_num:
        print("'you won'")
        sys.exit("your number matches the random number")
    elif number < random_num:
        print("too low")             
    else:
        print("too high")


else:
    print("'computer won'")
    sys.exit("you have reached max limits")