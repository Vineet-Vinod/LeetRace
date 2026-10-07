class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        counts = defaultdict(int)
        heap = []
        answer = []
        for identifier, change in zip(nums, freq):
            counts[identifier] += change
            heappush(heap, (-counts[identifier], identifier))
            while heap and -heap[0][0] != counts[heap[0][1]]:
                heappop(heap)
            answer.append(-heap[0][0] if heap else 0)
        return answer
