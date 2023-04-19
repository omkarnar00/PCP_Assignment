year=int(input("ENTER A YEAR :"))
if (year%400 == 0) or (year%4==0 and year%100!=0):
    print("TRUE")
else:
    print("FALSE")    