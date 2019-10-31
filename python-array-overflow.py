# a python program to demo buffer overflow
buffer=[None]*5

numloop=int(input("Enter a number for how many loops: "))
for i in range (0,numloop):
  test=int(input("type any number: "))
  buffer[i]=test


#Enter a number for how many loops: 6
#type any number: 2
#type any number: 3
#type any number: 4
#type any number: 5
#type any number: 6
#type any number: 7
#Traceback (most recent call last):
#  File "python-array-overflow.py", line 7, in <module>
#    buffer[i]=test
#IndexError: list assignment index out of range
