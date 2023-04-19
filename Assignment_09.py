n=int(input("ENTER A NUMBER : "))
if n%2==0:
    if n<=2 and n>=5:
        print("WEIRD")
    elif n<=6 and n>=20:
        print("NOT WEIRD")    
    elif n>20:
        print("NOT WEIRD")  
else:
    print("WEIRD")              