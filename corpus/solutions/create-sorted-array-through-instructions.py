class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        ranks = {x: i + 1 for i, x in enumerate(sorted(set(instructions)))}
        bit = [0] * (len(ranks) + 1)

        def count(i):
            result = 0
            while i:
                result += bit[i]
                i -= i & -i
            return result

        answer = 0
        for seen, x in enumerate(instructions):
            rank = ranks[x]
            answer += min(count(rank - 1), seen - count(rank))
            while rank < len(bit):
                bit[rank] += 1
                rank += rank & -rank
        return answer % 1000000007
