class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        while i < len(code):
            if i and not stack:
                return False
            if code.startswith("<![CDATA[", i):
                if not stack:
                    return False
                end = code.find("]]>", i + 9)
                if end == -1:
                    return False
                i = end + 3
            elif code[i] == "<":
                end = code.find(">", i + 1)
                if end == -1:
                    return False
                closing = code.startswith("</", i)
                name = code[i + 2 if closing else i + 1 : end]
                if not 1 <= len(name) <= 9 or any(not "A" <= c <= "Z" for c in name):
                    return False
                if closing:
                    if not stack or stack.pop() != name:
                        return False
                else:
                    stack.append(name)
                i = end + 1
            else:
                if not stack:
                    return False
                i += 1
        return not stack
