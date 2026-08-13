class Solution:
    def isValid(self, s: str) -> bool:
        openers = list("({[")
        closers = list(")}]")
        record = []
        for i in range(len(s)):
            if s[i] in openers:
                record.append(s[i])
            else:
                if record == []:
                    return False
                elif closers.index(s[i]) == openers.index(record[-1]):
                    record.pop()
                else:
                    return False
        valid = False
    
        if record == []:
            valid = True
    
        return valid