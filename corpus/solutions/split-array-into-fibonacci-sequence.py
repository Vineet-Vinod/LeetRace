class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        sequence = []

        def search(index: int) -> bool:
            if index == len(num):
                return len(sequence) >= 3
            value = 0
            for end in range(index, min(len(num), index + 10)):
                if end > index and num[index] == "0":
                    break
                value = value * 10 + int(num[end])
                if value >= 2**31:
                    break
                if len(sequence) >= 2:
                    expected = sequence[-1] + sequence[-2]
                    if value < expected:
                        continue
                    if value > expected:
                        break
                sequence.append(value)
                if search(end + 1):
                    return True
                sequence.pop()
            return False

        return sequence if search(0) else []
