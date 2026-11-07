class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star_stack = []
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == "*":
                star_stack.append(i)
            else:
                if not stack and not star_stack:
                    return False
                if stack:
                    stack.pop()
                else:
                    star_stack.pop()
        
        while stack and star_stack:
            if stack.pop() > star_stack.pop():
                return False
        return not stack


        