class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        people = [index for index, role in enumerate(team) if role == 0]
        it_people = [index for index, role in enumerate(team) if role == 1]
        person = caught = 0
        for it in it_people:
            while person < len(people) and people[person] < it - dist:
                person += 1
            if person < len(people) and people[person] <= it + dist:
                caught += 1
                person += 1
        return caught
