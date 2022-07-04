import sys

try:
    x= int(input("x= "))
    y= int(input("y= "))
except ValueError:
    print ("only number accepted !")
try:
    result = x / y
    print (f"{x} / {y} = {result}")
except ZeroDivisionError:
    print ("cannot devise by zero !")
    
    # esm el exeption jebneha mn el exeption elly fi terminal 
    # '''
    # Traceback (most recent call last):
    # File "c:\Users\rabi3\Desktop\GIT\POO_with_Python\exeptions.py", line 7, in <module>
    #     result = x / y
    # ZeroDivisionError: division by zero
    # '''