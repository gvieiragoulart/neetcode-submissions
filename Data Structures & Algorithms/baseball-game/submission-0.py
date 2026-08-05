class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record_stack: List[int] = []

        for op in operations:
            if op not in ["+", "D", "C"]:
                record_stack.append(int(op))
            elif op == "+":
                result = record_stack[-1] + record_stack[-2]
                record_stack.append(int(result))
            elif op == "C":
                record_stack.pop()
            elif op == "D":
                result = record_stack[-1] * 2
                record_stack.append(int(result))
        
        return sum(record_stack)
        