class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        events = defaultdict(lambda: [0, 0])
        for left, right, height in buildings:
            events[left][0] += height
            events[left][1] += 1
            events[right][0] -= height
            events[right][1] -= 1
        points = sorted(events)
        total_height = active = 0
        result: List[List[int]] = []
        for i, left in enumerate(points[:-1]):
            total_height += events[left][0]
            active += events[left][1]
            right = points[i + 1]
            if active == 0:
                continue
            average = total_height // active
            if result and result[-1][1] == left and result[-1][2] == average:
                result[-1][1] = right
            else:
                result.append([left, right, average])
        return result
