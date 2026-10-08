class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []
        for height, count in sorted(people, key=lambda person: (-person[0], person[1])):
            queue.insert(count, [height, count])
        return queue
