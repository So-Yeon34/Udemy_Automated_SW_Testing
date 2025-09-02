# import mymodule
#import sys

# print("code.py," , __name__) #tree of import
# #print(sys.path) #check the path of "mymodule"

from mymodule import divide
#from .mymodule import divide #error : current place in, so relative import X

print(divide(15,3))
