#############################################################################################
# Author: Dostonbek Toirov
#
#############################################################################################
# Problem: Given a sequence of brackets, how will you identify if it is valid or not.
# Taken from: geeksforgeeks.org - Google STEP Interview Experience
# Big O: O(n)
#############################################################################################

brackets = "({[][]})"                      # input set of brackets
stack = []                                  # stack used to store the opening brackets so as to match them with closing brackets

def bracket_validation(brackets):
    stack.append("#")                       # marking the bottom of the stack   
    for i in brackets:  
        if i == "(":                        # if opening bracket is encountered
            stack.append(i)                 # put it into stack
        elif i == "{":                      # if opening bracket is encountered
            stack.append(i)                 # put it into stack
        elif i == "[":                      # if opening bracket is encountered
            stack.append(i)                 # put it into stack
        elif i == ")" and stack[-1] == "(": # if closing bracket is encounterd and matches the opening bracket on top of the stack
            del stack[-1]                   # remove the opening bracket from the stack
        elif i == "}" and stack[-1] == "{": # if closing bracket is encounterd and matches the opening bracket on top of the stack
            del stack[-1]                   # remove the opening bracket from the stack
        elif i == "]" and stack[-1] == "[": # if closing bracket is encounterd and matches the opening bracket on top of the stack
            del stack[-1]                   # remove the opening bracket from the stack
        else:
            return False                    # if none of the above works, then return False

output = bracket_validation(brackets)       # call to the function

if output == False:                         # if the output is False, 
    print("Invalid")                        # then the sequence of brackets is invalid
else:                                       # else
    print("Valid")                          # it is valid


