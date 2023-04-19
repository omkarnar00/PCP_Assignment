num_student=int(input("ENTER THE NUMBER OF STUDENTS : "))

for num in range(0,num_student):
    students={}
    marks=[]
    name=input("ENTER THE NAME OF STUDENTS : ")

    n=int(input("ENTER THE NO OF  MARKS TO BE ENTERED  : "))
    for i in range(0,n):
        l=int((input("ENTER THE MARKS : ")))
        marks.append(l)
    students[name]=marks
print(students.items())    

for key,value in students.items():    
    print(key,":",value)    


query_name=input("ENTER THE NAME OF STUDENT ")
sum=0
if query_name in students.keys():
    for i in students.values():
        for x in i:
            sum+=x(num)
avg=sum/n
print(avg)





