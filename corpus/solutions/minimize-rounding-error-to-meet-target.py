class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        floors = 0
        fractions: list[int] = []
        base_error = 0
        for price in prices:
            whole, fractional = price.split(".")
            floor_value = int(whole)
            fraction = int(fractional)
            floors += floor_value
            if fraction:
                fractions.append(fraction)
                base_error += fraction
        ceils_needed = target - floors
        if ceils_needed < 0 or ceils_needed > len(fractions):
            return "-1"
        fractions.sort(reverse=True)
        error = base_error
        for fraction in fractions[:ceils_needed]:
            error += 1000 - 2 * fraction
        return f"{error // 1000}.{error % 1000:03d}"
