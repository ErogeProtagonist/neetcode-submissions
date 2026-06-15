class Solution:
    def isValid(self, s: str) -> bool:
        openers = list("({[")
        closers = list(")}]")
        string = list(s)
        valid = False
        order_1 = []
        for i in string:
            if i in openers:
                order_1.append(i)
            if i in closers:
                if len(order_1) == 0:
                    return False
                if closers.index(i) == openers.index(order_1[-1]):
                    order_1.pop()
                else:
                    return False
    
        if order_1 == []:
            valid = True
        return valid