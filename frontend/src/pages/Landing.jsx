import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';

const DIFFICULTIES = [
  { value: null, label: 'Any', style: 'active-any' },
  { value: 'Easy', label: 'Easy', style: 'active-easy' },
  { value: 'Medium', label: 'Medium', style: 'active-med' },
  { value: 'Hard', label: 'Hard', style: 'active-hard' },
];

const diffActiveClass = {
  'active-any': 'bg-accent/12 border-accent/30 text-accent-bright',
  'active-easy': 'bg-ok/12 border-ok/30 text-ok',
  'active-med': 'bg-warn/12 border-warn/30 text-warn',
  'active-hard': 'bg-err/12 border-err/30 text-err',
};

export default function Landing() {
  const navigate = useNavigate();
  const [tab, setTab] = useState('create');
  const [name, setName] = useState('');
  const [difficulty, setDifficulty] = useState(null);
  const [timeLimit, setTimeLimit] = useState(5);
  const [rounds, setRounds] = useState(1);
  const [roomCode, setRoomCode] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleCreate = async (e) => {
    e.preventDefault();
    const trimmed = name.trim();
    if (!trimmed) return setError('Enter your name');
    if (trimmed.length > 20) return setError('Name must be 20 characters or fewer');
    if (timeLimit < 1) return setError('Time limit must be at least 1 minute');
    if (rounds < 1 || rounds > 10) return setError('Rounds must be 1–10');

    setError('');
    setLoading(true);
    try {
      const res = await fetch('/api/rooms', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          host: trimmed,
          difficulty,
          time_limit: Math.round(timeLimit * 60),
          rounds,
        }),
      });
      if (!res.ok) throw new Error('Failed to create room');
      const data = await res.json();
      navigate(`/room?id=${data.room_id}&name=${encodeURIComponent(trimmed)}`);
    } catch (err) {
      setError(err.message || 'Something went wrong');
    } finally {
      setLoading(false);
    }
  };

  const handleJoin = (e) => {
    e.preventDefault();
    const trimmed = name.trim();
    const code = roomCode.trim().toUpperCase();
    if (!trimmed) return setError('Enter your name');
    if (trimmed.length > 20) return setError('Name must be 20 characters or fewer');
    if (code.length !== 6) return setError('Room code must be 6 characters');
    setError('');
    navigate(`/room?id=${code}&name=${encodeURIComponent(trimmed)}`);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center px-5 py-10 relative">
      {/* Ambient glow */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[600px] h-[600px] bg-[radial-gradient(circle,rgba(0,229,199,0.06)_0%,transparent_70%)] pointer-events-none" />

      {/* Logo */}
      <motion.h1
        initial={{ opacity: 0, y: -20, scale: 0.95 }}
        animate={{ opacity: 1, y: 0, scale: 1 }}
        transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
        className="font-display font-bold tracking-[0.25em] uppercase text-light relative z-10 mb-1"
        style={{ fontSize: 'clamp(2.6rem, 6vw, 4.2rem)' }}
      >
        LEET<span className="text-primary" style={{ textShadow: '0 0 30px rgba(0,229,199,0.3)' }}>RACE</span>
      </motion.h1>

      <motion.p
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.25, duration: 0.5 }}
        className="font-display text-dim tracking-[0.3em] uppercase mb-12 relative z-10"
        style={{ fontSize: 'clamp(0.7rem, 1.5vw, 0.9rem)' }}
      >
        Race to solve &middot; Code to win
      </motion.p>

      {/* Card */}
      <motion.div
        initial={{ opacity: 0, y: 24 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.15, duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
        className="w-full max-w-[480px] bg-surface/75 border border-brd rounded-2xl p-9 backdrop-blur-2xl shadow-panel relative z-10"
      >
        {/* Player Name */}
        <div className="mb-7">
          <label className="block font-display text-[0.72rem] font-semibold tracking-[0.14em] uppercase text-muted mb-2">
            Your Name
          </label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            maxLength={20}
            placeholder="Enter your name..."
            className="w-full px-4 py-3 bg-panel border border-brd rounded-lg text-light font-body text-[0.95rem] outline-none transition-all duration-150 focus:border-primary focus:shadow-[0_0_0_3px_rgba(0,229,199,0.15)] placeholder:text-dim"
          />
        </div>

        {/* Tabs */}
        <div className="flex border-b border-brd mb-7 relative">
          {['create', 'join'].map((t) => (
            <button
              key={t}
              onClick={() => { setTab(t); setError(''); }}
              className={`flex-1 py-3 bg-transparent border-none font-display text-[0.82rem] font-semibold tracking-[0.1em] uppercase cursor-pointer transition-colors duration-150 ${
                tab === t ? 'text-primary' : 'text-dim hover:text-muted'
              }`}
            >
              {t === 'create' ? 'Create Room' : 'Join Room'}
            </button>
          ))}
          <motion.div
            className="absolute bottom-[-1px] left-0 h-[2px] bg-primary"
            style={{ boxShadow: '0 0 10px rgba(0,229,199,0.25)', width: '50%' }}
            animate={{ x: tab === 'create' ? '0%' : '100%' }}
            transition={{ type: 'spring', stiffness: 500, damping: 30 }}
          />
        </div>

        {/* Create Form */}
        {tab === 'create' && (
          <motion.form
            key="create"
            initial={{ opacity: 0, x: -12 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.25 }}
            onSubmit={handleCreate}
            className="flex flex-col gap-5"
          >
            {/* Difficulty */}
            <div className="flex flex-col gap-1.5">
              <label className="font-display text-[0.72rem] font-medium tracking-[0.12em] uppercase text-muted">
                Difficulty
              </label>
              <div className="flex gap-1.5">
                {DIFFICULTIES.map((d) => (
                  <button
                    key={d.label}
                    type="button"
                    onClick={() => setDifficulty(d.value)}
                    className={`flex-1 py-2.5 px-2 bg-panel border border-brd rounded text-center font-display text-[0.72rem] font-semibold tracking-[0.08em] uppercase cursor-pointer transition-all duration-150 ${
                      difficulty === d.value
                        ? diffActiveClass[d.style]
                        : 'text-muted hover:border-brd-light hover:text-light'
                    }`}
                  >
                    {d.label}
                  </button>
                ))}
              </div>
            </div>

            {/* Time & Rounds row */}
            <div className="flex gap-3.5">
              <div className="flex-1 flex flex-col gap-1.5">
                <label className="font-display text-[0.72rem] font-medium tracking-[0.12em] uppercase text-muted">
                  Time (min)
                </label>
                <input
                  type="number"
                  min={1}
                  step={0.5}
                  value={timeLimit}
                  onChange={(e) => {
                    const v = e.target.value;
                    setTimeLimit(v === '' ? '' : Math.max(1, parseFloat(v) || 1));
                  }}
                  onBlur={() => { if (timeLimit === '' || isNaN(timeLimit)) setTimeLimit(5); }}
                  className="w-full px-4 py-3 bg-panel border border-brd rounded-lg text-light font-mono text-[0.95rem] outline-none transition-all duration-150 focus:border-primary focus:shadow-[0_0_0_3px_rgba(0,229,199,0.15)] placeholder:text-dim"
                />
              </div>
              <div className="flex-1 flex flex-col gap-1.5">
                <label className="font-display text-[0.72rem] font-medium tracking-[0.12em] uppercase text-muted">
                  Rounds
                </label>
                <input
                  type="number"
                  min={1}
                  max={10}
                  value={rounds}
                  onChange={(e) => {
                    const v = e.target.value;
                    setRounds(v === '' ? '' : Math.max(1, Math.min(10, parseInt(v) || 1)));
                  }}
                  onBlur={() => { if (rounds === '' || isNaN(rounds)) setRounds(1); }}
                  className="w-full px-4 py-3 bg-panel border border-brd rounded-lg text-light font-mono text-[0.95rem] outline-none transition-all duration-150 focus:border-primary focus:shadow-[0_0_0_3px_rgba(0,229,199,0.15)] placeholder:text-dim"
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full mt-1.5 inline-flex items-center justify-center gap-2 px-7 py-3.5 bg-primary text-inverse font-display text-[0.9rem] font-semibold tracking-[0.1em] uppercase rounded-lg transition-all duration-150 hover:bg-primary-bright hover:shadow-glow hover:-translate-y-px disabled:opacity-40 disabled:cursor-not-allowed disabled:transform-none"
            >
              {loading ? (
                <>
                  <span className="w-4 h-4 border-2 border-inverse/30 border-t-inverse rounded-full animate-spin" />
                  Creating...
                </>
              ) : (
                'Create Room'
              )}
            </button>
          </motion.form>
        )}

        {/* Join Form */}
        {tab === 'join' && (
          <motion.form
            key="join"
            initial={{ opacity: 0, x: 12 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.25 }}
            onSubmit={handleJoin}
            className="flex flex-col gap-5"
          >
            <div className="flex flex-col gap-1.5">
              <label className="font-display text-[0.72rem] font-medium tracking-[0.12em] uppercase text-muted">
                Room Code
              </label>
              <input
                type="text"
                value={roomCode}
                onChange={(e) => setRoomCode(e.target.value.slice(0, 6))}
                maxLength={6}
                placeholder="XXXXXX"
                className="w-full px-4 py-3.5 bg-panel border border-brd rounded-lg text-light font-mono text-xl tracking-[0.35em] uppercase text-center outline-none transition-all duration-150 focus:border-primary focus:shadow-[0_0_0_3px_rgba(0,229,199,0.15)] placeholder:text-dim"
              />
            </div>

            <button
              type="submit"
              className="w-full mt-1.5 inline-flex items-center justify-center gap-2 px-7 py-3.5 bg-primary text-inverse font-display text-[0.9rem] font-semibold tracking-[0.1em] uppercase rounded-lg transition-all duration-150 hover:bg-primary-bright hover:shadow-glow hover:-translate-y-px disabled:opacity-40 disabled:cursor-not-allowed"
            >
              Join Room
            </button>
          </motion.form>
        )}

        {/* Error */}
        {error && (
          <motion.p
            initial={{ opacity: 0, y: -4 }}
            animate={{ opacity: 1, y: 0 }}
            className="mt-4 text-err text-[0.82rem] text-center"
          >
            {error}
          </motion.p>
        )}
      </motion.div>
    </div>
  );
}
