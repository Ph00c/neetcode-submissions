"""
string of parenthesis 

put it on the stack if it's open and pop it if it matches?

"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for item in s:

            if item == "(" or item == "{" or item == "[":
                stack.append(item)
            elif item == ")" and  stack != [] and stack[-1] == "(" :
                stack.pop()     
            elif item == "}" and stack != [] and stack[-1] == "{":
                stack.pop()     
            elif item == "]" and stack != [] and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(item)
        return True if stack == [] else False