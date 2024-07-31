import string
import random as r

def pw(n):
    
    if n>=12: 
        lower=string.ascii_lowercase
        upper=string.ascii_uppercase
        digits=string.digits
        sc="!#$%&*+,-./:;=?@\`~"

        combine=lower+upper+digits+sc
            
        r_l=r.choice(lower)
        r_u=r.choice(upper)
        r_d=r.choice(digits)
        r_sc=r.choice(sc)

        T=r_l+r_u+r_d+r_sc

        for i in range(n-4):
            T=T+r.choice(combine)

        t=[]
        for i in T:
            t.append(i)
            r.shuffle(t)
            
        password=''
        for i in t:
            password+=i
        return password
    else:
        return "Password must have minimum 12 characters"
    


while True:

    print("1 generate")
    print("2 Exit")
    choice=input("Enter choice  : ")
    if choice=="1":
        n=int(input("Enter no. of characters:"))
        print(pw(n))
        print()
    elif choice=="2":
        print("Exit")
        break
    else:
        print()
        print("Invalid choice")
        print()
    
    


        
        
    



