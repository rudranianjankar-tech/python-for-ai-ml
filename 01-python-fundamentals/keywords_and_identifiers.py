#python is case sensitive language, so name and Name are different variables
#keywords
#keywords are reserved words in python that
#have a special meaning and cannot be used as identifiers (variable names, function names, etc.)

#python has 35 keywords in version 3.10, and they are:
#False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

import keyword
print(keyword.kwlist)

#Identifiers
#Identifiers are names given to variables, functions, classes, etc. in python.
#Identifiers must follow these rules:
#- They can contain letters (a-z, A-Z), digits (0-9), and underscores (_)
#- They cannot start with a digit
#- They are case sensitive
#- They cannot be keywords
#- can only start with a letter or underscore_