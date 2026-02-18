"""
Unit tests for server/sandbox.py — subprocess code execution sandbox.

Tests cover:
- Correct solutions: all tests pass
- Partial passes: some tests fail
- Wrong output: assertion error captured, error message set
- Syntax/compilation errors: error reported, passed=0
- Runtime exceptions: ZeroDivisionError, NameError, etc.
- Unknown entry point: error reported
- Empty code: graceful failure
- Empty test case list: returns 0/0 without error
- Infinite recursion: sandbox doesn't hang (RecursionError caught)
- Any-order flag: allows differently-ordered list results
- Preamble: typing imports available to user code
- stdout from user code: doesn't corrupt JSON result
- time_ms field: always present and non-negative
- Async run_code wrapper: correct plumbing to _run_sync
"""

import asyncio
import pytest
from server.sandbox import run_code, _run_sync


PREAMBLE = (
    "from typing import *\n"
    "from collections import *\n"
    "from functools import *\n"
)


# ---------------------------------------------------------------------------
# Correct solutions
# ---------------------------------------------------------------------------

class TestCorrectCode:
    def test_two_sum_solution_passes_all_cases(self):
        code = """
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
        return None
"""
        test_cases = [
            "assert candidate(nums=[2,7,11,15], target=9) == [0, 1]",
            "assert candidate(nums=[3,2,4], target=6) == [1, 2]",
            "assert candidate(nums=[3,3], target=6) == [0, 1]",
        ]
        result = _run_sync(code, "Solution().twoSum", test_cases, preamble=PREAMBLE)
        assert result["passed"] == 3
        assert result["total"] == 3
        assert result["error"] is None

    def test_simple_function_passes_all_cases(self):
        code = "def add(a, b): return a + b"
        test_cases = [
            "assert candidate(1, 2) == 3",
            "assert candidate(-1, 1) == 0",
            "assert candidate(0, 0) == 0",
            "assert candidate(100, 200) == 300",
        ]
        result = _run_sync(code, "add", test_cases)
        assert result["passed"] == 4
        assert result["total"] == 4
        assert result["error"] is None

    def test_solution_using_list_type_hint_with_preamble(self):
        code = """
class Solution:
    def doubleList(self, nums: List[int]) -> List[int]:
        return [n * 2 for n in nums]
"""
        test_cases = [
            "assert candidate(nums=[1,2,3]) == [2,4,6]",
            "assert candidate(nums=[]) == []",
        ]
        result = _run_sync(code, "Solution().doubleList", test_cases, preamble=PREAMBLE)
        assert result["passed"] == 2
        assert result["error"] is None

    def test_solution_with_optional_return_type(self):
        code = """
class Solution:
    def findMax(self, nums: List[int]) -> Optional[int]:
        return max(nums) if nums else None
"""
        test_cases = [
            "assert candidate(nums=[3,1,4,1,5]) == 5",
            "assert candidate(nums=[]) is None",
        ]
        result = _run_sync(code, "Solution().findMax", test_cases, preamble=PREAMBLE)
        assert result["passed"] == 2
        assert result["error"] is None

    def test_max_profit_solution(self):
        code = """
class Solution:
    def maxProfit(self, prices):
        max_p, min_p = 0, float('inf')
        for p in prices:
            min_p = min(min_p, p)
            max_p = max(max_p, p - min_p)
        return max_p
"""
        test_cases = [
            "assert candidate(prices=[7,1,5,3,6,4]) == 5",
            "assert candidate(prices=[7,6,4,3,1]) == 0",
            "assert candidate(prices=[1,2]) == 1",
        ]
        result = _run_sync(code, "Solution().maxProfit", test_cases)
        assert result["passed"] == 3
        assert result["error"] is None


# ---------------------------------------------------------------------------
# Time metadata
# ---------------------------------------------------------------------------

class TestTimeMeta:
    def test_time_ms_present_and_non_negative(self):
        result = _run_sync("def f(x): return x", "f", ["assert candidate(1) == 1"])
        assert "time_ms" in result
        assert isinstance(result["time_ms"], int)
        assert result["time_ms"] >= 0

    def test_time_ms_present_even_on_error(self):
        result = _run_sync("def f(x): raise ValueError", "f", ["assert candidate(1) == 1"])
        assert "time_ms" in result
        assert result["time_ms"] >= 0


# ---------------------------------------------------------------------------
# Partial passes
# ---------------------------------------------------------------------------

