student_grades=[]
for i in range(int(input())):
    name=input()
    score=float(input())
    student_grades.append([name,score])
# print(student_grades)    

sorted_scores=sorted(list(set([x[1] for x in student_grades])))    
# print(sorted_scores)

second_lowest=sorted_scores[1]
low_final_list=[]
for student in student_grades:
    if second_lowest == student[1]:
        low_final_list.append(student[0])

for student in low_final_list:
    print(student)        






