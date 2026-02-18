# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LeetRace is a multiplayer LeetCode racing webapp built with FastAPI and vanilla JavaScript. Players create rooms, join games, and race to solve the same problem — the shortest solution (fewest characters) wins, or if unsolved, the player with the most test cases passed ranks higher.

## Development Commands

### Configuration
Create a `.env` file in the root directory (copy from `.env.example`) to customize ports:
```bash
cp .env.example .env
# Edit .env to change FRONTEND_PORT and BACKEND_PORT if desired
```

### Quick Start with Makefile
```bash
make help              # Display all available targets
make format            # Format code with ruff
make lint              # Lint code with ruff (auto-fix)
make test              # Run all tests
make dev               # Start both backend and frontend
make dev-backend       # Start only the FastAPI server
make dev-frontend      # Start only the Vite frontend dev server
```

`make dev` intelligently chooses:
- **With tmux installed**: Runs `./tmux-dev.sh` which opens side-by-side panes and properly cleans up on exit
- **Without tmux**: Runs `./dev.sh` which starts both in the same terminal

### Manual Setup
```bash
uv sync                                    # Install Python dependencies
cd frontend && pnpm install                # Install frontend dependencies
python main.py                             # Start backend on http://localhost:8000
cd frontend && FRONTEND_PORT=3000 pnpm dev # Start frontend on http://localhost:3000
```

### Alternative: Run Script Directly
```bash
./dev.sh  # Starts both servers with environment variables from .env
```

### Testing
```bash
pytest                                    # Run all tests
pytest tests/test_name.py                 # Run tests in a single file
pytest tests/test_name.py::test_function  # Run a specific test function
pytest -v                                 # Verbose output with test names
pytest -k "substring"                     # Run tests matching a substring
```

### Code Quality
```bash
ruff format .                # Format Python code
ruff check . --fix           # Lint and auto-fix issues
```

### Problem Set
```bash
uv pip install datasets                   # Install optional build dependency
python scripts/build_problems.py          # Rebuild problems from HuggingFace dataset
```

The project ships with 2,637 problems (637 Easy, 1,395 Medium, 605 Hard) pre-downloaded from [newfacade/LeetCodeDataset](https://huggingface.co/datasets/newfacade/LeetCodeDataset).

## Architecture

### High-Level Design

**Backend (FastAPI)**
- **Entry Point**: `main.py` starts uvicorn on `0.0.0.0:8000`
- **REST API** (`server/app.py`): Create rooms, get room state, list problems
- **WebSocket Handler** (`server/ws.py`): Game logic (join, start, submit, timer, rankings)
- **State Management** (`server/rooms.py`): In-memory Room and Player objects
- **Code Execution** (`server/sandbox.py`): Run user submissions in isolated subprocesses with CPU/memory/time limits
- **Ranking** (`server/scoring.py`): Score players by solved > tests_passed > char_count > submission_time
- **Problem Loading** (`server/problems.py`): Load and index problems from JSON files

**Frontend (Vanilla JS + Monaco Editor)**
- `static/index.html` + `static/js/app.js`: Landing page (create/join room)
- `static/room.html` + `static/js/room.js`: Game room with game state and WebSocket client
- `static/js/editor.js`: Monaco Editor integration
- `static/css/style.css`: Dark theme styling

### Room Lifecycle

1. **Lobby** — Players join a room and wait for the host to start
2. **Playing** — Timer counts down, players submit solutions
3. **Finished** — Results shown; if multi-round, a 30-second break before next round

### Player Submission Flow

1. Player submits code via WebSocket
2. `ws.py` receives submission, calls `sandbox.run_code()` with the user's code
3. Sandbox runs code in subprocess with resource limits (5s CPU, 256MB RAM, 10s wall-clock)
4. Test results returned (passed count, char count, errors)
5. Player's best submission tracked; `scoring.rank_players()` updates rankings
6. Scoreboard broadcasted to all players

### Key Data Models

**Room** (`server/rooms.py`)
- `id`: 6-character hex code (e.g., 'A1B2C3')
- `state`: RoomState.LOBBY / PLAYING / FINISHED
- `players`: dict of name → Player
- `problem`: Current problem dict (None in lobby)
- `start_time`, `time_limit`: Unix timestamp and duration in seconds
- `current_round`, `total_rounds`: Multi-round support

**Player** (`server/rooms.py`)
- `name`: Display name, unique per room
- `websocket`: Active connection or None if disconnected
- `best_submission`: Highest-scoring submission (for rankings)
- `locked_at`: Timestamp when player locked in (for tiebreaking)

**Submission Result** (from `sandbox.run_code()`)
- `solved`: bool
- `passed`, `total`: Test cases
- `char_count`: Solution length (only if solved)
- `submit_time`: Timestamp
- `error`: Error message if execution failed
- `output`: Raw execution output (for debugging)

### Sandbox Security Model

User code runs in a subprocess via `subprocess.run()` with POSIX resource limits:
- **CPU time**: 5 seconds
- **Memory**: 256 MB
- **Wall-clock timeout**: 10 seconds
- **File writes**: 1 MB
- **Subprocesses**: None allowed (forking disabled)

**Important**: The sandbox does NOT provide filesystem isolation — code has full read access. For production, consider running inside containers or seccomp-bpf.

### WebSocket Message Types

**Client → Server**
- `join`: Player joins a room
- `start`: Host starts the game
- `submit`: Player submits code
- `lock`: Player locks in (ready for next round)

**Server → Client**
- `room_state`: Updated room/player list
- `problem`: Problem details when round starts
- `submission_result`: Feedback on code submission
- `scoreboard`: Updated rankings
- `tick`: Timer updates (every 5s)
- `round_ended`: Round results; if multi-round, shows break countdown
- `game_finished`: Final results
- `error`: Error message

## Testing

Tests use `pytest-asyncio` for async test support. Key test files:

- `test_ws_handler.py`: WebSocket message handling and game flow
- `test_sandbox.py`: Code execution and sandboxing
- `test_scoring.py`: Ranking logic
- `test_rooms.py`: Room creation and state management
- `test_api.py`: REST endpoints
- `test_problems.py`: Problem loading

Global fixtures in `conftest.py`:
- `clear_rooms`: Clears in-memory rooms dict before/after each test
- `clear_problems_cache`: Resets problem index cache for mocking

## Important Implementation Details

### Multi-Round Rooms
Rooms support multiple rounds via `total_rounds` config. Between rounds, a 30-second break is shown before auto-starting the next round.

### Code Golf Scoring
When a player solves a problem, their solution is scored by character count (excluding whitespace). The exact logic is in `sandbox.py`'s `count_chars()` function.

### Exponent Formatting
Problem descriptions from LeetCode may contain collapsed notation like '10^5' or '105'. `server/utils.py` provides `fix_exponents()` to convert these to Unicode superscripts for display.

### Problem Indexing
The `problems/index.json` file catalogs all problems with metadata (id, title, difficulty, category). Individual problems are loaded on-demand from `problems/{id}.json`.
