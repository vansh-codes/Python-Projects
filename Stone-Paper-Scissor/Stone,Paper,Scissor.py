import random
u_sc=0
cpu=0

def win():
    global u_sc
    print("CPU chose",r)
    print("You Win")
    print()
    u_sc+=1
    
def loose():
    global cpu
    print("CPU chose",r)
    print("You loose")
    print()
    cpu+=1
def tie():
    print("Tie")
    print()

while True:
    ch=["Stone","Paper","Scissor"]
    r=random.choice(ch)
    print("Stone,Paper,Scissor Game by Vansh")
    print("Press 'St' for Stone: ")
    print("Press 'P' for Paper: ")
    print("Press 'Sc' for Scissor: ")
    print("Press E to Quit Game")
    u=input("Make a choice : ")
    if u=="St" or u=="st" or u=="ST" or u=="sT":
        if r=="Stone":
            tie()
        elif r=="Paper":
            loose()
        elif r=="Scissor":
            win()


    elif u=="P" or u=="p":
        if r=="Stone":
            win()
        elif r=="Paper":
            tie()
        elif r=="Scissor":
            loose()


    elif u=="Sc" or u=="sc" or u=="SC" or u=="sC":
        if r=="Stone":
            loose()
        elif r=="Paper":
            win()
        elif r=="Scissor":
            tie()

    elif u=="e" or u=="E":
        print()
        print("Your Score:",u_sc)
        print("CPU's Score:",cpu)
        if u_sc==cpu:
            print("Its a Tie")
        elif u_sc>cpu:
            print("Congratulation!!You WIN")
        elif u_sc<cpu:
            print("Try Again! You Loose"
                  )
        break
    else:
        print("Invalid input")
        
