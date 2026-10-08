class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        if sensor1 == sensor2:
            return -1

        mismatch = next(
            index
            for index, (first, second) in enumerate(zip(sensor1, sensor2))
            if first != second
        )
        first_is_faulty = (
            sensor1[mismatch:-1] == sensor2[mismatch + 1 :]
            and sensor1[-1] != sensor2[mismatch]
        )
        second_is_faulty = (
            sensor2[mismatch:-1] == sensor1[mismatch + 1 :]
            and sensor2[-1] != sensor1[mismatch]
        )
        if first_is_faulty != second_is_faulty:
            return 1 if first_is_faulty else 2
        return -1
