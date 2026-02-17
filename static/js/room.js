/* Room page: WebSocket client, game state machine, UI updates */

const params = new URLSearchParams(window.location.search);
const roomId = params.get('id');
const playerName = params.get('name');

if (!roomId || !playerName) {
    window.location.href = '/';
}

// Screens
const lobbyScreen = document.getElementById('lobby');
const playingScreen = document.getElementById('playing');
const finishedScreen = document.getElementById('finished');

function showScreen(screen) {
    [lobbyScreen, playingScreen, finishedScreen].forEach(s => s.classList.remove('active'));
    screen.classList.add('active');
}

// WebSocket
const wsProto = location.protocol === 'https:' ? 'wss' : 'ws';
const ws = new WebSocket(`${wsProto}://${location.host}/ws/${roomId}`);

let isHost = false;
let gameActive = false;
let lockedIn = false;
let submitCooldown = false;
let timerInterval = null;
let remainingSeconds = 0;

ws.onopen = () => {
    ws.send(JSON.stringify({ type: 'join', name: playerName }));
};

ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    handlers[msg.type]?.(msg);
};

ws.onclose = () => {
    showFeedback('Disconnected from server', 'fail');
};

const handlers = {
    room_state(msg) {
        isHost = msg.host === playerName;
        showScreen(lobbyScreen);

        document.getElementById('lobby-room-id').textContent = msg.room_id;

        const playerList = document.getElementById('lobby-players');
        playerList.innerHTML = msg.players.map(p =>
            `<span class="player-chip ${p === msg.host ? 'host' : ''}">${esc(p)}${p === msg.host ? ' (host)' : ''}</span>`
        ).join('');

        const diff = msg.difficulty || 'Any';
        document.getElementById('lobby-difficulty').textContent = `Difficulty: ${diff}`;
        document.getElementById('lobby-time').textContent = `Time: ${msg.time_limit}s`;
        document.getElementById('lobby-rounds').textContent = `Rounds: ${msg.total_rounds}`;

        const startBtn = document.getElementById('start-btn');
        const waitingMsg = document.getElementById('lobby-waiting');
        if (isHost) {
            startBtn.hidden = false;
            waitingMsg.hidden = true;
        } else {
            startBtn.hidden = true;
            waitingMsg.hidden = false;
        }
    },

    game_start(msg) {
        gameActive = true;
        lockedIn = false;
        submitCooldown = false;
        showScreen(playingScreen);

        const p = msg.problem;
        document.getElementById('problem-title').textContent = p.title;

        const badge = document.getElementById('problem-difficulty');
        badge.textContent = p.difficulty;
        badge.className = 'difficulty-badge ' + p.difficulty.toLowerCase();

        document.getElementById('problem-description').textContent = p.description;

        // Round info
        const roundEl = document.getElementById('round-info');
        if (msg.total_rounds > 1) {
            roundEl.textContent = `Round ${msg.current_round}/${msg.total_rounds}`;
            roundEl.hidden = false;
        } else {
            roundEl.hidden = true;
        }

        // Init editor
        initEditor('editor-container', p.starter_code, (code) => {
            document.getElementById('char-count').textContent = `Chars: ${charCount(code)}`;
        });
        setEditorSubmitCallback(submitCode);
        setEditorReadOnly(false);

        // Timer - start client-side countdown
        startTimer(msg.time_limit);

        // Reset scoreboard and output
        document.getElementById('live-scoreboard').hidden = true;
        document.getElementById('live-scoreboard').innerHTML = '';
        document.getElementById('output-panel').hidden = true;
        document.getElementById('resize-h').hidden = true;

        // Buttons
        document.getElementById('submit-btn').disabled = false;
        document.getElementById('lock-btn').hidden = true;
        document.getElementById('lock-btn').disabled = false;
        document.getElementById('lock-btn').textContent = 'Lock In';
    },

    tick(msg) {
        // Sync with server time
        remainingSeconds = msg.remaining;
    },

    submit_result(msg) {
        if (msg.solved) {
            showFeedback(`Solved! ${msg.char_count} chars in ${msg.submit_time}s`, 'success');
            if (!lockedIn) document.getElementById('lock-btn').hidden = false;
        } else {
            const text = msg.error
                ? `${msg.passed}/${msg.total} tests passed - ${msg.error}`
                : `${msg.passed}/${msg.total} tests passed`;
            showFeedback(text, 'fail');
            document.getElementById('lock-btn').hidden = true;
        }

        const lines = [];
        lines.push(`Tests: ${msg.passed}/${msg.total} passed`);
        if (msg.error) lines.push(`Error: ${msg.error}`);
        if (msg.stdout) lines.push(`\nStdout:\n${msg.stdout}`);
        if (msg.stderr) lines.push(`\nStderr:\n${msg.stderr}`);

        const panel = document.getElementById('output-panel');
        const content = document.getElementById('output-content');
        content.textContent = lines.join('\n');
        panel.hidden = false;
        document.getElementById('resize-h').hidden = false;
    },

    locked() {
        lockedIn = true;
        setEditorReadOnly(true);
        document.getElementById('submit-btn').disabled = true;
        document.getElementById('lock-btn').disabled = true;
        document.getElementById('lock-btn').textContent = 'Locked In';
        showFeedback('Locked in! Your solution is final.', 'success');
    },

    scoreboard(msg) {
        updateLiveScoreboard(msg.rankings);
    },

    round_over(msg) {
        gameActive = false;
        clearInterval(timerInterval);
        showScreen(finishedScreen);
        renderFinalRankings(msg.rankings);

        document.getElementById('finished-title').textContent =
            `Round ${msg.current_round}/${msg.total_rounds} Complete`;
        document.getElementById('break-countdown').hidden = false;
        document.getElementById('break-countdown').textContent =
            `Next round in ${msg.break_seconds}s...`;
        document.getElementById('play-again-btn').hidden = true;
        document.getElementById('finished-waiting').hidden = true;
    },

    break_tick(msg) {
        document.getElementById('break-countdown').textContent =
            `Next round in ${msg.remaining}s...`;
    },

    game_over(msg) {
        gameActive = false;
        clearInterval(timerInterval);
        showScreen(finishedScreen);
        renderFinalRankings(msg.rankings);

        document.getElementById('finished-title').textContent = 'Game Over!';
        document.getElementById('break-countdown').hidden = true;
        document.getElementById('play-again-btn').hidden = !isHost;
        document.getElementById('finished-waiting').hidden = isHost;
    },

    error(msg) {
        showFeedback(msg.message, 'fail');
    },
};

