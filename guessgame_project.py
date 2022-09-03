#Project
#Game name : Guess number

import random as r
def guessgame():
    t='y'
    score=0
    while t=='y':
        comp_num= r.randint(1,100)
        user_num=int(input("Enter the number from 1 to 100 : "))
        dif=comp_num-user_num
        if comp_num==user_num:
            score+=50
            print("Its Same number and you get 50 points\nYour updated score is %d" % (score))
        elif dif>=-5 or dif<=5:
            score+=25
            print("Your number is very near to the real number so you get 25 points\nYour updated score is %d" % (score))
        elif dif>=-10 or dif<=10:
            score+=10
            print("Your number is near to the real number so you get 10 points\nYour updated score is %d" % (score))
        elif dif>=-20 or dif<=20:
            score+=5
            print("Your number is far to the real number so you get 5 points\nYour updated score is %d" % (score))
        else:
            print("Sorry you didn't get it\nComputer number : %d\nYour input : %d" % (comp_num,user_num))
        t=input("Do you want to play again (y/n) : ")

guessgame()
    
        
