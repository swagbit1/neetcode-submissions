class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closeToOpen = {
            ']':'[',
            '}':'{',
            ')':'('
        }

# ({[]})
        for char in s:
            print(char)
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    print(stack.pop())
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False
