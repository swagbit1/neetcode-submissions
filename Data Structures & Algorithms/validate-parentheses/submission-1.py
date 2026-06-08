class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closeOpen = {
            ']':'[',
            '}':"{",
            ")":"("
        }

        for character in s:
            if character in closeOpen:
                if stack and stack[-1] == closeOpen[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)

        return True if not stack else False
            