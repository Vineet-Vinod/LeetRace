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
let reviewMode = false;

// Rankings saved when a round or game ends so the review mode tab bar can
// access each player's submitted code. Entries come from rank_players() on
// the server and include a `code` field (null when the player never submitted).
let lastRankings = [];

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
        reviewMode = false;
        showScreen(playingScreen);

        // Restore game UI from review mode
        document.getElementById('submit-btn').hidden = false;
        document.getElementById('timer').hidden = false;
        document.getElementById('char-count').hidden = false;
        document.getElementById('back-to-results-btn').hidden = true;

        const p = msg.problem;
        document.getElementById('problem-title').textContent = p.title;

        const badge = document.getElementById('problem-difficulty');
        badge.textContent = p.difficulty;
        badge.className = 'difficulty-badge ' + p.difficulty.toLowerCase();

        renderDescription(document.getElementById('problem-description'), p.description);

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
        // Persist rankings so the review tab bar can reference each player's code.
        lastRankings = msg.rankings;
        showScreen(finishedScreen);
        renderFinalRankings(msg.rankings);

        document.getElementById('finished-title').textContent =
            `Round ${msg.current_round}/${msg.total_rounds} Complete`;
        document.getElementById('break-countdown').hidden = false;
        document.getElementById('break-countdown').textContent =
            `Next round in ${msg.break_seconds}s...`;
        document.getElementById('view-code-btn').hidden = false;
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
        // Persist rankings so the review tab bar can reference each player's code.
        lastRankings = msg.rankings;
        showScreen(finishedScreen);
        renderFinalRankings(msg.rankings);

        document.getElementById('finished-title').textContent = 'Game Over!';
        document.getElementById('break-countdown').hidden = true;
        document.getElementById('view-code-btn').hidden = false;
        document.getElementById('play-again-btn').hidden = !isHost;
        document.getElementById('finished-waiting').hidden = isHost;
    },

    error(msg) {
        showFeedback(msg.message, 'fail');
    },

    chat(msg) {
        appendChatMessage(msg.sender, msg.message);
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

// escHtml is the same DOM-based escape used by esc(), exposed with a name that
// makes the intent clear at call sites inside renderDescription().
const escHtml = esc;

/**
 * Render a structured problem description into the given container element.
 *
 * Attempts to parse the raw description text with parseDescription(). If
 * parsing throws or returns nothing useful, falls back to plain text so the
 * player always sees the problem content.
 *
 * @param {HTMLElement} container - The #problem-description element
 * @param {string} rawText - Raw description string from the server
 */
function renderDescription(container, rawText) {
    // Defensive: always show something even if the parser fails or is not yet
    // available (parseDescription is assigned to window by an inline module script
    // in room.html; it should always be ready before a WebSocket game_start fires).
    let parsed = null;
    try {
        if (typeof parseDescription !== 'function') throw new Error('parser not loaded');
        parsed = parseDescription(rawText);
    } catch (e) {
        // Parser threw or isn't available — fall back to plain text
        container.textContent = rawText;
        return;
    }

    // If the parser returned no meaningful content, fall back to plain text
    if (!parsed || (!parsed.statement && parsed.examples.length === 0 && parsed.constraints.length === 0)) {
        container.textContent = rawText;
        return;
    }

    // Build HTML using template literals. All user-sourced text goes through
    // escHtml() to prevent XSS. Unicode superscripts produced by fix_exponents()
    // on the server survive escaping because they are ordinary Unicode characters,
    // not HTML entities. Code brackets like [1,2,3] also survive correctly.

    const parts = [];

    // --- Problem statement ---
    if (parsed.statement) {
        // The statement may contain \n within paragraphs; convert them to <br>
        // so paragraph structure is preserved without switching to <pre>.
        const stmtHtml = escHtml(parsed.statement)
            // Blank lines (two consecutive newlines) become paragraph breaks
            .replace(/\n{2,}/g, '</p><p>')
            // Single newlines become line breaks
            .replace(/\n/g, '<br>');
        parts.push(`<p class="problem-statement">${stmtHtml}</p>`);
    }

    // --- Examples ---
    parsed.examples.forEach(ex => {
        const inputHtml = ex.input ? `<div class="example-input"><span class="example-field-label">Input:</span> <code>${escHtml(ex.input)}</code></div>` : '';
        const outputHtml = ex.output ? `<div class="example-output"><span class="example-field-label">Output:</span> <code>${escHtml(ex.output)}</code></div>` : '';
        // Explanation may contain embedded newlines for multi-step content (e.g.
        // "1. step\n2. step"); convert them to <br> so they render visually.
        const explanationHtml = ex.explanation
            ? `<div class="example-explanation"><span class="example-field-label">Explanation:</span> ${escHtml(ex.explanation).replace(/\n/g, '<br>')}</div>`
            : '';

        parts.push(`
<section class="example-block">
    <div class="example-label">Example ${escHtml(String(ex.number))}:</div>
    ${inputHtml}
    ${outputHtml}
    ${explanationHtml}
</section>`);
    });

    // --- Constraints ---
    if (parsed.constraints.length > 0) {
        const items = parsed.constraints
            .map(c => `<li>${escHtml(c)}</li>`)
            .join('');
        parts.push(`
<section class="constraints-section">
    <div class="constraints-label">Constraints:</div>
    <ul class="constraint-list">${items}</ul>
</section>`);
    }

    // --- Follow-up ---
    if (parsed.followUp) {
        parts.push(`
<section class="follow-up-section">
    <span class="follow-up-label">Follow-up:</span> ${escHtml(parsed.followUp)}
</section>`);
    }

    container.innerHTML = parts.join('');
}

/**
 * Build the opponent code tab bar and show it above the editor.
 *
 * Each entry in `rankings` is a rank_players() dict that now includes a `code`
 * field. Tabs are ordered by final position. Clicking a tab loads that player's
 * code into the (read-only) editor. The local player's own tab is pre-selected
 * on open so they have a reference point before browsing opponents.
 *
 * @param {Array} rankings - Ranking entries from game_over / round_over message.
 */
function buildCodeTabs(rankings) {
    const tabBar = document.getElementById('code-tabs');
    tabBar.innerHTML = '';
    tabBar.setAttribute('role', 'tablist');

    if (rankings.length === 0) {
        tabBar.hidden = true;
        return;
    }

    rankings.forEach((entry, idx) => {
        const btn = document.createElement('button');
        btn.className = 'code-tab';
        btn.setAttribute('role', 'tab');
        btn.setAttribute('aria-selected', 'false');
        // Indicate solve status with a visual class so players can spot
        // who solved the problem at a glance without reading the rankings.
        if (entry.solved) {
            btn.classList.add('code-tab-solved');
        } else if (entry.code !== null && entry.code !== undefined) {
            btn.classList.add('code-tab-attempted');
        } else {
            btn.classList.add('code-tab-none');
        }

        // Show position + name. Use esc() for the name to avoid XSS since
        // player names are user-supplied strings.
        btn.innerHTML = `<span class="code-tab-pos">#${entry.position}</span> ${esc(entry.name)}`;
        btn.dataset.index = idx;
        btn.addEventListener('click', () => showCodeTab(rankings, idx, tabBar));
        tabBar.appendChild(btn);
    });

    tabBar.hidden = false;

    // Pre-select the local player's tab; fall back to position 0 if not found.
    const selfIdx = rankings.findIndex(r => r.name === playerName);
    showCodeTab(rankings, selfIdx >= 0 ? selfIdx : 0, tabBar);
}

/**
 * Activate a specific code tab and load the player's code into the editor.
 *
 * @param {Array}       rankings - Full rankings array.
 * @param {number}      idx      - Index into rankings to display.
 * @param {HTMLElement} tabBar   - The #code-tabs container element.
 */
function showCodeTab(rankings, idx, tabBar) {
    const entry = rankings[idx];

    // Mark the clicked tab active, clear all others.
    tabBar.querySelectorAll('.code-tab').forEach((btn, i) => {
        btn.classList.toggle('code-tab-active', i === idx);
        btn.setAttribute('aria-selected', i === idx ? 'true' : 'false');
    });

    const NO_SUBMISSION_PLACEHOLDER = '# No submission';

    // Load code into the editor. editor.setValue() works even in read-only mode.
    const code = (entry.code !== null && entry.code !== undefined)
        ? entry.code
        : NO_SUBMISSION_PLACEHOLDER;

    if (typeof editor !== 'undefined' && editor) {
        editor.setValue(code);
    }
}

// Button handlers

document.getElementById('start-btn').addEventListener('click', () => {
    ws.send(JSON.stringify({ type: 'start' }));
});

document.getElementById('copy-invite-btn').addEventListener('click', () => {
    // Construct the full invite URL using the roomId already parsed from the
    // query string at the top of this file — no need to re-read the DOM.
    const inviteUrl = `${location.origin}/room?id=${roomId}`;
    navigator.clipboard.writeText(inviteUrl).then(() => {
        const btn = document.getElementById('copy-invite-btn');
        const originalText = btn.textContent;
        btn.textContent = 'Copied!';
        btn.classList.add('btn-invite-copied');
        // Reset button text after 2 seconds so the user can copy again
        setTimeout(() => {
            btn.textContent = originalText;
            btn.classList.remove('btn-invite-copied');
        }, 2000);
    }).catch(() => {
        // Clipboard API can fail if the page is not focused or permissions are
        // denied — fall back to a visible error in the existing feedback toast.
        showFeedback('Could not copy link — please copy it manually.', 'fail');
    });
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

document.getElementById('view-code-btn').addEventListener('click', () => {
    reviewMode = true;
    showScreen(playingScreen);
    setEditorReadOnly(true);

    // Hide game controls, show back button
    document.getElementById('submit-btn').hidden = true;
    document.getElementById('lock-btn').hidden = true;
    document.getElementById('timer').hidden = true;
    document.getElementById('char-count').hidden = true;
    document.getElementById('back-to-results-btn').hidden = false;
    document.getElementById('live-scoreboard').hidden = true;

    // Build and reveal the player tab bar using the stored end-of-game rankings.
    buildCodeTabs(lastRankings);
});

document.getElementById('back-to-results-btn').addEventListener('click', () => {
    reviewMode = false;
    showScreen(finishedScreen);
    document.getElementById('back-to-results-btn').hidden = true;
    // Hide and clear the tab bar so it is rebuilt fresh if the player opens
    // review mode again (e.g. after a multi-round break refreshes rankings).
    const tabBar = document.getElementById('code-tabs');
    tabBar.hidden = true;
    tabBar.innerHTML = '';
});

// === Chat ===

let chatCollapsed = false;
const MAX_CHAT_MESSAGES = 200;

/**
 * Append a chat message bubble to #chat-messages and auto-scroll to the bottom.
 * Text is set via textContent (not innerHTML) so no further escaping is needed.
 *
 * @param {string} sender - The player name who sent the message
 * @param {string} text   - The sanitized message body
 */
function appendChatMessage(sender, text) {
    const container = document.getElementById('chat-messages');

    const bubble = document.createElement('div');
    bubble.className = 'chat-bubble' + (sender === playerName ? ' chat-bubble-self' : '');

    const nameEl = document.createElement('span');
    nameEl.className = 'chat-sender';
    nameEl.textContent = sender;

    const textEl = document.createElement('span');
    textEl.className = 'chat-text';
    textEl.textContent = text;

    bubble.appendChild(nameEl);
    bubble.appendChild(textEl);
    container.appendChild(bubble);

    // Cap DOM size to prevent memory growth in long sessions.
    while (container.children.length > MAX_CHAT_MESSAGES) {
        container.removeChild(container.firstChild);
    }

    // Only auto-scroll when the panel is open so we don't silently consume scroll
    // state while collapsed. The unread badge (below) covers the collapsed case.
    if (!chatCollapsed) {
        container.scrollTop = container.scrollHeight;
    } else {
        // Show an unread indicator on the header when collapsed
        const toggle = document.getElementById('chat-toggle');
        toggle.classList.add('chat-has-unread');
    }
}

let chatCooldown = false;

function sendChatMessage() {
    const input = document.getElementById('chat-input');
    const text = input.value.trim();
    if (!text || chatCooldown) return;

    ws.send(JSON.stringify({ type: 'chat', message: text }));
    input.value = '';

    chatCooldown = true;
    setTimeout(() => { chatCooldown = false; }, 500);
}

document.getElementById('chat-send').addEventListener('click', sendChatMessage);

document.getElementById('chat-input').addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault();
        sendChatMessage();
    }
});

// Collapse/expand the chat panel body; keep the header always visible.
document.getElementById('chat-toggle').addEventListener('click', () => {
    const panel = document.getElementById('chat-panel');
    chatCollapsed = !chatCollapsed;
    panel.classList.toggle('chat-collapsed', chatCollapsed);

    const toggle = document.getElementById('chat-toggle');
    // Update arrow direction and clear any unread indicator on expand
    toggle.innerHTML = chatCollapsed ? '&#x25B2;' : '&#x25BC;';
    if (!chatCollapsed) {
        toggle.classList.remove('chat-has-unread');
        // Scroll to bottom now that the messages area is visible again
        const container = document.getElementById('chat-messages');
        container.scrollTop = container.scrollHeight;
    }
});
