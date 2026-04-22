Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
s1
'hello'
type(s1)
<class 'str'>
s1.lower()
'hello'
s1.upper()
'HELLO'
s1.count('l')
2
s1.count('h')
1
s1.count('o')
1
s1.count('s')
0
s1.endswith('o)
            
SyntaxError: unterminated string literal (detected at line 1)
s1.endswith('o')
            
True
s1.endswith('o')
            
True
s1.isalpha()
            
True
s1.replace('L','l')
            
'hello'
s1='Hi Hello How Are You'
            
s1.split( )
            
['Hi', 'Hello', 'How', 'Are', 'You']
s1.swapcase()
            
'hI hELLO hOW aRE yOU'
s1[1]
            
'i'
s1[0:10]
            
'Hi Hello H'
s1[-10:-2]
            
'ow Are Y'
>>> s1[-10::-2]
...             
'o le H'
>>> s1="hello"
...             
>>> it =iter(s1)
...             
>>> for i in it:
...             print(i)
... 
...             
h
e
l
l
o
