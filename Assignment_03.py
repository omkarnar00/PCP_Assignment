no_eng=int(input("ENTER THE NUMBER OF STUDENT WHO SUBSCRIBED ENGLISH : "))
eng=set()
for i in range(0,no_eng):
    s=int(input("ENTER THE ROLL nUMBERS OF STUDENTS :"))
    eng.add(s) 

no_fre=int(input("ENTER THE NUMBER OF STUDENT WHO SUBSCRIBED ENGLISH : "))
fre=set()
for i in range(0,no_fre):
    s=int(input("ENTER THE ROLL nUMBERS OF STUDENTS :"))
    fre.add(s)    

print(len(eng.intersection(fre)))          