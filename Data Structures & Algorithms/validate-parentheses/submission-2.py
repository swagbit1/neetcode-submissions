class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closeOpen = {
            ']':'[',
            '}':"{",
            ")":"("
        }

        #{()()[({[((()))]})]}
        # check if character in s, the closing one per the key, other wise it must be open so append that
        # it will check until a closing index and since the open of that is in the top of the stack
        # we check if it matches and then pop it, in the event that its true
        # then the stack will be empty at the end, if it is not then it is missing
        # a closing or an opeing bracket, effectively making this right 
        for character in s:
            if character in closeOpen:
                if stack and stack[-1] == closeOpen[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)

        return True if not stack else False
            