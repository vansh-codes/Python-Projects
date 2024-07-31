n=input("Enter a string : ")
string=""
for i in n:
    if i.isalpha():
        encrypt=ord(i)+4
        string+=str(chr(encrypt))
print(string)