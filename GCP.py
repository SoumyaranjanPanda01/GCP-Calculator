n=int(input("Enter Amount: "))
print("Oh Nice, For what time period you wanna invest?")
def menu():
    print("[1]3year")
    print("[2]5year")
    print("[3]7year")
    print("[4]10year")
    
menu()
option = int(input())
if option ==1:
    print("What would be your Investment plan?")
    def menu():
        print("[1]Montly")
        print("[2]Yealy")
        print("[3]Maturity")
    menu()
    option = int(input())
    if option ==1:
        t1=(n*(1.25/100))*36
        print("your profit after the maturity period would be",t1)
    elif option ==2:
        t2=(n*(16/100))*3
        print("your profit after the maturity period would be",t2)
    elif option ==3:
        t3=(n*(54/100))
        t4=(n*(4.5/100))
        t5=t3+t4
        print("your profit after the maturity period would be",t3,"and bonus would be",t4,"total = ",t5)
elif option ==2:
    print("What would be your Investment plan?")
    def menu():
        print("[1]Montly")
        print("[2]Yealy")
        print("[3]Maturity")
    menu()
    option = int(input())
    if option ==1:
        f1=(n*(1.5/100))*60
        print("your profit after the maturity period would be",f1)
    elif option ==2:
        f2=(n*(19/100))*5
        print("your profit after the maturity period would be",f2)
    elif option ==3:
        f3=(n*(105/100))
        f4=(n*(7.5/100))
        f5=f3+f4
        print("your profit after the maturity period would be",f3,"and bonus would be",f4,"total = ",f5)
elif option ==3:
    print("What would be your Investment plan?")
    def menu():
        print("[1]Montly")
        print("[2]Yealy")
        print("[3]Maturity")
    menu()
    option = int(input())
    if option ==1:
        s1=(n*(1.75/100))*84
        print("your profit after the maturity period would be",s1)
    elif option ==2:
        s2=(n*(22/100))*7
        print("your profit after the maturity period would be",s2)
    elif option ==3:
        s3=(n*(168/100))
        s4=(n*(10.5/100))
        s5=s3+s4
        print("your profit after the maturity period would be",s3,"and bonus would be",s4,"total = ",s5)
elif option ==4:
    print("What would be your Investment plan?")
    def menu():
        print("[1]Montly")
        print("[2]Yealy")
        print("[3]Maturity")
    menu()
    option = int(input())
    if option ==1:
        e1=(n*(2/100))*120
        print("your profit after the maturity period would be",e1)
    elif option ==2:
        e2=(n*(25/100))*10
        print("your profit after the maturity period would be",e2)
    elif option ==3:
        e3=(n*(270/100))
        e4=(n*(15/100))
        e5=e3+e4
        print("your profit after the maturity period would be",e3,"and bonus would be",e4,"total = ",e5)
