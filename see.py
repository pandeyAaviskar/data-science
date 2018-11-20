def gpa(x):
    if x ==4:
        return 'A+'
    elif x >=3.6 and a<4:
        return 'A'
    elif x >=3.2 and x<3.6:
        return 'B+'
    elif x >=2.8 and x<3.2:
        return 'B'
    elif x >=2.4 and x<2.8:
        return 'C+'
    elif x >=2 and x<2.4:
        return 'C'
    elif x >=1.6 and x<2:
        return 'D'
    elif x >=0.8 and x<1.6:
        return 'E'
    else: 
        return 'N'
def compare(x):
    if x>100:
        print('\n error')
    elif x>=90 and x<100:
        return 4.0
    elif x>=80 and x<90:
        return 3.6
    elif x>=70 and x<80:
        return 3.2
    elif x>=60 and x<70:
        return 2.8
    elif x>=50 and x<60:
        return 2.4
    elif x>=40 and x<50:
        return 2.0
    elif x>=20 and x<40:
        return 1.6
    elif x>=1 and x<20:
        return 0.8
    else:
        return 0
marks=0
num=0
tpSum=[]
while num==0:
    print('---FOR SUBJECTS WITH THEORY AND PRACTICAL---')
    theoryPrac=[int(input('enter the marks of theory: '))]
    theoryPrac.append(int(input('enter the marks of pracrical: ')))
    marks=sum(theoryPrac)
    print("you scored: ",marks)
    tpSum.append(compare(marks))
    print("\n and the respective grade is: ",tpSum)
    
    num=int(input('enter 0 to continue with subject with practical or else 1 to end :'))

num=0
print('/n')
while num==0:
    print('\n---FOR SUBJECTS WITH ONLY THEORY---\n')
    theory=compare(int(input('enter the marks of theory: ')))   
    tpSum.append(theory)
    num=int(input('enter 0 to continue with subject with only theory or else 1 to end the program:'))
if len(tpSum)>8:
    print('INVALID- entry overflooded ')
elif len(tpSum)<8:
    print('INVALID- entry insufficient')
else:
    totalSum=round((sum(tpSum)/8),2)
    print('--------CONGRATULATION--------\n')
    print('your final grade is ',totalSum)
    print('\n your GPA is ',gpa(totalSum))














    

