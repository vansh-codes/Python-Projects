s1=int(input("Enter first side of a triangle : "))
s2=int(input("Enter second side of a triangle : "))
s3=int(input("Enter third side of a triangle : "))

if s1==s2==s3:
    print("Triangle is a Equilateral Triangle")
elif s1!=s2 and s2!=s3 and s1!=s3:
    print("Triangle is a Scalene Triangle")
elif s1==s2 or s2==s3 or s1==s3:
    print("Traingle is a Isosceles Traingle")
