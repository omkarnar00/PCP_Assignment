n=int(input("ENTER THE NUMBER :"))
a=list()
print("ENTR THE SCORE :")
for i in range(0,n):
    score=input()
    a.append(score)
print(a)   

a2=list(set(a))

a2.sort()

print("THE RUNNER_UP IS",a2[-2])
