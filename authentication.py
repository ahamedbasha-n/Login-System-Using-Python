def register():
    db=open("database.txt","r")
    Username=input("Create Username:")
    Password=input("Create Password:")
    Password1=input("Confirm Password:")

    d=[]
    f=[]
    for i in db:
        a,b = i.split(", ")
        b=b.strip()
        d.append(a)
        f.append(b)

    data=dict(zip(d,f))


    if Password!=Password1:
        print("Passwords don't match, restart.")
        register()
    else:
        if len(Password)<=6:
            print("Password tooo short, restart.")
            register()
        elif Username in d:
            print("Username already exists")
            register()
        else:
            db=open("database.txt","a")
            db.write(Username+", "+Password+"\n")
            print("Success!")


def access():
    db=open("database.txt","r")
    Username=input("Enter your Username:")
    Password=input("Enter your Password:")

    if not len(Username or Password)<1:
        d=[]
        f=[]
        for i in db:
            a,b = i.split(", ")
            b=b.strip()
            d.append(a)
            f.append(b)

        data=dict(zip(d,f))

        try:
            if data[Username]:
                try:
                    if Password==data[Username]:
                        print("Login Successful")
                        print("Hi,",Username)
                    else:
                        print("Username or Password is incorrect.")
                except:
                    print("Incorrect Password or Username")
            else:
                print("Username or Password doesn't exist")
        except:
            print("Username or Password doesn't exist")
    else:
        print("Please enter a value")
def home(option=None):
    option=input("Login | Sign Up : ")
    if option =="Login":
        access()
    elif option=="Sign Up":
        register() 
    else:
        print("please enter an option")

home()