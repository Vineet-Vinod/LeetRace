import pytest

from scripts.corpus import compact_test, float_tolerances, load_calls
from server.sandbox import _run_sync


@pytest.mark.parametrize(
    ("description", "expected"),
    [
        ("Answers within 10^-5 are accepted.", (1e-5, 0.0)),
        ("Answers within 10-5 are accepted.", (1e-5, 0.0)),
        ("Absolute or relative error of 10^-6 is accepted.", (1e-6, 1e-6)),
        ("Input: date = '2052-10-20'", (1e-6, 0.0)),
    ],
)
def test_float_tolerance_matches_contract(description, expected):
    assert float_tolerances(description) == expected


def test_generator_inputs_are_reproducible():
    calls, _ = load_calls("two-sum", 37)
    repeated, _ = load_calls("two-sum", 37)
    assert calls == repeated


def test_compact_inputs_preserve_values_and_argument_strings():
    values = [None, True, -7, 0.25, "candidate(nums=literal)"] * 1000
    test = compact_test(f"assert candidate(values={values!r}) == {values!r}")
    assert "test_data(" in test
    result = _run_sync("def solution(values):\n    return values", "solution", [test])
    assert result["passed"] == 1
    wrong = _run_sync(
        "def solution(values):\n    return values[:-1]", "solution", [test]
    )
    assert wrong["passed"] == 0


def test_duplicate_inputs_are_rejected(tmp_path, monkeypatch):
    import scripts.corpus as corpus

    path = tmp_path / "corpus" / "generators"
    path.mkdir(parents=True)
    (path / "duplicate.py").write_text(
        "def generate(seed=0):\n    return ['candidate(1)', 'candidate( 1 )']\n"
    )
    monkeypatch.setattr(corpus, "ROOT", tmp_path)
    with pytest.raises(ValueError, match="duplicate"):
        load_calls("duplicate", 0)


def test_build_preserves_concurrent_statement_edit(tmp_path, monkeypatch):
    import json

    import scripts.corpus as corpus
    from scripts.corpus_dataclasses import BuildResult

    path = tmp_path / "problems" / "edited.json"
    path.parent.mkdir()
    problem = {
        "id": "edited",
        "title": "Edited",
        "difficulty": "Easy",
        "description": "Original statement",
        "starter_code": "def solution(value): pass",
        "entry_point": "solution",
    }
    path.write_text(json.dumps(problem))
    solutions = tmp_path / "corpus" / "solutions"
    solutions.mkdir(parents=True)
    (solutions / "edited.py").write_text("def solution(value): return value")

    def edit_during_verification(problem_id, problem, code):
        updated = json.loads(path.read_text())
        updated["description"] = "Corrected statement"
        path.write_text(json.dumps(updated))
        return BuildResult(problem_id, 1, 0)

    monkeypatch.setattr(corpus, "ROOT", tmp_path)
    monkeypatch.setattr(corpus, "load_calls", lambda *_: (["candidate(1)"], 1))
    monkeypatch.setattr(corpus, "verify", edit_during_verification)
    with pytest.raises(ValueError, match="changed during rebuild"):
        corpus.build("edited")
    assert json.loads(path.read_text())["description"] == "Corrected statement"
