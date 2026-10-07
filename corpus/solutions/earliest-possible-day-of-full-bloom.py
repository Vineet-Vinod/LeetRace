class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        planted = 0
        answer = 0
        for grow, plant in sorted(zip(growTime, plantTime), reverse=True):
            planted += plant
            answer = max(answer, planted + grow)
        return answer
