# Project:          Exercise 4-1
# Purpose:          prompts user for password and validates
# Author:           Richard Barnes iii


import re
passWord= input("Input your password:   ")
var = True
while var:  
    # Sets limit and Max legnth of password
    if (len(passWord)<6 or len(passWord)>20):
        break
    # password must contain a lower case letter
    elif not re.search("[a-z]",passWord):
        break
    #password must contain a number
    elif not re.search("[0-9]",passWord):
        break
    # password must contain a upper case
    elif not re.search("[A-Z]",passWord):
        break
    # password must contain speicial char
    elif not re.search("[!#%&*$#@]",passWord):
        break
    elif re.search("\s",passWord):
        break
    else:
        print("Valid Password")
        var=False
        break
# password does not meet criteria
if var:
    print("Not a Valid Password")