import { useState } from 'react';
import { motion } from 'framer-motion';
import { useGame } from '../context/GameContext';

export default function Lobby() {
  const { roomId, players, isHost, difficulty, timeLimit, totalRounds, startGame } = useGame();
  const [copied, setCopied] = useState(false);

  function copyCode() {
    navigator.clipboard.writeText(roomId).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    });
  }

  return (
    <div className="relative z-1 flex flex-col items-center justify-center min-h-screen p-8">
      <motion.h1
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="font-display font-black text-2xl tracking-[3px] uppercase text-txt mb-8"
        style={{ textShadow: '0 0 15px rgba(240,160,48,0.25)' }}
      >
        Leet<span className="text-accent">Race</span>
      </motion.h1>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
        className="card-glow bg-surface border border-white/[0.06] rounded-xl p-8 w-full max-w-[480px] text-center"
      >
        <h2 className="font-heading text-sm font-semibold text-txt-secondary uppercase tracking-[1.5px] mb-2">
          Room Code
        </h2>

        <motion.div
          onClick={copyCode}
          whileHover={{ scale: 1.03 }}
          whileTap={{ scale: 0.97 }}
          className="font-display font-black text-4xl tracking-[8px] text-accent cursor-pointer select-all mb-1 transition-all"
          style={{ textShadow: '0 0 15px rgba(240,160,48,0.25), 0 0 40px rgba(240,160,48,0.08)' }}
          title="Click to copy"
        >
          {roomId}
        </motion.div>

        <p className="text-xs text-txt-dim font-heading mb-6">
          {copied ? (
            <span className="text-success uppercase tracking-wider">Copied!</span>
          ) : (
            'Share this code with friends'
          )}
        </p>

        {/* Player list */}
        <div className="flex flex-wrap gap-2 justify-center mb-6">
          {players.map((p, i) => (
            <motion.span
              key={p}
              initial={{ opacity: 0, scale: 0.8 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: i * 0.05, ease: [0.34, 1.56, 0.64, 1] }}
              className={`px-3.5 py-1.5 rounded font-heading text-sm font-semibold border transition-all ${
                p === players[0]
                  ? 'border-secondary text-secondary shadow-glow-secondary bg-elevated'
                  : 'border-white/[0.06] text-txt bg-elevated'
              }`}
            >
              {p}
              {p === players[0] && (
                <span className="ml-1.5 text-xs opacity-70">(host)</span>
              )}
            </motion.span>
          ))}
        </div>

        {/* Game info */}
        <div className="flex justify-center gap-6 font-mono text-xs text-txt-dim uppercase tracking-wider mb-6">
          <span>
            <span className="text-txt-secondary">{difficulty || 'Any'}</span>
          </span>
          <span>
            <span className="text-txt-secondary">{timeLimit}s</span>
          </span>
          <span>
            <span className="text-txt-secondary">{totalRounds} {totalRounds === 1 ? 'round' : 'rounds'}</span>
          </span>
        </div>

        {/* Actions */}
        {isHost ? (
          <motion.button
            whileHover={{ scale: 1.01 }}
            whileTap={{ scale: 0.97 }}
            onClick={startGame}
            className="w-full py-3 font-heading font-bold text-sm uppercase tracking-wider rounded bg-gradient-to-br from-accent to-accent-dim text-void border border-accent shadow-glow-accent cursor-pointer transition-all duration-200 hover:shadow-glow-accent-lg"
          >
            Start Game
          </motion.button>
        ) : (
          <p className="font-heading text-sm text-txt-dim animate-pulse-slow">
            Waiting for host to start...
          </p>
        )}
      </motion.div>
    </div>
  );
}
