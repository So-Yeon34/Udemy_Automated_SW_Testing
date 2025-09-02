print("operator.py: ", __name__)

from..mylib import * 
#..: It just skips the parent folder and goes up to the next one (two level depth)
'''
The * means "import everything", so all variables, functions, 
and classes defined inside defined inside ..mylib will be available as local variables, functions 
and classes.
'''