
# a decorator is a function take a function modified her by adding a capaility
#to it then give back an output
from textwrap import wrap


def announce (f):
    def wrapper():
        print ("Aout to run the function...")
        f()
        print("Done with the function.")
    
    return wrapper

# to add a decorator we need to add @ befor the decorator function call
@announce
def hello():
    print("Hello world")

hello ()