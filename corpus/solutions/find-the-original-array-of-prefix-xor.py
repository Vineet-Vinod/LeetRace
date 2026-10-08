class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        result = [pref[0]]
        for index in range(1, len(pref)):
            result.append(pref[index - 1] ^ pref[index])
        return result
