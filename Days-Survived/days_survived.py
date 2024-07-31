#date entered should be correct as per month
#month should be till 12

print("Please enter date of birth in DD-MM-YYYY format")
birth_date=input("Enter your date of birth : ").split("-")
##print(date)
year=int(birth_date[2])   #birth year
##print(year)
##print(type(year))
month=int(birth_date[1])  #birth month
day=int(birth_date[0])       #birth date
##print("month : ",month)
tdays=[31,28,31,30,31,30,31,31,30,31,30,31] #days in months
n=0  #days in the month of birth
birth_yr=0

#################################################
date=input("Enter present date : ").split("-")
year1=int(date[2])
month1=int(date[1])
day1=int(date[0])
tdays1=[31,28,31,30,31,30,31,31,30,31,30,31] #days in months
n1=0  #days in the month of birth
yr=0

    
def leap(year,tdays,n,birth_yr,month):
##    global tdays
##    global n             
##    global birth_yr
##    global tdays1
##    global n1
##    global yr
    if year%4==0 and year%100!=0 or year%400==0:
        #tdays.remove(28)
        del tdays[1]
        tdays.insert(1,29)
        ##print("L: ",tdays)
        n+=tdays[month-1]
        birth_yr+=366
        return True
        ##return "Leap"
    else:
        ##print("NL : ",tdays)
        n+=tdays[month-1]
        birth_yr+=365
        ##return "nl"

##leap(year,tdays,n,birth_yr,month)
##print(n)
##print(birth_yr)
day_month=tdays[month-1]-day     #days in month left to live
##print(day_month)


leap(year,tdays,n,birth_yr,month)
days_birth_yr=0
for i in range(month,12):
    days_birth_yr += tdays[i]
    ##print("LD : ",days_birth_yr)
        
##leap(year,tdays,n,birth_yr,month)
totaldaysLeft_birth=days_birth_yr + day_month
#print("Total : ",totaldaysLeft_birth)

##################################
##print("Current month : ",month1)
##leap(year1,tdays1,n1,yr,month1)
days_yr=0
for i in range(0,month1-1):
    days_yr += tdays1[i]
    #print("Check : ",days_yr)
        
leap(year1,tdays1,n1,yr,month1)
totaldaysLived=days_yr + (day1)
print("Total : ",totaldaysLived)

total=0
if year<year1:
    while year+1!=year1:
        if leap(year+1,tdays,n,birth_yr,month):
            total += 366
            print("Leap Add : ",year+1," ",total)
        else:
            total+= 365
            print("N-Leap Add : ",total)
        year+=1
    print("TOTAL DAYS SURVIVED(ok) : ",total+totaldaysLeft_birth+totaldaysLived+1)
elif year>year1:
    print("Birth of birth must be earlier than present date")
elif year==year1:
    totaldaysLived=0
    print(month,month1)
    if month==month1:
        print("TOTAL DAYS SURVIVED!! : ",day1-day)      ##tdays[month1-1]-tdays[month-1]
    else:
        for i in range(month,month1-1):
            totaldaysLived += tdays[i]
            print("Year : ",totaldaysLived)
    #print("month lived days : ",totaldaysLived,"+ Birth month left days : ",tdays[month-1],day,tdays[month-1]-day,"+ days of month : ",day1)
        print("TOTAL DAYS SURVIVED(same) : ",totaldaysLived + (tdays[month-1]-(day-1)) + day1)
elif month==month1:
    print("TOTAL DAYS SURVIVED!! : ",tdays[month1-1]-tdays[month-1])

