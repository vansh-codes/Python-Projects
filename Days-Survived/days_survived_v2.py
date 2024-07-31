def check(year,month,day):
    if len(str(year))==4 and len(str(month))<=2 and len(str(day))<=2:                    
        if (month<=12 and month>0) and (day<=31 and day>0):
            if leap(year,tdays,n,birth_yr,month):
                if day<=tdays[month-1]:
                    return False
                else:
                    print("Month",month,"of year",year,"had",tdays[month-1],"days")
            else:
                if day<=tdays[month-1]:
                    return False
                else:
                    print("Month",month,"of year",year,"had",tdays[month-1],"days")
        else:
            print()
            print("Date must be less than or equal to 31 and greater than 0")
            print("Month must be less than or equal to 12 and gretaer than 0")
            print()
    
    else:
        print("Please enter date of birth in DD/MM/YYYY format")


def leap(year,tdays,n,birth_yr,month):

    if year%4==0 and year%100!=0 or year%400==0:
        del tdays[1]
        tdays.insert(1,29)
        n+=tdays[month-1]
        birth_yr+=366
        return True
        
    else:        
        n+=tdays[month-1]
        birth_yr+=365
        
while True:
    print("Press 1 to Start")
    print("Press 2 to exit")
    choice=input("Enter your choice : ")
    if choice == "1" :
        n=0                    #days in the month of birth
        birth_yr=0
        tdays1=[31,28,31,30,31,30,31,31,30,31,30,31] #days in months
        n1=0  #days in the month of birth
        yr=0
        tdays=[31,28,31,30,31,30,31,31,30,31,30,31]   #days in months
        
        print("Please enter date of birth in DD/MM/YYYY format")
        while True:
            birth_date=input("Enter your date of birth : ").split("/")
            if len(birth_date)==3:
                year=int(birth_date[2])   #birth year
                month=int(birth_date[1])  #birth month
                day=int(birth_date[0])    #birth date
                if check(year,month,day)==False:
                    break
            else:
                print("Invalid Format")
                print()

        #################################################
        while True:
            date=input("Enter present date : ").split("/")
            if len(date)==3:
                year1=int(date[2])
                month1=int(date[1])
                day1=int(date[0])
                if check(year1,month1,day1)==False:
                    break
            else:
                print()
                print("Invalid Format")
                print()
                
        day_month=tdays[month-1]-day     #days in month left to live

        leap(year,tdays,n,birth_yr,month)
        days_birth_yr=0
        for i in range(month,12):
            days_birth_yr += tdays[i]

        totaldaysLeft_birth=days_birth_yr + day_month
        #print("Total left : ",totaldaysLeft_birth)
        ############################
        days_yr=0
        for i in range(0,month1-1):
            days_yr += tdays1[i]

                
        leap(year1,tdays1,n1,yr,month1)
        totaldaysLived=days_yr + (day1)
        #print("Total : ",totaldaysLived)

        total=0
        y_c=1
        
        if year<year1:
            while year+1!=year1:
                y_c+=1
                if leap(year+1,tdays,n,birth_yr,month):
                    total += 366
                    #print("Leap Add : ",year+1," ",total)
                else:
                    total+= 365
                    #print("N-Leap Add : ",total)
                year+=1
            print("TOTAL DAYS SURVIVED(year) : ",total+totaldaysLeft_birth+totaldaysLived+1)
            print("Years lived : ",y_c)
            # print("minutes lived :",1440*(total+totaldaysLeft_birth+totaldaysLived))
        elif year>year1:
            print("Date of birth must be earlier than present date")
        elif year==year1:
            totaldaysLived=0
            print(month,month1)
            if month==month1:
                ##end included
                print("TOTAL DAYS SURVIVED!!@@(end included) : ",day1-day + 1)
                print("Years lived : ",year1-year)
                # print("minutes lived :",1440*(day1-day))
            elif month>month1:
                print("Date of birth must be earlier than present date")
            else:
                ##end included
                for i in range(month,month1-1):
                    totaldaysLived += tdays[i]
                print("TOTAL DAYS SURVIVED(same)(end included) : ",totaldaysLived + (tdays[month-1]-(day-1)) + day1)
##                print("Years lived : ",year1-year)
##                print("minutes lived :",1440*(totaldaysLived + (tdays[month-1]-(day-1)) + day1))
    elif choice=="2":
        print("Exit")
        break
    else:
        print()
        print("Invalid choice")
        print()