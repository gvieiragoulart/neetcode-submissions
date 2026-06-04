class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def isOpenBracket(bracket: str):
            return bracket == "(" or bracket == "{" or bracket == "["

        def validOpenBracket(open_bracket: str, closed_bracket: str):
            if open_bracket == "(":
                return closed_bracket == ")"
            
            if open_bracket == "[":
                return closed_bracket == "]"

            if open_bracket == "{":
                return closed_bracket == "}"

        for bracket in s:
            if isOpenBracket(bracket):
                stack.append(bracket)
            else:
                if not stack:
                    return False

                if validOpenBracket(stack[-1], bracket):
                    stack.pop()
                else:
                    return False
        
        return stack == []





        