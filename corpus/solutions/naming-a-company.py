class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups = [set() for _ in range(26)]
        for word in ideas:
            groups[ord(word[0]) - 97].add(word[1:])
        answer = 0
        for i in range(26):
            for j in range(i):
                common = len(groups[i] & groups[j])
                answer += 2 * (len(groups[i]) - common) * (len(groups[j]) - common)
        return answer