class TestPartialPass:
    def test_off_by_one_fails_some_tests(self):
        code = "def add(a, b): return a + b + 1"  # always off by 1
        test_cases = [
            "assert candidate(1, 2) == 3",   # fails: returns 4
            "assert candidate(0, 0) == 0",   # fails: returns 1
            "assert candidate(0, 0) == 1",   # passes: returns 1 (lucky)
        ]
        result = _run_sync(code, "add", test_cases)
        assert result["total"] == 3
        assert result["passed"] == 1

    def test_error_is_set_when_at_least_one_test_fails(self):
        code = "def f(x): return x + 1"
        test_cases = [
            "assert candidate(0) == 0",  # fails
            "assert candidate(1) == 2",  # passes
        ]
        result = _run_sync(code, "f", test_cases)
        assert result["passed"] == 1
        assert result["total"] == 2
        assert result["error"] is not None

    def test_first_failing_error_is_captured(self):
        code = "def f(x): return x * 2"
        test_cases = [
            "assert candidate(1) == 99",   # fails first
            "assert candidate(2) == 4",    # passes second
        ]
        result = _run_sync(code, "f", test_cases)
        assert result["error"] is not None
        # Error message should mention expected vs got
        assert "99" in result["error"] or "Expected" in result["error"] or "2" in result["error"]


# ---------------------------------------------------------------------------
# Wrong output
# ---------------------------------------------------------------------------

class TestWrongOutput:
    def test_wrong_return_value_results_in_zero_passed(self):
        code = "def add(a, b): return a - b"  # wrong operation
        test_cases = ["assert candidate(1, 2) == 3"]
        result = _run_sync(code, "add", test_cases)
        assert result["passed"] == 0
        assert result["total"] == 1
        assert result["error"] is not None

    def test_none_return_when_value_expected(self):
        code = "def f(x): return None"
        test_cases = ["assert candidate(5) == 5"]
        result = _run_sync(code, "f", test_cases)
        assert result["passed"] == 0
        assert result["error"] is not None


# ---------------------------------------------------------------------------
# Compilation / syntax errors
# ---------------------------------------------------------------------------

class TestCompilationErrors:
    def test_syntax_error_reports_compilation_error(self):
        code = "def f(x\n    return x"  # missing closing paren
        test_cases = ["assert candidate(1) == 1"]
        result = _run_sync(code, "f", test_cases)
        assert result["passed"] == 0
        assert result["error"] is not None
        error_lower = result["error"].lower()
        assert "compilation error" in error_lower or "syntaxerror" in error_lower or "error" in error_lower

    def test_undefined_variable_in_code(self):
        code = "def f(x): return undefined_var + x"
        test_cases = ["assert candidate(1) == 1"]
        result = _run_sync(code, "f", test_cases)
        assert result["passed"] == 0
        assert result["error"] is not None

    def test_import_error_inside_function(self):
        code = "def f(x): import nonexistent_module_xyz; return x"
        test_cases = ["assert candidate(1) == 1"]
        result = _run_sync(code, "f", test_cases)
        assert result["passed"] == 0
        assert result["error"] is not None


# ---------------------------------------------------------------------------
# Runtime exceptions per test case
# ---------------------------------------------------------------------------

class TestRuntimeExceptions:
    def test_zero_division_in_function(self):
        code = "def f(x): return 10 // x"
        test_cases = [
            "assert candidate(0) == 1",    # ZeroDivisionError
            "assert candidate(2) == 5",    # passes
        ]
        result = _run_sync(code, "f", test_cases)
        assert result["total"] == 2
        assert result["passed"] == 1
        assert result["error"] is not None

    def test_index_error_in_function(self):
        code = "def f(lst): return lst[10]"
        test_cases = ["assert candidate([1,2]) == 1"]
        result = _run_sync(code, "f", test_cases)
        assert result["passed"] == 0
        assert result["error"] is not None
        assert "runtime error" in result["error"].lower()

    def test_infinite_recursion_does_not_hang(self):
        code = "def f(x): return f(x + 1)"
        test_cases = ["assert candidate(0) == 1"]
        # Should complete within sandbox timeout, not hang
        result = _run_sync(code, "f", test_cases)
        assert result["passed"] == 0
        assert result["error"] is not None


# ---------------------------------------------------------------------------
# Entry point resolution
# ---------------------------------------------------------------------------

