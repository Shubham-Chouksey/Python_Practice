Number_of_students = int(input())
student_marks = {}

for i in range(Number_of_students):
    name,*line = input().split()
    scores = list(map(float,line))
    student_marks[name] = scores

query_name = input()

query_name_list = student_marks[query_name]
avg_query_result = sum(query_name_list)/3
print(format(avg_query_result,".2f"))


#=================================================================================

Total_Students = int(input())

students = []

for i in range(Total_Students):
    name = input()
    score = float(input())
    students.append([name,score])
    """students.remove(min(students,key= lambda x:x[1]))"""

def sorted_stud(students):
    t = min(students,key= lambda x:x[1])
    """"print(students)"""
    """print(t[1])"""
    """k = []"""
    l = []
    for z in students:
        if z[1] != t[1]:
            l.append(z)
    q=min(l,key=lambda x:x[1])
    l.sort()
    for x in l:
        if x[1] == q[1]:
            print(x[0])


sorted_stud(students)

##Input =5   output =Berry
#Harry                Harry
#37.21
#Berry
#37.21
#Tina
#37.2
#Akriti
#41
#Harsh
#39


#==================================================================================================

def is_leap(year):
    leap = False

    if year%4 == 0:
        leap = True
        if year%100 == 0 and year%400 != 0:
            leap = False
    return leap

year = int(input())
print(is_leap(year))

#======================================

L = ''
for y in range(1,int(input())+1):
    L += str(y)

print(L)

#========================================

#second most number in the array input

def make_integer(n):
    return int(n)

length = input()
x = input()

if len(x) == 1:
    print(x)
else:
    y = set(map(make_integer,x.split()))
    t = sorted(y,reverse=True)[1]
    print(t)