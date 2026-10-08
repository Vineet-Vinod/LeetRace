from dataclasses import dataclass


@dataclass(frozen=True)
class BuildResult:
    problem_id: str
    test_count: int
    time_ms: int
