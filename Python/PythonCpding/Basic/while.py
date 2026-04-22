
'''
num=int(input("Enter number"))
value=1
s=0
while value<=num:
    print(value)
    value+=1
 '''

number=input("Enter number")
count =(len(number))
s=0
ni=int(number)
t=ni
while ni>0:
    r=ni%10
    s=s+r**count
    ni=ni//10
if t==s:
    print(s,"is Armstrong")
else:
    print(s,"is Not Armstrong")
