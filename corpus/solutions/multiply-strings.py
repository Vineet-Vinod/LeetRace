class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        result = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                product = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                total = product + result[i + j + 1]
                result[i + j + 1] = total % 10
                result[i + j] += total // 10
        return "".join(map(str, result)).lstrip("0")
