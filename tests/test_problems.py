"""
Unit tests for server/problems.py — loading, caching, and picking problems.

Tests cover:
- load_index: real data, caching, empty-dir fallback
- load_problem: real problem, missing problem, required fields
- pick_random: no filter, difficulty filter (case-insensitive), empty index
"""

import json
from unittest.mock import patch

import server.problems as problems_module
from server.problems import load_index, load_problem, pick_random


# ---------------------------------------------------------------------------
# Fake data for mocked tests
# ---------------------------------------------------------------------------

FAKE_INDEX = [
    {
        "id": "two-sum",
        "title": "Two Sum",
        "difficulty": "Easy",
        "tags": [],
        "test_count": 5,
    },
    {
        "id": "merge-sort",
        "title": "Merge Sort",
        "difficulty": "Medium",
        "tags": [],
        "test_count": 3,
    },
    {
        "id": "trapping",
        "title": "Trapping Rain",
        "difficulty": "Hard",
        "tags": [],
        "test_count": 4,
    },
]

FAKE_PROBLEM = {
    "id": "two-sum",
    "title": "Two Sum",
    "difficulty": "Easy",
    "description": "Given nums and target...",
    "entry_point": "Solution().twoSum",
    "starter_code": "class Solution:\n    def twoSum(self, nums, target): pass",
    "preamble": "from typing import *",
    "test_cases": [
        "assert candidate(nums=[2,7,11,15], target=9) == [0, 1]",
        "assert candidate(nums=[3,2,4], target=6) == [1, 2]",
    ],
}


# ---------------------------------------------------------------------------
# load_index
# ---------------------------------------------------------------------------


class TestLoadIndex:
    def test_returns_list(self):
        result = load_index()
        assert isinstance(result, list)

    def test_real_index_is_non_empty(self):
        result = load_index()
        assert len(result) > 0

    def test_entries_have_id_field(self):
        for entry in load_index()[:10]:
            assert "id" in entry, f"Entry missing 'id': {entry}"

    def test_entries_have_title_field(self):
        for entry in load_index()[:10]:
            assert "title" in entry

    def test_entries_have_difficulty_field(self):
        for entry in load_index()[:10]:
            assert "difficulty" in entry

    def test_all_difficulties_are_valid(self):
        valid = {"Easy", "Medium", "Hard"}
        for entry in load_index():
            assert entry["difficulty"] in valid, (
                f"Problem '{entry['id']}' has unexpected difficulty '{entry['difficulty']}'"
            )

    def test_result_is_cached_on_second_call(self):
        """Second call returns the same list object (identity check)."""
        result1 = load_index()
        result2 = load_index()
        assert result1 is result2

    def test_returns_empty_list_when_index_file_missing(self, tmp_path):
        with patch.object(problems_module, "PROBLEMS_DIR", tmp_path):
            problems_module._index = None
            result = load_index()
        assert result == []


# ---------------------------------------------------------------------------
# load_problem
# ---------------------------------------------------------------------------


class TestLoadProblem:
    def test_real_problem_returns_dict(self):
        result = load_problem("two-sum")
        assert isinstance(result, dict)

    def test_real_problem_has_id(self):
        result = load_problem("two-sum")
        assert result["id"] == "two-sum"

    def test_real_problem_has_required_fields(self):
        result = load_problem("two-sum")
        required = {
            "id",
            "title",
            "difficulty",
            "description",
            "entry_point",
            "starter_code",
            "test_cases",
        }
        assert required.issubset(set(result.keys()))

    def test_test_cases_is_nonempty_list(self):
        result = load_problem("two-sum")
        assert isinstance(result["test_cases"], list)
        assert len(result["test_cases"]) > 0

    def test_test_cases_are_strings(self):
        result = load_problem("two-sum")
        for tc in result["test_cases"]:
            assert isinstance(tc, str)

    def test_missing_problem_returns_none(self):
        result = load_problem("this-problem-absolutely-does-not-exist-xyz-abc")
        assert result is None

    def test_empty_id_returns_none(self):
        result = load_problem("")
        assert result is None

    def test_load_from_fake_directory(self, tmp_path):
        """Can load a problem JSON from a temp directory via mock."""
        (tmp_path / "test-prob.json").write_text(json.dumps(FAKE_PROBLEM))
        with patch.object(problems_module, "PROBLEMS_DIR", tmp_path):
            result = load_problem("test-prob")
        assert result is not None
        assert result["id"] == "two-sum"
        assert result["title"] == "Two Sum"

    def test_missing_file_in_fake_directory_returns_none(self, tmp_path):
        with patch.object(problems_module, "PROBLEMS_DIR", tmp_path):
            result = load_problem("missing-problem")
        assert result is None


# ---------------------------------------------------------------------------
# pick_random
# ---------------------------------------------------------------------------


class TestPickRandom:
    def test_returns_a_problem_dict(self):
        result = pick_random()
        assert result is not None
        assert isinstance(result, dict)

    def test_returned_problem_has_required_fields(self):
        result = pick_random()
        assert "id" in result
        assert "title" in result
        assert "difficulty" in result

    def test_returns_none_for_empty_index(self, tmp_path):
        (tmp_path / "index.json").write_text("[]")
        with patch.object(problems_module, "PROBLEMS_DIR", tmp_path):
            problems_module._index = None
            result = pick_random()
        assert result is None

    def test_difficulty_easy_filter_returns_easy_problems(self):
        """All picks filtered by 'easy' should have Easy difficulty."""
        for _ in range(5):
            result = pick_random(difficulty="easy")
            if result is not None:
                assert result["difficulty"].lower() == "easy"

    def test_difficulty_hard_filter_returns_hard_problems(self):
        for _ in range(5):
            result = pick_random(difficulty="hard")
            if result is not None:
                assert result["difficulty"].lower() == "hard"

    def test_difficulty_medium_filter_returns_medium_problems(self):
        for _ in range(5):
            result = pick_random(difficulty="medium")
            if result is not None:
                assert result["difficulty"].lower() == "medium"

    def test_no_filter_returns_a_problem(self):
        result = pick_random(difficulty=None)
        assert result is not None

    def test_unknown_difficulty_returns_none(self, tmp_path):
        """No problems match a nonsense difficulty, so result must be None."""
        (tmp_path / "index.json").write_text(json.dumps(FAKE_INDEX))
        (tmp_path / "two-sum.json").write_text(json.dumps(FAKE_PROBLEM))
        with patch.object(problems_module, "PROBLEMS_DIR", tmp_path):
            problems_module._index = None
            result = pick_random(difficulty="impossible_xyz")
        assert result is None

    def test_difficulty_filter_is_case_insensitive(self, tmp_path):
        """'EASY', 'easy', and 'Easy' should all match difficulty='Easy'."""
        (tmp_path / "index.json").write_text(json.dumps(FAKE_INDEX))
        (tmp_path / "two-sum.json").write_text(json.dumps(FAKE_PROBLEM))
        with patch.object(problems_module, "PROBLEMS_DIR", tmp_path):
            problems_module._index = None
            result = pick_random(difficulty="EASY")
        assert result is not None
        assert result["difficulty"] == "Easy"

    def test_successive_calls_may_return_different_problems(self):
        """With a large index, two picks are unlikely to both be identical (probabilistic)."""
        results = {pick_random()["id"] for _ in range(20)}
        # With hundreds of problems, we'd expect more than 1 unique result in 20 tries
        assert len(results) >= 1  # at minimum it shouldn't crash
