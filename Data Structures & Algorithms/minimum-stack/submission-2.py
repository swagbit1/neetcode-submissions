class MinStack:
    """
    the weird input and output format is just the leet code
    because it does not support work around classes so it must be explictlitly said
    
    we are build a stack and its operations
    the main thing here is the get min and keeping track of it the min
    when pop occurs, thats what makes this s O(n) and O(1) look ups, 
    using stacks and a array to keep track of the minimum


    """
    

    def __init__(self):
        self.minHistory = []
        self.stack = []
        

    def push(self, val: int) -> None:

        if len(self.minHistory) > 0:
            self.stack.append(val)
            if val <= self.minHistory[-1]:
                self.minHistory.append(val)
            else:
                self.minHistory.append(self.minHistory[-1])
        else:
            self.stack.append(val)
            self.minHistory.append(val)

        

    def pop(self) -> None:
        if self.stack and self.minHistory:
            self.stack.pop()
            self.minHistory.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minHistory[-1] if self.minHistory else 0
        
