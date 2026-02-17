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
let submitted = false;

ws.onopen = () => {
    ws.send(JSON.stringify({ type: 'join', name: playerName }));
};

ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    handlers[msg.type]?.(msg);
};

ws.onclose = () => {
    if (!submitted) {
        showFeedback('Disconnected from server', 'fail');
    }
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
        submitted = false;
        showScreen(playingScreen);

        const p = msg.problem;
        document.getElementById('problem-title').textContent = p.title;

        const badge = document.getElementById('problem-difficulty');
        badge.textContent = p.difficulty;
        badge.className = 'difficulty-badge ' + p.difficulty.toLowerCase();

        document.getElementById('problem-description').textContent = p.description;

        // Init editor
        initEditor('editor-container', p.starter_code, (code) => {
            document.getElementById('char-count').textContent = `Chars: ${charCount(code)}`;
        });

        // Timer
        updateTimer(msg.time_limit);

        // Reset scoreboard
        document.getElementById('live-scoreboard').hidden = true;
        document.getElementById('live-scoreboard').innerHTML = '';

        // Submit button
        const submitBtn = document.getElementById('submit-btn');
        submitBtn.disabled = false;
    },

    tick(msg) {
        updateTimer(msg.remaining);
    },

    submit_result(msg) {
        submitted = true;
        setEditorReadOnly(true);
        document.getElementById('submit-btn').disabled = true;

        if (msg.solved) {
            showFeedback(`Solved! ${msg.char_count} chars in ${msg.submit_time}s`, 'success');
        } else {
            const text = msg.error
                ? `${msg.passed}/${msg.total} tests passed - ${msg.error}`
                : `${msg.passed}/${msg.total} tests passed`;
            showFeedback(text, 'fail');
        }
    },

    scoreboard(msg) {
        updateLiveScoreboard(msg.rankings);
    },

    game_over(msg) {
        gameActive = false;
        showScreen(finishedScreen);
        renderFinalRankings(msg.rankings);
    },

    error(msg) {
        showFeedback(msg.message, 'fail');
    },
};

// UI helpers

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
        const status = r.solved
            ? `<span class="rank-solved">${r.char_count} chars</span>`
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
        const stats = r.solved
            ? `<span class="rank-solved">Solved</span>
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

document.getElementById('submit-btn').addEventListener('click', () => {
    if (submitted) return;
    const code = getCode();
    if (!code.trim()) {
        showFeedback('Write some code first!', 'fail');
        return;
    }
    ws.send(JSON.stringify({ type: 'submit', code }));
    document.getElementById('submit-btn').disabled = true;
});

document.getElementById('play-again-btn').addEventListener('click', () => {
    window.location.href = '/';
});
