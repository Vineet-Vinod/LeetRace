class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        devices = [row.count("1") for row in bank if "1" in row]
        return sum(first * second for first, second in zip(devices, devices[1:]))
