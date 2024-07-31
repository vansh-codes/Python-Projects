name=["Vansh","Sarthak","Ritesh","Anshul","Prateek"]
contact=["1","2","3","4","5"]
n1=[]
c1=[]
def search(name,contact):
    user=input("Enter name to be searched for : ")
    if user in name:
        find=name.index(user)
        print("Contact: ",contact[find])
    else:
        print()
        print("Name not found in repository")


def display(name,contact):
    if len(name)==len(contact):
        for i in range(len(name)):
            print("Name :",name[i])
            print("Contact :",contact[i])
            print()
    else:
        print("ERROR404")

def update(name,contact):
    user=input("Enter name to be updated for : ")
    
    if user in name:
        find=name.index(user)
        c=input("Enter your contact number to get the access: ")
        if c==contact[find]:
            while True:
                print("What do you want to update?")
                print("1. Name")
                print("2. Contact number")
                print("3. Exit")
                choice=input("Enter your choice from the menu : ")
                if choice=="1":
                    update_n=input("Enter updated name : ")
                    
                    name[find]=update_n
                    print("Updated successfully")
                    print("Name : ",name[find])
                    print()
                    
                    
                elif choice=="2":
                    update_c=input("Enter updated number : ")
                    find=contact.index(c)
                    contact[find]=update_c
                    print("Updated successfully")
                    print("Contact : ",contact[find])
                    print()

                elif choice=="3":
                    break
            
        else:
            print("Incorrect Contact number")
    else:
        print("Name not found in repository")

def add(name,contact):
    while True:
        new_n=input("Enter Name : ")
        new_c=input("Enter Contact number : ")
        name.append(new_n)
        contact.append(new_c)
        print("Added Successfully")
        ch=input("Do you want to add more? (yes/no): ")
        if ch=="yes" or ch=="Yes":
            continue
        else:
            break
        
    
def delete(name,contact):
    user=input("Enter name to be deleted for : ")
    if user in name:
        find=name.index(user)
        c=input("Enter your contact number to get the access: ")
        if c==contact[find]:
            print("Enter yes if you are sure")
            sure=input("Type 'yes' to confirm delete : ")
            if sure=="yes" or sure=="Yes":
                del name[find]
                del contact[find]
                print("Deleted Successfully")
            else:
                pass
        else:
            print("Incorrect Contact number")
    else:
        print("Name not found in repository")
        
def multiple(name,contact,n1,c1):

    n1.clear()
    c1.clear()
    while True:
        m=input("Enter name : ")
        if m in name:
            n1.append(m) 
            ch=input("Do you want to add more(yes/no): ")
            if ch=="yes":
                continue             
            else:
                break
        else:
            print("Name",m,"not found in the repository")
            
    for i in range(len(n1)):
        find=name.index(n1[i])
        c1.append(contact[find])
     
while True:
    print("Press 1 to search in the repositary")
    print("Press 2 to display the repositary")
    print("Press 3 to update the repository")
    print("Press 4 to add data to repository")
    print("Press 5 to delete data from repository")
    print("Press 6 to extract multiple contacts")
    print("Press 7 to exit")
    print()
    choice=input("Enter your choice from the menu : ")
    if choice=="1":
        print()
        search(name,contact)
        print()
    elif choice=="2":
        print()
        display(name,contact)
        print()
    elif choice=="3":
        print()
        update(name,contact)
        print()
    elif choice=="4":
        print()
        add(name,contact)
        print()
    elif choice=="5":
        print()
        delete(name,contact)
        print()
    elif choice=="6":
        print()
        multiple(name,contact,n1,c1)
        print()
        display(n1,c1)
        print()
    elif choice=="7":
        print("Exit successful")
        break
    else:
        print()
        print("Invalid choice")
        print("Please choose from the menu")
        print()
