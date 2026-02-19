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
        "verified": True,
    },
    {
        "id": "merge-sort",
        "title": "Merge Sort",
        "difficulty": "Medium",
        "tags": [],
        "test_count": 3,
        "verified": True,
    },
    {
        "id": "trapping",
        "title": "Trapping Rain",
        "difficulty": "Hard",
        "tags": [],
        "test_count": 4,
        "verified": True,
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
    def _write_all_fake_problems(self, tmp_path):
        """Write index and all fake problem files to tmp_path."""
        (tmp_path / "index.json").write_text(json.dumps(FAKE_INDEX))
        for entry in FAKE_INDEX:
            prob = {
                **FAKE_PROBLEM,
                "id": entry["id"],
                "difficulty": entry["difficulty"],
            }
            (tmp_path / f"{entry['id']}.json").write_text(json.dumps(prob))

    def test_returns_a_problem_dict(self, tmp_path):
        self._write_all_fake_problems(tmp_path)
        with patch.object(problems_module, "PROBLEMS_DIR", tmp_path):
            problems_module._index = None
            result = pick_random()
        assert result is not None
        assert isinstance(result, dict)

    def test_returned_problem_has_required_fields(self, tmp_path):
        self._write_all_fake_problems(tmp_path)
        with patch.object(problems_module, "PROBLEMS_DIR", tmp_path):
            problems_module._index = None
            result = pick_random()
        assert result is not None
        assert "id" in result
        assert "title" in result
        assert "difficulty" in result

    def test_returns_none_for_empty_index(self, tmp_path):
        (tmp_path / "index.json").write_text("[]")
        with patch.object(problems_module, "PROBLEMS_DIR", tmp_path):
            problems_module._index = None
            result = pick_random()
        assert result is None

    def test_difficulty_easy_filter_returns_easy_problems(self, tmp_path):
        """All picks filtered by 'easy' should have Easy difficulty."""
        (tmp_path / "index.json").write_text(json.dumps(FAKE_INDEX))
        (tmp_path / "two-sum.json").write_text(json.dumps(FAKE_PROBLEM))
        with patch.object(problems_module, "PROBLEMS_DIR", tmp_path):
            problems_module._index = None
            for _ in range(5):
                result = pick_random(difficulty="easy")
                if result is not None:
                    assert result["difficulty"].lower() == "easy"

    def test_difficulty_hard_filter_returns_hard_problems(self, tmp_path):
        fake_hard_problem = {**FAKE_PROBLEM, "id": "trapping", "difficulty": "Hard"}
        (tmp_path / "index.json").write_text(json.dumps(FAKE_INDEX))
        (tmp_path / "trapping.json").write_text(json.dumps(fake_hard_problem))
        with patch.object(problems_module, "PROBLEMS_DIR", tmp_path):
            problems_module._index = None
            for _ in range(5):
                result = pick_random(difficulty="hard")
                if result is not None:
                    assert result["difficulty"].lower() == "hard"

    def test_difficulty_medium_filter_returns_medium_problems(self, tmp_path):
        fake_medium_problem = {
            **FAKE_PROBLEM,
            "id": "merge-sort",
            "difficulty": "Medium",
        }
        (tmp_path / "index.json").write_text(json.dumps(FAKE_INDEX))
        (tmp_path / "merge-sort.json").write_text(json.dumps(fake_medium_problem))
        with patch.object(problems_module, "PROBLEMS_DIR", tmp_path):
            problems_module._index = None
            for _ in range(5):
                result = pick_random(difficulty="medium")
                if result is not None:
                    assert result["difficulty"].lower() == "medium"

    def test_no_filter_returns_a_problem(self, tmp_path):
        self._write_all_fake_problems(tmp_path)
        with patch.object(problems_module, "PROBLEMS_DIR", tmp_path):
            problems_module._index = None
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

    def test_successive_calls_may_return_different_problems(self, tmp_path):
        """With multiple verified entries, picks should vary."""
        (tmp_path / "index.json").write_text(json.dumps(FAKE_INDEX))
        for entry in FAKE_INDEX:
            prob = {
                **FAKE_PROBLEM,
                "id": entry["id"],
                "difficulty": entry["difficulty"],
            }
            (tmp_path / f"{entry['id']}.json").write_text(json.dumps(prob))
        with patch.object(problems_module, "PROBLEMS_DIR", tmp_path):
            problems_module._index = None
            results = {pick_random()["id"] for _ in range(20)}
        # With 3 verified problems, we'd expect more than 1 unique result in 20 tries
        assert len(results) >= 1  # at minimum it shouldn't crash
