'''
D:\Learn Grow Earn\Python & AI\Python_Basics>python
Type "help", "copyright", "credits" or "license" for more information.
>>> mylist=[1,2,3,4]
>>> mylist is itera(mylist)
  File "<stdin>", line 1, in <module>
NameError: name 'itera' is not defined. Did you mean: 'iter'?
>>> mylist is iter(mylist)
False
>>> mylist.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute '__next__'. Did you mean: '__ne__'?
>>> mylist.__ne__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: expected 1 argument, got 0
>>> f=iter(mylist)
>>> f.__next__()
1
>>> f.__next__()
2
>>> f.__next__()
3
>>> f.__next__()
4
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

'''

'''
D:\Learn Grow Earn\Python & AI\Python_Basics>python
Type "help", "copyright", "credits" or "license" for more information.
>>> f is iter(f)
>>> f.__next__()
"print('file opened')\n"
>>>
>>>
>>>
>>>
>>> f.__next__()
"print('.........line one executed..........')\n"
>>> f.__next__()
'sum=None;\n'
>>> f.__next__()
"print('.........line two executed..........')\n"
>>> f.__next__()
'for i in range(0,5):\n'
>>> f.__next__()
'    sum+=i\n'
>>> f.__next__()
"print('.........Loop is executed..........')\n"
>>> f.__next__()
"print(f'sum of range(0,5)  is {sum}')\n"
>>> f.__next__()
"print('.........line End..........')"
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>

'''

'''
D:\Learn Grow Earn\Python & AI\Python_Basics>python
Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> f=set(1,2,3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: set expected at most 1 argument, got 3

D:\Learn Grow Earn\Python & AI\Python_Basics>python
Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> f=set(1,2,3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

D:\Learn Grow Earn\Python & AI\Python_Basics>python
Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> f=set(1,2,3)

D:\Learn Grow Earn\Python & AI\Python_Basics>python
Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

D:\Learn Grow Earn\Python & AI\Python_Basics>python


D:\Learn Grow Earn\Python & AI\Python_Basics>python
Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
D:\Learn Grow Earn\Python & AI\Python_Basics>python
Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Type "help", "copyright", "credits" or "license" for more information.
>>> f=set(1,2,3)
TypeError: set expected at most 1 argument, got 3
>>> f=(1,2,3)
>>> f is iter(f)
>>> f=iter(f)
Traceback (most recent call last):
AttributeError: 'tuple_iterator' object has no attribute 'next'
>>> f.readlines()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
>>> f.__next__()
1
>>> f.__next__()
2
>>> f.__next__()
3
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''

'''

D:\Learn Grow Earn\Python & AI\Python_Basics>python
>>> mylist=[1,2]
>>> i
<list_iterator object at 0x000001CF56223940>
>>> f=open('file.py)
  File "<stdin>", line 1
    f=open('file.py)
           ^
SyntaxError: unterminated string literal (detected at line 1)
>>> f=open('file.py')
>>> f
<_io.TextIOWrapper name='file.py' mode='r' encoding='cp1252'>
>>>

'''

file=open('file.py')
file2=open('file.py')
# print(f'--------------For Loop--------------\n\n')
# for line in file:
#     print(line, end='')
print(f'\n\n--------------While Loop--------------')

while True:
    f=file.readline()
    if not f:break
    print(f, end='')

print(f'\n\n--------------For Loop--------------\n\n')
for line in file2:
    print(line, end='')