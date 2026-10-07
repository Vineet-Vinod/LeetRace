class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0.0
        lower = 0
        for upper, percent in brackets:
            taxable = min(income, upper) - lower
            if taxable > 0:
                tax += taxable * percent / 100
            if income <= upper:
                break
            lower = upper
        return tax
