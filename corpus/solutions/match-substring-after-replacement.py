class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        # Bit i represents a partial match ending at sub[i].
        masks = {}
        for i, char in enumerate(sub):
            masks[char] = masks.get(char, 0) | (1 << i)
        allowed = dict(masks)
        for old, new in mappings:
            allowed[new] = allowed.get(new, 0) | masks.get(old, 0)
        state = 0
        last = 1 << (len(sub) - 1)
        for char in s:
            state = ((state << 1) | 1) & allowed.get(char, 0)
            if state & last:
                return True
        return False
