import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';

export default function Landing() {
  const navigate = useNavigate();
  const [name, setName] = useState('');
  const [difficulty, setDifficulty] = useState('');
  const [timeLimit, setTimeLimit] = useState(300);
  const [rounds, setRounds] = useState(1);
  const [roomCode, setRoomCode] = useState('');
  const [error, setError] = useState('');
  const [creating, setCreating] = useState(false);

  function showError(msg) {
    setError(msg);
    setTimeout(() => setError(''), 4000);
  }

  function getName() {
    const trimmed = name.trim();
    if (!trimmed) {
      showError('Please enter your name');
      return null;
    }
    return trimmed;
  }

  async function handleCreate() {
    const playerName = getName();
    if (!playerName) return;

    setCreating(true);
    try {
      const res = await fetch('/api/rooms', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          host: playerName,
          difficulty: difficulty || null,
          time_limit: parseInt(timeLimit) || 300,
          rounds: parseInt(rounds) || 1,
        }),
      });
      const data = await res.json();
      if (data.room_id) {
        navigate(`/room?id=${data.room_id}&name=${encodeURIComponent(playerName)}`);
      } else {
        showError('Failed to create room');
      }
    } catch {
      showError('Network error');
    } finally {
      setCreating(false);
    }
  }

  function handleJoin() {
    const playerName = getName();
    if (!playerName) return;
    const code = roomCode.trim().toUpperCase();
    if (!code || code.length !== 6) {
      showError('Enter a valid 6-character room code');
      return;
    }
    navigate(`/room?id=${code}&name=${encodeURIComponent(playerName)}`);
  }

  return (
    <div className="relative z-1 flex flex-col items-center justify-center min-h-screen p-8 overflow-y-auto">
      <motion.h1
        initial={{ opacity: 0, y: -30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
        className="font-display font-black text-5xl tracking-[4px] uppercase text-txt mb-2"
        style={{ textShadow: '0 0 15px rgba(240,160,48,0.25), 0 0 40px rgba(240,160,48,0.08)' }}
      >
        Leet<span className="text-accent">Race</span>
      </motion.h1>

      <motion.p
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2, duration: 0.5 }}
        className="font-heading text-txt-secondary text-sm tracking-[2px] uppercase mb-12"
      >
        Race to solve. Fewest characters wins.
      </motion.p>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3, duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
        className="card-glow bg-surface border border-white/[0.06] rounded-xl p-8 w-full max-w-[520px] backdrop-blur-lg"
      >
        {/* Name input */}
        <label className="block font-heading text-xs font-semibold text-txt-dim uppercase tracking-[1px] mb-1">
          Your Name
        </label>
        <input
          type="text"
          maxLength={20}
          value={name}
          onChange={(e) => setName(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleCreate()}
          placeholder="Enter your name"
          autoFocus
          className="w-full px-3.5 py-2.5 bg-input-bg border border-white/[0.06] rounded text-txt font-body text-base outline-none transition-all duration-250 focus:border-accent focus:shadow-[0_0_0_2px_rgba(240,160,48,0.1)] placeholder:text-txt-dim"
        />

        {/* Create room section */}
        <div className="mt-8">
          <h2 className="font-heading text-sm font-semibold text-txt-secondary uppercase tracking-[1.5px] mb-4">
            Create a Room
          </h2>

          <div className="flex gap-3 items-end">
            <div className="flex-1">
              <label className="block font-heading text-xs font-semibold text-txt-dim uppercase tracking-[1px] mb-1">
                Difficulty
              </label>
              <select
                value={difficulty}
                onChange={(e) => setDifficulty(e.target.value)}
                className="w-full px-3 py-2.5 bg-input-bg border border-white/[0.06] rounded text-txt font-body text-base outline-none transition-all duration-250 focus:border-accent"
              >
                <option value="">Any</option>
                <option value="Easy">Easy</option>
                <option value="Medium">Medium</option>
                <option value="Hard">Hard</option>
              </select>
            </div>

            <div className="flex-1">
              <label className="block font-heading text-xs font-semibold text-txt-dim uppercase tracking-[1px] mb-1">
                Time (sec)
              </label>
              <input
                type="number"
                value={timeLimit}
                onChange={(e) => setTimeLimit(e.target.value)}
                min="1"
                step="30"
                className="w-full px-3 py-2.5 bg-input-bg border border-white/[0.06] rounded text-txt font-body text-base outline-none transition-all duration-250 focus:border-accent"
              />
            </div>

            <div className="flex-1">
              <label className="block font-heading text-xs font-semibold text-txt-dim uppercase tracking-[1px] mb-1">
                Rounds
              </label>
              <input
                type="number"
                value={rounds}
                onChange={(e) => setRounds(e.target.value)}
                min="1"
                max="10"
                step="1"
                className="w-full px-3 py-2.5 bg-input-bg border border-white/[0.06] rounded text-txt font-body text-base outline-none transition-all duration-250 focus:border-accent"
              />
            </div>
          </div>

          <motion.button
            whileHover={{ scale: 1.01 }}
            whileTap={{ scale: 0.97 }}
            onClick={handleCreate}
            disabled={creating}
            className="w-full mt-4 py-3 font-heading font-bold text-sm uppercase tracking-wider rounded bg-gradient-to-br from-accent to-accent-dim text-void border border-accent shadow-glow-accent cursor-pointer transition-all duration-200 hover:shadow-glow-accent-lg disabled:opacity-40 disabled:cursor-not-allowed"
          >
            {creating ? 'Creating...' : 'Create Room'}
          </motion.button>
        </div>

        {/* Divider */}
        <div className="flex items-center my-8 text-txt-dim font-heading text-xs tracking-[2px] uppercase">
          <div className="flex-1 border-b border-white/[0.06]" />
          <span className="px-4">or</span>
          <div className="flex-1 border-b border-white/[0.06]" />
        </div>

        {/* Join room section */}
        <div>
          <h2 className="font-heading text-sm font-semibold text-txt-secondary uppercase tracking-[1.5px] mb-4">
            Join a Room
          </h2>
          <div className="flex gap-3 items-end">
            <input
              type="text"
              maxLength={6}
              value={roomCode}
              onChange={(e) => setRoomCode(e.target.value.toUpperCase())}
              onKeyDown={(e) => e.key === 'Enter' && handleJoin()}
              placeholder="Room code"
              className="flex-1 px-3.5 py-2.5 bg-input-bg border border-white/[0.06] rounded text-txt font-body text-base outline-none uppercase tracking-[3px] transition-all duration-250 focus:border-accent focus:shadow-[0_0_0_2px_rgba(240,160,48,0.1)] placeholder:text-txt-dim placeholder:tracking-normal"
            />
            <motion.button
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.96 }}
              onClick={handleJoin}
              className="px-6 py-2.5 bg-transparent border border-white/10 rounded font-heading font-semibold text-sm uppercase tracking-wider text-txt-secondary cursor-pointer transition-all duration-200 hover:border-accent hover:text-accent whitespace-nowrap"
            >
              Join
            </motion.button>
          </div>
        </div>

        {/* Error */}
        <AnimatePresence>
          {error && (
            <motion.p
              initial={{ opacity: 0, y: 5 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -5 }}
              className="text-danger font-heading text-sm text-center mt-4"
            >
              {error}
            </motion.p>
          )}
        </AnimatePresence>
      </motion.div>
    </div>
  );
}
