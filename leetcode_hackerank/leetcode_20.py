class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        dictt = {"(": ")", "[": "]", "{": "}"}
        for el in s:
            if el in "([{":
                lst.append(el)
            else:
                if len(lst) == 0:
                    return False
                if el == dictt[lst[-1]]:
                    lst.pop()
                else:
                    return False
        if len(lst) != 0:
            return False
        return True