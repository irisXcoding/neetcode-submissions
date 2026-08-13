class Solution:
    def isValid(self, s: str) -> bool:
        _dict = {')':'(', '}':'{', ']':'['}
        _stack = []
        for item in s:
            if item not in _dict:
                _stack.append(item)
            elif not _stack or _stack.pop(-1)!=_dict[item]:
                return False
        return True if not _stack else False

        