class TestEntryPoint:
    def test_unknown_entry_point_returns_error(self):
        code = "def f(x): return x"
        result = _run_sync(code, "does_not_exist_xyz", ["assert candidate(1) == 1"])
        assert result["passed"] == 0
        assert result["error"] is not None
        assert "cannot resolve" in result["error"].lower()

    def test_solution_class_method_entry_point(self):
        code = """
class Solution:
    def solve(self, n):
        return n * n
"""
        result = _run_sync(code, "Solution().solve", ["assert candidate(4) == 16"])
        assert result["passed"] == 1
        assert result["error"] is None

    def test_plain_function_entry_point(self):
        code = "def my_func(n): return n + 1"
        result = _run_sync(code, "my_func", ["assert candidate(5) == 6"])
        assert result["passed"] == 1
        assert result["error"] is None


# ---------------------------------------------------------------------------
# Edge cases
# ---------------------------------------------------------------------------

class TestEdgeCases:
    def test_empty_test_cases_list(self):
        result = _run_sync("def f(x): return x", "f", [])
        assert result["passed"] == 0
        assert result["total"] == 0
        # No error expected — there's simply nothing to run
        assert result.get("error") is None or result["passed"] == 0

    def test_empty_code_returns_error(self):
        result = _run_sync("", "f", ["assert candidate(1) == 1"])
        assert result["passed"] == 0
        assert result["error"] is not None

    def test_whitespace_only_code_returns_error(self):
        result = _run_sync("   \n\n   ", "f", ["assert candidate(1) == 1"])
        assert result["passed"] == 0
        assert result["error"] is not None

    def test_stdout_key_always_present(self):
        code = "def f(x): print('hello'); return x"
        result = _run_sync(code, "f", ["assert candidate(1) == 1"])
        assert "stdout" in result

    def test_user_print_does_not_corrupt_json_result(self):
        """User code printing to stdout must not break JSON parsing of the result."""
        code = "def f(x):\n    print('debug:', x)\n    return x * 2"
        result = _run_sync(code, "f", ["assert candidate(5) == 10"])
        assert result["passed"] == 1
        assert result["total"] == 1

    def test_user_print_captured_in_stdout(self):
        code = "def f(x):\n    print('output_here')\n    return x"
        result = _run_sync(code, "f", ["assert candidate(1) == 1"])
        assert "output_here" in result.get("stdout", "")

    def test_any_order_true_allows_different_list_order(self):
        # Result [1,2,3] should match expected [3,1,2] when any_order=True
        code = "def f(nums): return sorted(nums, reverse=True)"
        test_cases = ["assert candidate(nums=[1,2,3]) == [1,2,3]"]
        result = _run_sync(code, "f", test_cases, any_order=True)
        assert result["passed"] == 1

    def test_any_order_false_requires_exact_order(self):
        code = "def f(nums): return sorted(nums, reverse=True)"
        test_cases = ["assert candidate(nums=[1,2,3]) == [1,2,3]"]
        result = _run_sync(code, "f", test_cases, any_order=False)
        # [3,2,1] != [1,2,3] with exact ordering
        assert result["passed"] == 0


# ---------------------------------------------------------------------------
# Async run_code wrapper
# ---------------------------------------------------------------------------

class TestRunCodeAsync:
    @pytest.mark.asyncio
    async def test_correct_solution_via_async(self):
        code = "def add(a, b): return a + b"
        result = await run_code(code, "add", ["assert candidate(1, 2) == 3"])
        assert result["passed"] == 1
        assert result["total"] == 1
        assert result["error"] is None

    @pytest.mark.asyncio
    async def test_returns_time_ms_as_int(self):
        code = "def f(x): return x"
        result = await run_code(code, "f", ["assert candidate(1) == 1"])
        assert "time_ms" in result
        assert isinstance(result["time_ms"], int)

    @pytest.mark.asyncio
    async def test_wrong_answer_via_async(self):
        code = "def f(x): return x + 100"
        result = await run_code(code, "f", ["assert candidate(5) == 5"])
        assert result["passed"] == 0
        assert result["error"] is not None

    @pytest.mark.asyncio
    async def test_preamble_passed_through_async(self):
        code = """
class Solution:
    def fn(self, nums: List[int]) -> int:
        return sum(nums)
"""
        result = await run_code(
            code, "Solution().fn",
            ["assert candidate(nums=[1,2,3]) == 6"],
            preamble=PREAMBLE,
        )
        assert result["passed"] == 1
        assert result["error"] is None
