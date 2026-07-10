print("===== Challange Game =====")
print("Guess the correct number\n")
n = int(input("Enter Your first guess from 1 to 50 (5 lives left)"))
while n >7 or n <9:
    if n == 8:
        print("You Won well done")
    elif n <20  :
        print("You are close its under 20  ")
        int(input("Enter your next guess"))
    elif n >=30:
        print("You should decrese")
        int(input("enter your next guess"))
        
    elif n >=40:
        print("This number is a multiple of 2")
        int(input("enter your next guess"))
    elif n >=50:
        print("This is an even number")
        int(input("enter your next guess"))
    elif n <50:
        print("Its the 2nd jersey number of virat kholi")
        int(input("enter your last guess"))
    else:
        print("You lose it was 8")
    i = 5
   
    




    

    
           


