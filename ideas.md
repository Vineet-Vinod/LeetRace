# LeetRace - Feature Ideas

## Gameplay

- **Live typing indicators** — show opponents' character counts updating in real-time (without revealing code), so you feel the race pressure
- **Multiple language support** — let players pick Python, JS, Go, etc. per round; compare by char count across languages or separate leaderboards
- **Difficulty progression** — in multi-round games, automatically escalate difficulty (Easy → Medium → Hard)
- **Practice/solo mode** — play against the clock without needing a second player, track personal bests
- **Custom problem pools** — filter by topic tags (arrays, trees, DP, etc.) when creating a room

## Competitive

- **ELO rating system** — persistent player accounts with ratings that update after each match
- **Match history & replays** — save games, let players review the winning solution's code afterward
- **Global leaderboard** — weekly/all-time rankings by win rate, average char count, fastest solves
- **Tournament mode** — bracket-style elimination across multiple rooms

## UX Polish

- **Shareable invite links** — `/room?id=ABC123` link you can send directly instead of dictating a code
- **Rich problem rendering** — parse markdown/HTML in descriptions so code blocks, bold, lists render properly instead of plain text
- **Individual test case results** — show which specific test cases pass/fail with their input/output, not just a count
- **Sound effects** — subtle audio cues for countdown warnings, opponent solving, lock-in
- **Reconnection support** — if you disconnect mid-game, rejoin the room and resume where you left off
- **In-lobby chat** — simple text chat while waiting for everyone to join

## Technical / Infrastructure

- **Persistent accounts** — login with GitHub/Google, track stats over time
- **Room passwords** — private rooms for organized competitions
- **Anti-cheat** — detect suspicious paste events or impossibly fast solves
- **Containerized sandbox** — Docker-based code execution for better isolation and multi-language support
