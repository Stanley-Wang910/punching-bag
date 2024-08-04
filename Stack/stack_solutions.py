class Stack:
    # 20. Valid Parentheses / Easy / 15:30 minutes / (https://leetcode.com/problems/valid-parentheses/)
    def isValid(self, s: str) -> bool:
        stack = []
        valid_map = {")" :"(","]" :"[","}" :"{"}

        for c in s:
            if c in valid_map:
                if not stack or valid_map[c] != stack.pop():
                    return False
                      
            else:
                stack.append(c)
        return len(stack) == 0

    # 155. Min Stack / Medium / 12 minutes / (https://leetcode.com/problems/min-stack/)
    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

    # 150. Evaluate Reverse Polish Notation / Medium / 51 minutess / (https://leetcode.com/problems/evaluate-reverse-polish-notation/)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a)) # round towards zero
            else:
                stack.append(int(c))
        return stack[0]

    # 22. Generate Parentheses / Medium / 30 minutes / (https://leetcode.com/problems/generate-parentheses/)
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return 

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res

    # 739. Daily Temperatures / Medium / 23 minute / (https://leetcode.com/problems/daily-temperatures/)
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = [] # pair = [temp, index]
        for i, temp in enumerate(temps):
            while stack and temp > stack[-1][0]: # Top of stack
                stackT, stackI = stack.pop()
                res[stackI] = (i - stackI)
            stack.append([temp, i])
        return res
    
    # 853. Car Fleet / Medium / 50 minutes / (https://leetcode.com/problems/car-fleet/)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(key=lambda pair: pair[0])
        stack = []
        for pair in reversed(pairs):
            stack.append((target - pair[0]) / pair[1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        
    