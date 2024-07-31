import random as R
score=0
print("Guess the Number")
print("RULES : ")
print("You have 3 tries to guess the number")
print("You can play multiple times to increase your score")
print("You get 15 points if you guess in 1 try")
print("You get 10 points if you guess in 2 try")
print("You get 5 points if you guess in 3 try")
print("------------------****------------------")
print("\r")
while True:
    print("Press P to play")
    print("Press any other key to exit")
    play=input("Do you want to play : ")
    print('\r')
    if play in "pP":
        l=int(input("Enter lower limit of the range : "))
        u=int(input("Enter upper limit of the range : "))
        r=R.randint(l,u)
        tries=3
        count=0
        while True:
            print('\r')            
            guess=int(input("Guess the number : "))
            if guess==r:
                count+=1
                if count==1:
                    score+=15
                elif count==2:
                    score+=10
                else:
                    score+=5
                print("Congratulations! You guessed the number in",count,"tries")
                print("Your score :",score)
                print('\r')
                break
            if guess>r:
                print("Try again! Your guess was high")
                count+=1
                tries-=1
                print(tries,"tries left")
            elif guess<r:
                print("Try again! Your guess was low")
                count+=1
                tries-=1
                print(tries,"tries left")
            if tries==0:
                print("You loose")
                print("The number was ",r)
                print("Your score :",score)
                print('\r')
                break
    else:
        print("Your final score : ",score)
        break
