class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def isSimbol(token:str):
            return token == "+" or token == "-" or token == "/" or token == "*"
        
        def doMath(firstNumber:int, operation:str, secondNumber:int):
            if operation == "+":
                return firstNumber + secondNumber
            if operation == "-":
                return firstNumber - secondNumber
            if operation == "/":
                return int(firstNumber / secondNumber)
            if operation == "*":
                return firstNumber * secondNumber

        number_stack = []
        result:int = 0
        for token in tokens:
            if isSimbol(token):
                result = doMath(int(number_stack[-2]), token, int(number_stack[-1]))
                number_stack.pop()
                number_stack.pop()
                number_stack.append(result)
            else:
                number_stack.append(token) 

        return int(number_stack[-1])