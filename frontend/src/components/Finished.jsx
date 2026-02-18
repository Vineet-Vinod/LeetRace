import { motion } from 'framer-motion';
import { useGame } from '../context/GameContext';

export default function Finished() {
  const {
    isHost,
    isGameOver,
    isBreak,
    breakTimeLeft,
    currentRound,
    totalRounds,
    finalRankings,
    restart,
    enterReviewMode,
  } = useGame();

  const title = isGameOver
    ? 'Game Over!'
    : `Round ${currentRound}/${totalRounds} Complete`;

  return (
    <div className="relative z-1 flex flex-col items-center justify-center min-h-screen p-8">
      <motion.h1
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="font-display font-black text-2xl tracking-[3px] uppercase text-txt mb-6"
        style={{ textShadow: '0 0 15px rgba(240,160,48,0.25)' }}
      >
        Leet<span className="text-accent">Race</span>
      </motion.h1>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
        className="card-glow bg-surface border border-white/[0.06] rounded-xl p-8 w-full max-w-[520px]"
      >
        <h2 className="font-display text-xl font-bold tracking-[2px] uppercase text-center mb-1 text-txt">
          {title}
        </h2>

        {/* Rankings */}
        <div className="my-6">
          {finalRankings.map((r, i) => {
            const locked = r.locked_at !== null;
            return (
              <motion.div
                key={r.name}
                initial={{ opacity: 0, x: -15 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.1 + i * 0.06, ease: [0.16, 1, 0.3, 1] }}
                className="flex items-center justify-between py-3 px-4 border-b border-white/[0.06] first:border-t transition-colors hover:bg-elevated"
              >
                <div className="flex items-center gap-3">
                  <span
                    className={`font-display font-black w-8 text-right ${
                      i === 0
                        ? 'text-warning text-xl'
                        : i === 1
                          ? 'text-txt-secondary text-lg'
                          : i === 2
                            ? 'text-[#cd7f32] text-lg'
                            : 'text-secondary text-base'
                    }`}
                    style={i === 0 ? { textShadow: '0 0 15px rgba(232,192,64,0.3)' } : undefined}
                  >
                    #{r.position}
                  </span>
                  <span className="font-heading font-semibold text-txt">
                    {r.name}
                  </span>
                </div>

                <div className="flex items-center gap-5 font-mono text-xs text-txt-dim">
                  {r.solved ? (
                    <>
                      <span className="text-success font-bold">
                        Solved{locked ? ' \u{1f512}' : ''}
                      </span>
                      <span>{r.char_count} chars</span>
                      <span>{r.submit_time}s</span>
                    </>
                  ) : (
                    <span className="text-danger">
                      {r.tests_passed}/{r.tests_total} tests
                    </span>
                  )}
                </div>
              </motion.div>
            );
          })}
        </div>

        {/* Break countdown */}
        {isBreak && (
          <p className="font-display text-sm font-bold text-warning text-center tracking-wider animate-pulse-slow mb-4">
            Next round in {breakTimeLeft}s...
          </p>
        )}

        {/* Actions */}
        <div className="flex gap-2 mt-2">
          <button
            onClick={enterReviewMode}
            className="flex-1 py-2.5 bg-transparent border border-white/10 rounded font-heading font-semibold text-xs uppercase tracking-wider text-txt-secondary cursor-pointer transition-all hover:border-accent hover:text-accent"
          >
            View Code
          </button>

          {isGameOver && isHost && (
            <motion.button
              whileHover={{ scale: 1.01 }}
              whileTap={{ scale: 0.97 }}
              onClick={restart}
              className="flex-1 py-2.5 font-heading font-bold text-xs uppercase tracking-wider rounded bg-gradient-to-br from-accent to-accent-dim text-void border border-accent shadow-glow-accent cursor-pointer transition-all duration-200 hover:shadow-glow-accent-lg"
            >
              Play Again
            </motion.button>
          )}

          {isGameOver && !isHost && (
            <p className="flex-1 flex items-center justify-center font-heading text-xs text-txt-dim animate-pulse-slow">
              Waiting for host...
            </p>
          )}
        </div>
      </motion.div>
    </div>
  );
}