// UI helpers

function startTimer(seconds) {
    clearInterval(timerInterval);
    remainingSeconds = seconds;
    updateTimer(remainingSeconds);
    timerInterval = setInterval(() => {
        remainingSeconds = Math.max(0, remainingSeconds - 1);
        updateTimer(remainingSeconds);
    }, 1000);
}

function updateTimer(remaining) {
    const el = document.getElementById('timer');
    const min = Math.floor(remaining / 60);
    const sec = remaining % 60;
    el.textContent = `${min}:${sec.toString().padStart(2, '0')}`;

    el.className = 'timer';
    if (remaining <= 30) el.classList.add('danger');
    else if (remaining <= 60) el.classList.add('warning');
}

function updateLiveScoreboard(rankings) {
    const bar = document.getElementById('live-scoreboard');
    bar.hidden = false;
    bar.innerHTML = rankings.map(r => {
        const locked = r.locked_at !== null;
        const status = r.solved
            ? `<span class="rank-solved">${r.char_count} chars${locked ? ' \u{1f512}' : ''}</span>`
            : r.tests_passed > 0
                ? `${r.tests_passed}/${r.tests_total}`
                : 'pending';
        return `<div class="score-entry ${r.solved ? 'solved' : ''}">
            <span class="rank">#${r.position}</span>
            <span>${esc(r.name)}</span>
            <span>${status}</span>
        </div>`;
    }).join('');
}

function renderFinalRankings(rankings) {
    const el = document.getElementById('final-rankings');
    el.innerHTML = rankings.map(r => {
        const locked = r.locked_at !== null;
        const stats = r.solved
            ? `<span class="rank-solved">Solved${locked ? ' \u{1f512}' : ''}</span>
               <span>${r.char_count} chars</span>
               <span>${r.submit_time}s</span>`
            : `<span class="rank-failed">${r.tests_passed}/${r.tests_total} tests</span>`;
        return `<div class="rank-row">
            <span class="rank-position">#${r.position}</span>
            <span class="rank-name">${esc(r.name)}</span>
            <div class="rank-stats">${stats}</div>
        </div>`;
    }).join('');
}

function showFeedback(text, type) {
    const el = document.getElementById('submit-feedback');
    el.textContent = text;
    el.className = `feedback ${type}`;
    el.hidden = false;
    setTimeout(() => { el.hidden = true; }, 5000);
}

function esc(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

// Button handlers

document.getElementById('start-btn').addEventListener('click', () => {
    ws.send(JSON.stringify({ type: 'start' }));
});

function submitCode() {
    if (lockedIn || submitCooldown || !gameActive) return;
    const code = getCode();
    if (!code.trim()) {
        showFeedback('Write some code first!', 'fail');
        return;
    }
    ws.send(JSON.stringify({ type: 'submit', code }));
    submitCooldown = true;
    document.getElementById('submit-btn').disabled = true;
    setTimeout(() => {
        submitCooldown = false;
        if (gameActive) document.getElementById('submit-btn').disabled = false;
    }, 1000);
}

document.getElementById('submit-btn').addEventListener('click', submitCode);

document.getElementById('lock-btn').addEventListener('click', () => {
    if (lockedIn || !gameActive) return;
    ws.send(JSON.stringify({ type: 'lock' }));
});

document.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'Enter') {
        e.preventDefault();
        submitCode();
    }
});

document.getElementById('play-again-btn').addEventListener('click', () => {
    ws.send(JSON.stringify({ type: 'restart' }));
});
