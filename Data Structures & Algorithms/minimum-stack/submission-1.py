
# ============================================================
# LEETCODE: MIN STACK (MEDIUM)
# ============================================================
#
# PROBLEM:
# Design a stack supporting these operations in O(1) time:
#
# push(val) -> Add a value to the top
# pop()     -> Remove the top value
# top()     -> Return the top value
# getMin()  -> Return the smallest value currently in the stack
#
# ------------------------------------------------------------
# MAIN IDEA: USE TWO STACKS
# ------------------------------------------------------------
#
# 1. stack:
#    Stores all the actual values we push.
#
# 2. minHistory:
#    Stores the minimum value of the stack at EACH position.
#
# WHY?
# Normally, finding the minimum using min(stack) takes O(n)
# because we need to search every element.
#
# Instead, we remember the minimum every time we push.
# This lets us retrieve the minimum in O(1).
#
# ------------------------------------------------------------
# EXAMPLE 1: PUSHING VALUES
# ------------------------------------------------------------
#
# Start:
# stack      = []
# minHistory = []
#
# push(5):
# stack      = [5]
# minHistory = [5]        # 5 is the only value
#
# push(3):
# stack      = [5, 3]
# minHistory = [5, 3]     # 3 is smaller than 5
#
# push(7):
# stack      = [5, 3, 7]
# minHistory = [5, 3, 3]  # 7 > 3, so minimum stays 3
#
# push(1):
# stack      = [5, 3, 7, 1]
# minHistory = [5, 3, 3, 1]  # 1 becomes new minimum
#
# IMPORTANT:
# minHistory does NOT store the values being pushed.
# It stores the smallest value seen UP TO each position.
#
# ------------------------------------------------------------
# EXAMPLE 2: POPPING VALUES
# ------------------------------------------------------------
#
# Before:
# stack      = [5, 3, 7, 1]
# minHistory = [5, 3, 3, 1]
#
# pop() -> removes the last element from BOTH lists
#
# After:
# stack      = [5, 3, 7]
# minHistory = [5, 3, 3]
#
# getMin() -> 3
#
# pop() again:
# stack      = [5, 3]
# minHistory = [5, 3]
#
# getMin() -> 3
#
# pop() again:
# stack      = [5]
# minHistory = [5]
#
# getMin() -> 5
#
# KEY INSIGHT:
# Popping from BOTH stacks automatically restores
# the previous minimum. No searching is needed!
#
# ------------------------------------------------------------
# EXAMPLE 3: DUPLICATE MINIMUM VALUES
# ------------------------------------------------------------
#
# push(4), push(2), push(2), push(8)
#
# stack      = [4, 2, 2, 8]
# minHistory = [4, 2, 2, 2]
#
# pop() -> removes 8
# stack      = [4, 2, 2]
# minHistory = [4, 2, 2]
# getMin() -> 2
#
# pop() -> removes one 2
# stack      = [4, 2]
# minHistory = [4, 2]
# getMin() -> 2
#
# pop() -> removes the other 2
# stack      = [4]
# minHistory = [4]
# getMin() -> 4
#
# Duplicate minimums are handled automatically.
#
# ============================================================
# SOLUTION
# ============================================================

class MinStack:

    def __init__(self):
        # Regular stack stores the actual values.
        self.stack = []

        # Stores the minimum at every position.
        # Both lists always have the same length.
        self.minHistory = []

    def push(self, val: int) -> None:

        # CASE 1: This is the first element.
        # Since nothing exists yet, val is the minimum.
        if len(self.minHistory) == 0:
            self.stack.append(val)
            self.minHistory.append(val)

        # CASE 2: The stack already contains elements.
        else:
            # Always add the value to the regular stack.
            self.stack.append(val)

            # Compare val with the CURRENT minimum,
            # which is the last element of minHistory.
            if val <= self.minHistory[-1]:

                # New value is smaller or equal.
                # It becomes the current minimum.
                self.minHistory.append(val)

            else:
                # New value is larger.
                # Keep the previous minimum.
                self.minHistory.append(self.minHistory[-1])

        # Example:
        # Before:
        # stack      = [5, 3]
        # minHistory = [5, 3]
        #
        # push(7):
        # stack      = [5, 3, 7]
        # minHistory = [5, 3, 3]
        #
        # Time: O(1) amortized


    def pop(self) -> None:

        # Remove the last element of BOTH lists.
        # This keeps the stack and minimum history synchronized.
        self.stack.pop()
        self.minHistory.pop()

        # Example:
        # Before:
        # stack      = [5, 3, 7, 1]
        # minHistory = [5, 3, 3, 1]
        #
        # After:
        # stack      = [5, 3, 7]
        # minHistory = [5, 3, 3]
        #
        # Current minimum is now 3.
        #
        # Time: O(1)


    def top(self) -> int:

        # [-1] accesses the last element of a Python list.
        # It does NOT remove the element.
        #
        # Example:
        # stack = [5, 3, 7]
        #
        # top() -> 7
        # stack remains [5, 3, 7]

        return self.stack[-1]

        # Time: O(1)


    def getMin(self) -> int:

        # The last element of minHistory always stores
        # the minimum of the CURRENT stack.
        #
        # Example:
        # stack      = [5, 3, 7]
        # minHistory = [5, 3, 3]
        #
        # getMin() -> 3
        #
        # No searching or looping is needed!

        return self.minHistory[-1]

        # Time: O(1)


# ============================================================
# FULL DRY RUN: LEETCODE EXAMPLE
# ============================================================
#
# obj = MinStack()
#
# Operation        stack       minHistory    Output
# ------------------------------------------------
# MinStack()       []          []            null
# push(1)          [1]         [1]           null
# push(2)          [1,2]       [1,1]         null
# push(0)          [1,2,0]     [1,1,0]       null
# getMin()         [1,2,0]     [1,1,0]       0
# pop()            [1,2]       [1,1]         null
# top()            [1,2]       [1,1]         2
# getMin()         [1,2]       [1,1]         1
#
# Expected output:
# [null, null, null, null, 0, null, 2, 1]
#
# Note:
# LeetCode automatically creates the object and calls
# these methods. We only implement the class.
# We do NOT need to construct the output array ourselves.
#
# ============================================================
# TIME AND SPACE COMPLEXITY
# ============================================================
#
# __init__() -> O(1)
# push()     -> O(1) amortized
# pop()      -> O(1)
# top()      -> O(1)
# getMin()   -> O(1)
#
# SPACE COMPLEXITY: O(n)
#
# stack      -> stores n elements
# minHistory -> stores n elements
#
# Total = O(n) + O(n) = O(2n) = O(n)
#
# ============================================================
# KEY TAKEAWAYS FOR FUTURE LEETCODE PROBLEMS
# ============================================================
#
# 1. If repeatedly calculating something costs O(n),
#    consider storing information as elements are inserted.
#
# 2. An auxiliary data structure can help optimize queries.
#
# 3. Two synchronized stacks can maintain information
#    about the current state.
#
# 4. When pushing, update both the data and its metadata.
#
# 5. When popping, remove both so previous information
#    is automatically restored.
#
# 6. Python list[-1] accesses the last element in O(1).
#    Python list.pop() removes the last element in O(1).
#
# REMEMBER:
# "Store the minimum at every position, so removing an
# element automatically restores the previous minimum."
# ============================================================
