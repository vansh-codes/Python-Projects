n=int(input("n: "))
print("Multiplication of 1")
for i in range(1,n+1):
    print("Multiplication of ",i)    
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))
    print()