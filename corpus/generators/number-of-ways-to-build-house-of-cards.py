# Inputs are constructed within the stated limits and preserve problem-specific invariants.
def generate(seed: int = 0) -> list[str]:
    # The complete legal input domain is exactly the 500 integers from 1 through 500.
    calls = [f"candidate(n={n})" for n in range(1, 501)]
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
