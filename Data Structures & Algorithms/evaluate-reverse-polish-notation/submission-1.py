class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        _stack = []
        operators = {'+','-','*','/'}
        for token in tokens:
            if token not in operators:
                _stack.append(int(token))
            else:
                first_token = _stack.pop(-1)
                second_token = _stack.pop(-1)
                if token == "+":
                    res = first_token+second_token
                elif token == '*':    
                    res = first_token*second_token
                elif token == '-':
                    res = second_token-first_token
                else:
                    res = int(second_token/first_token)
                _stack.append(res)
        return _stack[0]
