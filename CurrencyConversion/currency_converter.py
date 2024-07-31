d={"   Country         ":"      Currency Code",
   "Indian Rupee       ":"          INR",
   "US Dollars         ":"          USD",
   "British Pounds     ":"          GBP",
   "Euros              ":"          EUR",
   "Canandian Dollar   ":"          CAD",
   "Chinese Yuan       ":"          CNY",
   "Russian Rubal      ":"          RUB"}

for key,values in d.items():
    print("{: >5}{}:{}".format(" ",key,values))
print('\r')
c1=input("which currency you want to convert : ")
print('\r')

for key,values in d.items():
    if d[key]==c1:
        continue    
    else:
        print(key," : ",values)
print('\r')
c2=input("In which you want to convert : ")

cr=float(input("Enter the conversion rates : "))

amount=float(input("Enter amount to be converted : "))
print(amount,c1,"=",amount*cr,c2)


