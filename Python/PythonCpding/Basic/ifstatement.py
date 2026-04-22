"""
Date: 22-04-2026
Desc: Diff If statements
"""


#big2

'''
Firstnumber=int(input("Enter the number"))
Secondnumber=int(input("Enter the number"))
if Firstnumber==Secondnumber:
    print(Firstnumber,"and",Secondnumber,"is equal")
elif Firstnumber>Secondnumber:
    print(Firstnumber,"Is Bigger")
else:
    print(Secondnumber,"Is Bigger")
'''

#big3
'''
Firstnumber=int(input(("Enter a Number")))
Secondnumber=int(input(("Enter a Number")))
Thirdnumber=int(input(("Enter a Number")))
if Firstnumber==Secondnumber==Thirdnumber:
    print("All are Equal")
elif Firstnumber>Secondnumber and Firstnumber>Thirdnumber:
    print(Firstnumber,"Is Greater")
elif Secondnumber>Firstnumber and Secondnumber>Thirdnumber:
    print(Secondnumber,"Is greater")
else:
    print(Thirdnumber,"Is greater")
'''

#Switch Weekday

n=int(input("Enter a Number"))

match (n):
    case 1:
        print('monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case 7:
        print('Sunday')
    case _:
        print('Invalid')




