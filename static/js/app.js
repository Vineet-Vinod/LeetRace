/* Landing page logic: create/join rooms */

const nameInput = document.getElementById('player-name');
const createBtn = document.getElementById('create-btn');
const joinBtn = document.getElementById('join-btn');
const roomCodeInput = document.getElementById('room-code');
const difficultySelect = document.getElementById('difficulty');
const timeLimitInput = document.getElementById('time-limit');
const errorMsg = document.getElementById('error-msg');

function showError(msg) {
    errorMsg.textContent = msg;
    errorMsg.hidden = false;
    setTimeout(() => { errorMsg.hidden = true; }, 4000);
}

function getName() {
    const name = nameInput.value.trim();
    if (!name) {
        showError('Please enter your name');
        return null;
    }
    return name;
}

createBtn.addEventListener('click', async () => {
    const name = getName();
    if (!name) return;

    createBtn.disabled = true;
    try {
        const res = await fetch('/api/rooms', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                host: name,
                difficulty: difficultySelect.value || null,
                time_limit: parseInt(timeLimitInput.value) || 300,
            }),
        });
        const data = await res.json();
        if (data.room_id) {
            window.location.href = `/room?id=${data.room_id}&name=${encodeURIComponent(name)}`;
        } else {
            showError('Failed to create room');
        }
    } catch (e) {
        showError('Network error');
    } finally {
        createBtn.disabled = false;
    }
});

joinBtn.addEventListener('click', () => {
    const name = getName();
    if (!name) return;

    const code = roomCodeInput.value.trim().toUpperCase();
    if (!code || code.length !== 6) {
        showError('Enter a valid 6-character room code');
        return;
    }

    window.location.href = `/room?id=${code}&name=${encodeURIComponent(name)}`;
});

// Allow Enter key on room code input
roomCodeInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') joinBtn.click();
});

nameInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') createBtn.click();
});
