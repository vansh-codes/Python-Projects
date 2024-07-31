""" print("*****   INT108 - Python Programming   *****")
print("*********    Project 15    *********")
print() """

prime=[]                                      #list of prime numbers
comp=[]                                       #list of composite numbers

prime_count=0                                 #count of prime numbers
comp_count=0                                  #count of composite numbers

def start(n,m,prime,comp,x,y): #functn which finds prime&comp num in the range and append to their respective lists

    prime.clear()
    comp.clear()
    
    global prime_count
    global comp_count
    for i in range(n,m+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:                  
                    comp.append(i)
                    break
            else:
                prime.append(i)

def one(n):       #function which checks 0 and 1 and the range is of positive integers
    if n==0:
        print("0 & 1 is neither prime nor composite")
        print()
        return True
    if n==1:
        print("1 is neither prime nor composite")
        print()
        return True  

        
def primef():   #function which prints prime num and its count
    prime_count=0
    for i in prime:
        print(i,end=" ")
        prime_count+=1
    print()
    print("There are total",prime_count,"prime numbers in the given range",n,"-",m)
    print()
    
def compf():   #function which prints composite num and its count
    comp_count=0
    for j in comp:
        comp_count+=1
        print(j,end=" ")
    print()
    print("There are total",comp_count,"composite numbers in the given range",n,"-",m)
    print()

while True:              #main menu
    print("Press '1' to Start")
    print("Press '2' to exit")
    print()
    user=input("Enter your choice from the above Menu: ")
    print()
    
    if user=="1":
        while True:
            while True:
                n=input("Enter lower limit of the range: ")
                if n.isdigit():
                    n=int(n)
                    break
                else:
                    print("Please enter appropriate digits :: characters and special characters are not allowed")
                    print()
                    continue
            while True:
                m=input("Enter upper limit of the range: ")
                if m.isdigit():
                    m=int(m)
                    break
                else:
                    print("Please enter appropriate digits :: characters and special characters are not allowed")
                    print()
                    continue
                print()
        
            if n-m>=0:
                print("Invalid range")
                print("Upper limit cannot be less than or equal to lower limit")
                print()
            else:
                break
        
        start(n,m,prime,comp,prime_count,comp_count)
        print()
        while True:            #menu to perform operations on the range
            print("Press 'a' to Display Prime")
            print("Press 'b' to Display Composite")
            print("Press 'c' to Display Both")
            print("Press 'd' to go Back to Main Menu")
            print()
            u=input("Enter your choice from the Menu: ")
            print()
            if u in "aA":
                if one(n)==False:
                    break
                primef()
            elif u in "Bb":
                if one(n)==False:
                    break
                compf()
            elif u in "Cc":
                if one(n)==False:
                    break
                primef() 
                compf()
            elif u in "Dd":
                print()
                break
            else:
                print("Invalid choice")
                print()

            c=input("Do you want to continue with same limits [Press 'Y' for Yes/Any other key for No]: ")
            print()
            if c in "yY":
                continue
            
            else:
                print()
                break
            
    elif user=="2":
        # print("INT108 Project by")
        # print("- Vansh Chaurasiya")
        # print("Roll.No : RK22WBB59")
        break 

    else:
        print("Invalid input")
        print()