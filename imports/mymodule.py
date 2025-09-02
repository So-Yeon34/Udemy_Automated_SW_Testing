from libs import mylib
#from .libs import mylib #relative import error
def divide(devidend, divisor):
    return devidend/divisor

print("mymodule.py: ", __name__) #__name__ means global variable