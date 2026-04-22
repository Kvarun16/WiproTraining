'''
n=int(input())
s=0
for i in range(1,n+1):
    s=s+i**2
print(s)
'''

n=int(input("Enter how many *"))

for _ in range(1,n+1):
    print('*',sep=' ',end='\t')