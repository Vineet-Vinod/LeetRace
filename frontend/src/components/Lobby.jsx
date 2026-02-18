import { useState } from 'react';
import { motion } from 'framer-motion';

function formatTime(seconds) {
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return s > 0 ? `${m}m ${s}s` : `${m}m`;
}

function DifficultyBadge({ difficulty }) {
  const map = {
    Easy: 'bg-ok/12 text-ok border border-ok/30',
    Medium: 'bg-warn/12 text-warn border border-warn/30',
    Hard: 'bg-err/12 text-err border border-err/30',
  };
  const cls = map[difficulty] || 'bg-accent/12 text-accent-bright border border-accent/30';
  const label = difficulty || 'Any';
  return (
    <span className={`inline-flex items-center px-3 py-1 rounded-full font-display text-[0.72rem] font-semibold tracking-[0.06em] uppercase ${cls}`}>
      {label}
    </span>
  );
}

export default function Lobby({ roomInfo, playerName, onStart }) {
  const [copied, setCopied] = useState(false);

  if (!roomInfo) return null;

  const isHost = playerName === roomInfo.host;
  const canStart = isHost && roomInfo.players.length >= 1;

  const copyCode = () => {
    navigator.clipboard.writeText(roomInfo.room_id).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    });
  };

  return (
    <div className="flex-1 flex flex-col items-center justify-center px-5 py-10 gap-8">
      {/* Room Code */}
      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
        className="text-center"
      >
        <p className="font-display text-[0.82rem] font-medium tracking-[0.2em] uppercase text-dim mb-3">
          Room Code
        </p>
        <button
          onClick={copyCode}
          className="font-mono font-bold tracking-[0.3em] text-primary uppercase relative py-2 px-6 border border-primary/25 rounded-lg bg-primary/3 transition-all duration-150 hover:bg-primary/6 hover:shadow-glow cursor-pointer animate-glow-pulse"
          style={{ fontSize: 'clamp(2rem, 5vw, 3.2rem)', textShadow: '0 0 30px rgba(0,229,199,0.3)' }}
        >
          {roomInfo.room_id}
          <span className="absolute -bottom-5 left-1/2 -translate-x-1/2 font-body text-[0.68rem] text-dim tracking-[0.06em] whitespace-nowrap normal-case font-normal">
            {copied ? 'Copied!' : 'Click to copy'}
          </span>
        </button>
      </motion.div>

      {/* Room Info */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.15, duration: 0.4 }}
        className="flex gap-6 items-center justify-center flex-wrap"
      >
        <div className="flex items-center gap-2 font-display text-[0.78rem] tracking-[0.06em] uppercase text-muted">
          <span className="text-light font-semibold"><DifficultyBadge difficulty={roomInfo.difficulty} /></span>
        </div>
        <div className="flex items-center gap-2 font-display text-[0.78rem] tracking-[0.06em] uppercase text-muted">
          Time: <span className="text-light font-semibold">{formatTime(roomInfo.time_limit)}</span>
        </div>
        <div className="flex items-center gap-2 font-display text-[0.78rem] tracking-[0.06em] uppercase text-muted">
          Rounds: <span className="text-light font-semibold">{roomInfo.total_rounds}</span>
        </div>
      </motion.div>

      {/* Players */}
      <motion.div
        initial={{ opacity: 0, y: 12 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.25, duration: 0.4 }}
        className="text-center"
      >
        <p className="font-display text-[0.7rem] font-semibold tracking-[0.15em] uppercase text-dim mb-4">
          Players ({roomInfo.players.length})
        </p>
        <div className="flex gap-2.5 flex-wrap justify-center">
          {roomInfo.players.map((p, i) => (
            <motion.div
              key={p}
              initial={{ opacity: 0, x: -16 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.3 + i * 0.08, duration: 0.35 }}
              className={`px-5 py-2.5 border rounded-lg font-display text-[0.88rem] font-medium tracking-[0.04em] ${
                p === roomInfo.host
                  ? 'border-primary/25 text-primary bg-primary/5'
                  : 'border-brd-light text-light bg-elevated'
              } ${p === playerName ? 'ring-1 ring-primary/20' : ''}`}
            >
              {p}
              {p === roomInfo.host && (
                <span className="ml-2 text-[0.65rem] text-primary-dim uppercase tracking-wider">host</span>
              )}
            </motion.div>
          ))}
        </div>
      </motion.div>

      {/* Waiting / Start */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.45, duration: 0.4 }}
        className="flex flex-col items-center gap-3"
      >
        {roomInfo.players.length < 1 && (
          <p className="font-body text-[0.85rem] text-dim italic">
            Waiting for at least 1 player...
          </p>
        )}
        {isHost ? (
          <button
            onClick={onStart}
            disabled={!canStart}
            className="inline-flex items-center justify-center gap-2 px-10 py-3.5 bg-primary text-inverse font-display text-[0.9rem] font-semibold tracking-[0.1em] uppercase rounded-lg transition-all duration-150 hover:bg-primary-bright hover:shadow-glow hover:-translate-y-px disabled:opacity-40 disabled:cursor-not-allowed disabled:transform-none"
          >
            Start Game
          </button>
        ) : (
          <p className="font-body text-[0.85rem] text-muted">
            Waiting for host to start...
          </p>
        )}
      </motion.div>
    </div>
  );
}
