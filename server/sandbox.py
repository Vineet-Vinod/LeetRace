"""Execute user code in a sandboxed subprocess with resource limits."""

import asyncio
import json
import subprocess
import sys
import textwrap
import time


RUNNER_SCRIPT = textwrap.dedent("""\
    import json, sys, time, re

    def strip_kwargs(tc):
        return re.sub(r'(?<=[\\(,])\\s*\\w+\\s*=\\s*(?!=)', ' ', tc)

    data = json.loads(sys.stdin.read())
    code = data["code"]
    entry_point = data["entry_point"]
    test_cases = [strip_kwargs(tc) for tc in data["test_cases"]]
    preamble = data.get("preamble", "")

    # Execute preamble (imports needed by starter code like List, Optional, etc.)
    namespace = {}
    if preamble:
        try:
            exec(preamble, namespace)
        except Exception:
            pass

    # Execute user code
    try:
        exec(code, namespace)
    except Exception as e:
        print(json.dumps({"passed": 0, "total": len(test_cases), "error": f"Compilation error: {e}"}))
        sys.exit(0)

    # Resolve entry_point — supports both bare names and expressions like Solution().twoSum
    try:
        candidate = eval(entry_point, namespace)
    except Exception as e:
        print(json.dumps({"passed": 0, "total": len(test_cases), "error": f"Cannot resolve '{entry_point}': {e}"}))
        sys.exit(0)

    # Inject as 'candidate' into test namespace (test cases call candidate(...))
    test_ns = dict(namespace)
    test_ns["candidate"] = candidate

    passed = 0
    total = len(test_cases)
    first_error = None

    for tc in test_cases:
        try:
            exec(tc, test_ns)
            passed += 1
        except AssertionError as e:
            if first_error is None:
                first_error = f"Assertion failed: {tc[:100]}"
        except Exception as e:
            if first_error is None:
                first_error = f"Runtime error: {type(e).__name__}: {e}"

    result = {"passed": passed, "total": total, "error": first_error}
    print(json.dumps(result))
""")


def _set_limits():
    """Set resource limits for the child process (Linux only)."""
    try:
        import resource
        resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
        resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, 256 * 1024 * 1024))
        resource.setrlimit(resource.RLIMIT_FSIZE, (1024 * 1024, 1024 * 1024))
        resource.setrlimit(resource.RLIMIT_NPROC, (0, 0))
    except (ImportError, ValueError, OSError):
        pass


def _run_sync(code: str, entry_point: str, test_cases: list[str], preamble: str = "") -> dict:
    """Synchronous sandbox execution."""
    payload = json.dumps({
        "code": code,
        "entry_point": entry_point,
        "test_cases": test_cases,
        "preamble": preamble,
    })

    start = time.monotonic()
    try:
        proc = subprocess.run(
            [sys.executable, "-c", RUNNER_SCRIPT],
            input=payload,
            capture_output=True,
            text=True,
            timeout=10,
            preexec_fn=_set_limits,
        )
        elapsed_ms = int((time.monotonic() - start) * 1000)

        if proc.returncode != 0 and not proc.stdout.strip():
            stderr = proc.stderr.strip()[:200]
            return {"passed": 0, "total": len(test_cases), "error": stderr or "Process crashed", "time_ms": elapsed_ms}

        result = json.loads(proc.stdout.strip())
        result["time_ms"] = elapsed_ms
        return result

    except subprocess.TimeoutExpired:
        elapsed_ms = int((time.monotonic() - start) * 1000)
        return {"passed": 0, "total": len(test_cases), "error": "Time limit exceeded (10s)", "time_ms": elapsed_ms}
    except (json.JSONDecodeError, Exception) as e:
        elapsed_ms = int((time.monotonic() - start) * 1000)
        return {"passed": 0, "total": len(test_cases), "error": str(e)[:200], "time_ms": elapsed_ms}


async def run_code(code: str, entry_point: str, test_cases: list[str], preamble: str = "") -> dict:
    """Run user code in a sandbox. Returns {passed, total, error, time_ms}."""
    return await asyncio.to_thread(_run_sync, code, entry_point, test_cases, preamble)
