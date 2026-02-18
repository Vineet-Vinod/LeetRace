import { useState, useRef, useEffect, useCallback } from 'react';
import { motion } from 'framer-motion';
import CodeEditor from './CodeEditor';

function formatTimer(seconds) {
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return `${m}:${s.toString().padStart(2, '0')}`;
}

function DifficultyBadge({ difficulty }) {
  const map = {
    Easy: 'bg-ok/12 text-ok border border-ok/30',
    Medium: 'bg-warn/12 text-warn border border-warn/30',
    Hard: 'bg-err/12 text-err border border-err/30',
  };
  return (
    <span className={`inline-flex items-center px-3 py-1 rounded-full font-display text-[0.72rem] font-semibold tracking-[0.06em] uppercase ${map[difficulty] || 'bg-accent/12 text-accent-bright border border-accent/30'}`}>
      {difficulty}
    </span>
  );
}

export default function Playing({
  problem,
  remaining,
  rankings,
  submitResult,
  locked,
  isHost,
  playerName,
  onSubmit,
  onLock,
  code,
  setCode,
  currentRound,
  totalRounds,
  reviewMode,
  onExitReview,
}) {
  const [leftWidth, setLeftWidth] = useState(42);
  const [editorRatio, setEditorRatio] = useState(70);
  const [submitCooldown, setSubmitCooldown] = useState(false);
  const isDragging = useRef(null);
  const containerRef = useRef(null);
  const editorPanelRef = useRef(null);

  // Timer color class
  const timerClass = remaining <= 30
    ? 'text-err animate-pulse-danger'
    : remaining <= 60
    ? 'text-warn'
    : 'text-primary';
  const timerShadow = remaining <= 30
    ? '0 0 12px rgba(239,68,68,0.4)'
    : remaining <= 60
    ? '0 0 10px rgba(234,179,8,0.3)'
    : 'none';

  // Submit handler with cooldown
  const handleSubmit = useCallback(() => {
    if (submitCooldown || locked || reviewMode) return;
    onSubmit(code);
    setSubmitCooldown(true);
    setTimeout(() => setSubmitCooldown(false), 3000);
  }, [code, submitCooldown, locked, reviewMode, onSubmit]);

  // Has solved (for showing lock button)
  const hasSolved = submitResult?.solved === true;

  // Resize handling
  useEffect(() => {
    const handleMouseMove = (e) => {
      if (!isDragging.current) return;
      if (isDragging.current === 'v' && containerRef.current) {
        const rect = containerRef.current.getBoundingClientRect();
        const pct = ((e.clientX - rect.left) / rect.width) * 100;
        setLeftWidth(Math.max(15, Math.min(85, pct)));
      } else if (isDragging.current === 'h' && editorPanelRef.current) {
        const rect = editorPanelRef.current.getBoundingClientRect();
        const pct = ((e.clientY - rect.top) / rect.height) * 100;
        setEditorRatio(Math.max(20, Math.min(90, pct)));
      }
    };
    const handleMouseUp = () => {
      if (isDragging.current) {
        document.body.classList.remove('resizing', 'resizing-h');
        isDragging.current = null;
      }
    };
    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', handleMouseUp);
    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
    };
  }, []);

  const startDragV = () => {
    isDragging.current = 'v';
    document.body.classList.add('resizing');
  };
  const startDragH = () => {
    isDragging.current = 'h';
    document.body.classList.add('resizing-h');
  };

  // Build output content
  const renderOutput = () => {
    if (!submitResult) {
      return <span className="text-dim italic">Submit your code to see results...</span>;
    }
    const { passed, total, error, solved, char_count, submit_time, stdout, stderr } = submitResult;

    return (
      <div className="flex flex-col gap-1">
        {solved ? (
          <div className="text-ok font-bold text-[0.88rem]">
            Solved! {char_count} chars in {submit_time.toFixed(1)}s
          </div>
        ) : error ? (
          <>
            <div className="text-warn font-semibold">
              {passed}/{total} tests passed
            </div>
            <div className="text-err text-[0.8rem] whitespace-pre-wrap">{error}</div>
          </>
        ) : (
          <div className="text-warn font-semibold">
            {passed}/{total} tests passed
          </div>
        )}
        {stdout && (
          <div className="mt-2.5 pt-2.5 border-t border-brd text-dim whitespace-pre-wrap break-all text-[0.78rem]">
            <span className="text-muted font-semibold text-[0.7rem] uppercase tracking-wider">stdout:</span>
            <br />{stdout}
          </div>
        )}
        {stderr && (
          <div className="mt-1.5 text-err/70 whitespace-pre-wrap break-all text-[0.78rem]">
            <span className="text-err font-semibold text-[0.7rem] uppercase tracking-wider">stderr:</span>
            <br />{stderr}
          </div>
        )}
      </div>
    );
  };

  return (
    <div className="flex flex-col h-screen overflow-hidden">
      {/* Review banner */}
      {reviewMode && (
        <div className="flex items-center justify-center gap-3 px-4 py-2 bg-elevated border-b border-brd">
          <span className="font-display text-[0.75rem] font-semibold tracking-[0.1em] uppercase text-muted">
            Review Mode
          </span>
          <button
            onClick={onExitReview}
            className="px-4 py-1.5 bg-transparent text-primary border border-primary/25 rounded font-display text-[0.72rem] font-semibold tracking-[0.08em] uppercase cursor-pointer transition-all duration-150 hover:bg-primary/8 hover:border-primary"
          >
            Back to Results
          </button>
        </div>
      )}

      {/* Header */}
      <div className="flex items-center justify-between px-5 h-14 min-h-14 bg-surface border-b border-brd gap-4 z-10">
        {/* Left: Logo + Round */}
        <div className="flex items-center gap-4">
          <span className="font-display text-[0.9rem] font-bold tracking-[0.15em] uppercase text-muted">
            Leet<span className="text-primary">Race</span>
          </span>
          {totalRounds > 1 && (
            <span className="font-mono text-[0.72rem] font-semibold text-muted bg-elevated px-2.5 py-1 rounded border border-brd">
              Round {currentRound}/{totalRounds}
            </span>
          )}
        </div>

        {/* Center: Timer + Char count */}
        {!reviewMode && (
          <div className="flex items-center gap-6">
            <div
              className={`font-mono text-[1.35rem] font-bold tracking-[0.08em] min-w-[90px] text-center ${timerClass}`}
              style={{ textShadow: timerShadow }}
            >
              {formatTimer(remaining)}
            </div>
            <div className="font-mono text-[0.82rem] text-muted flex items-center gap-1.5">
              Chars: <span className="text-light font-semibold">{code.length}</span>
            </div>
          </div>
        )}

        {/* Right: Buttons */}
        {!reviewMode && (
          <div className="flex items-center gap-2.5">
            {locked ? (
              <span className="font-display text-[0.78rem] font-semibold tracking-[0.1em] uppercase text-warn bg-warn/12 border border-warn/30 px-3.5 py-1.5 rounded">
                Locked In
              </span>
            ) : (
              <>
                <button
                  onClick={handleSubmit}
                  disabled={submitCooldown}
                  className="inline-flex items-center justify-center gap-2 px-5 py-2 bg-ok text-inverse font-display text-[0.8rem] font-semibold tracking-[0.08em] uppercase rounded transition-all duration-150 hover:bg-[#2ad86c] hover:shadow-glow-ok hover:-translate-y-px disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
                >
                  {submitCooldown ? 'Wait...' : 'Submit'}
                </button>
                {hasSolved && (
                  <motion.button
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                    onClick={onLock}
                    className="inline-flex items-center justify-center gap-2 px-5 py-2 bg-warn text-inverse font-display text-[0.8rem] font-semibold tracking-[0.08em] uppercase rounded transition-all duration-150 hover:bg-[#fbbf24] hover:shadow-glow-warn hover:-translate-y-px"
                  >
                    Lock In
                  </motion.button>
                )}
              </>
            )}
          </div>
        )}
      </div>

      {/* Game Body */}
      <div ref={containerRef} className="flex-1 flex overflow-hidden relative">
        {/* Problem Panel */}
        <div
          className="flex flex-col overflow-hidden bg-base border-r border-brd"
          style={{ width: `${leftWidth}%` }}
        >
          {/* Problem Header */}
          <div className="px-5 pt-4 pb-3 border-b border-brd flex items-start gap-3 flex-wrap">
            <h2 className="font-display text-[1.1rem] font-bold text-light tracking-[0.02em]">
              {problem?.title}
            </h2>
            {problem?.difficulty && <DifficultyBadge difficulty={problem.difficulty} />}
          </div>
          {/* Problem Description */}
          <div className="flex-1 overflow-y-auto px-5 py-5 font-body text-[0.88rem] leading-[1.7] text-muted">
            <pre className="whitespace-pre-wrap break-words font-[inherit] m-0">
              {problem?.description}
            </pre>
          </div>
        </div>

        {/* Vertical resize handle */}
        <div
          className={`resize-handle-v ${isDragging.current === 'v' ? 'active' : ''}`}
          onMouseDown={startDragV}
        />

        {/* Editor Panel */}
        <div
          ref={editorPanelRef}
          className="flex flex-col overflow-hidden flex-1"
        >
          {/* Code Editor */}
          <div className="overflow-hidden" style={{ height: `${editorRatio}%` }}>
            <CodeEditor
              value={code}
              onChange={reviewMode ? undefined : setCode}
              readOnly={reviewMode || locked}
              onSubmit={handleSubmit}
            />
          </div>

          {/* Horizontal resize handle */}
          <div
            className={`resize-handle-h ${isDragging.current === 'h' ? 'active' : ''}`}
            onMouseDown={startDragH}
          />

          {/* Output Panel */}
          <div className="flex flex-col overflow-hidden bg-surface flex-1">
            <div className="px-4 py-2 font-display text-[0.68rem] font-semibold tracking-[0.12em] uppercase text-dim border-b border-brd bg-elevated">
              Output
            </div>
            <div className="flex-1 overflow-y-auto px-4 py-3 font-mono text-[0.82rem] leading-[1.6] text-muted">
              {renderOutput()}
            </div>
          </div>
        </div>
      </div>

      {/* Live Scoreboard */}
      {!reviewMode && rankings.length > 0 && (
        <div className="flex items-center gap-2 px-4 py-2 bg-surface border-t border-brd overflow-x-auto min-h-[48px] z-10">
          {rankings.map((r) => {
            const posClass = r.position === 1 ? 'text-gold' : r.position === 2 ? 'text-silver' : r.position === 3 ? 'text-bronze' : 'text-dim';
            const isYou = r.name === playerName;
            const cardBorder = r.locked_at
              ? 'border-warn/30'
              : r.solved
              ? 'border-ok/30'
              : isYou
              ? 'border-primary/20'
              : 'border-brd';
            const cardBg = isYou ? 'bg-primary/4' : 'bg-elevated';

            return (
              <div
                key={r.name}
                className={`flex items-center gap-2 px-3.5 py-1.5 ${cardBg} border ${cardBorder} rounded whitespace-nowrap shrink-0 transition-all duration-150`}
              >
                <span className={`font-mono text-[0.7rem] font-bold min-w-[18px] text-center ${posClass}`}>
                  #{r.position}
                </span>
                <span className={`font-display text-[0.78rem] font-semibold tracking-[0.02em] ${isYou ? 'text-primary' : 'text-light'}`}>
                  {r.name}
                </span>
                <span className={`font-mono text-[0.7rem] ${r.solved ? 'text-ok' : 'text-muted'}`}>
                  {r.solved
                    ? `${r.char_count}ch${r.locked_at ? ' \u{1f512}' : ''}`
                    : `${r.tests_passed}/${r.tests_total}`
                  }
                </span>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
