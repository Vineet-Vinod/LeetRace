import { useState, useRef, useCallback, useEffect } from 'react';
import { useGame } from '../context/GameContext';
import ProblemPanel from './ProblemPanel';
import CodeEditor from './CodeEditor';
import OutputPanel from './OutputPanel';
import Scoreboard from './Scoreboard';

export default function Playing() {
  const {
    timeLeft,
    totalRounds,
    currentRound,
    submitCooldown,
    lockedIn,
    hasSolved,
    gameActive,
    reviewMode,
    lastResult,
    scoreboard,
    submitCode,
    lockIn,
    exitReviewMode,
  } = useGame();

  const editorRef = useRef(null);
  const [charCount, setCharCount] = useState(0);

  // Resize state
  const [problemWidth, setProblemWidth] = useState(40);
  const [editorHeightPercent, setEditorHeightPercent] = useState(70);
  const layoutRef = useRef(null);
  const editorPanelRef = useRef(null);
  const dragging = useRef(null);

  const handleSubmit = useCallback(() => {
    const code = editorRef.current?.();
    if (code != null) submitCode(code);
  }, [submitCode]);

  // Ctrl+Enter submit handler
  useEffect(() => {
    function onKeyDown(e) {
      if (e.ctrlKey && e.key === 'Enter') {
        e.preventDefault();
        handleSubmit();
      }
    }
    document.addEventListener('keydown', onKeyDown);
    return () => document.removeEventListener('keydown', onKeyDown);
  }, [handleSubmit]);

  // Timer display
  const minutes = Math.floor(timeLeft / 60);
  const seconds = timeLeft % 60;
  const timerText = `${minutes}:${seconds.toString().padStart(2, '0')}`;
  const timerClass =
    timeLeft <= 30 ? 'text-danger animate-timer-pulse' :
    timeLeft <= 60 ? 'text-warning' :
    'text-success';

  // Resize handlers
  function onMouseDown(type) {
    return (e) => {
      e.preventDefault();
      dragging.current = type;
      document.body.style.cursor = type === 'v' ? 'col-resize' : 'row-resize';
      document.body.style.userSelect = 'none';
    };
  }

  useEffect(() => {
    function onMouseMove(e) {
      if (!dragging.current) return;

      if (dragging.current === 'v' && layoutRef.current) {
        const rect = layoutRef.current.getBoundingClientRect();
        const pct = ((e.clientX - rect.left) / rect.width) * 100;
        setProblemWidth(Math.min(85, Math.max(15, pct)));
      }

      if (dragging.current === 'h' && editorPanelRef.current) {
        const rect = editorPanelRef.current.getBoundingClientRect();
        const pct = ((e.clientY - rect.top) / rect.height) * 100;
        setEditorHeightPercent(Math.min(90, Math.max(20, pct)));
      }
    }

    function onMouseUp() {
      if (dragging.current) {
        dragging.current = null;
        document.body.style.cursor = '';
        document.body.style.userSelect = '';
      }
    }

    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
    return () => {
      document.removeEventListener('mousemove', onMouseMove);
      document.removeEventListener('mouseup', onMouseUp);
    };
  }, []);

  const showOutput = lastResult !== null;

  return (
    <div className="flex flex-col h-screen relative z-1">
      {/* Header */}
      <div className="relative flex items-center justify-between px-6 py-2 bg-surface border-b border-white/[0.06] shrink-0 z-10">
        {/* Logo */}
        <h1
          className="font-display font-black text-lg tracking-[2px] uppercase text-txt"
          style={{ textShadow: '0 0 10px rgba(240,160,48,0.2)' }}
        >
          L<span className="text-accent">R</span>
        </h1>

        {/* Center info */}
        <div className="absolute left-1/2 -translate-x-1/2 flex items-center gap-8">
          {totalRounds > 1 && (
            <span className="font-heading text-xs font-semibold text-secondary uppercase tracking-wider">
              Round {currentRound}/{totalRounds}
            </span>
          )}

          {!reviewMode && (
            <>
              <span className={`font-display text-xl font-bold tracking-[2px] transition-colors ${timerClass}`}>
                {timerText}
              </span>
              <span className="font-mono text-xs text-txt-dim tracking-wider">
                {charCount} chars
              </span>
            </>
          )}
        </div>

        {/* Actions */}
        <div className="flex items-center gap-2">
          {reviewMode ? (
            <button
              onClick={exitReviewMode}
              className="px-5 py-2 bg-transparent border border-white/10 rounded font-heading font-semibold text-xs uppercase tracking-wider text-txt-secondary cursor-pointer transition-all hover:border-accent hover:text-accent"
            >
              Back to Results
            </button>
          ) : (
            <>
              <button
                onClick={handleSubmit}
                disabled={submitCooldown || lockedIn || !gameActive}
                className="px-5 py-2 bg-transparent border border-success rounded font-heading font-bold text-xs uppercase tracking-wider text-success cursor-pointer transition-all hover:bg-success hover:text-void hover:shadow-glow-success disabled:border-txt-dim disabled:text-txt-dim disabled:cursor-not-allowed disabled:hover:bg-transparent disabled:hover:shadow-none"
              >
                Submit
              </button>
              {hasSolved && !lockedIn && (
                <button
                  onClick={lockIn}
                  className="px-5 py-2 bg-transparent border border-warning rounded font-heading font-bold text-xs uppercase tracking-wider text-warning cursor-pointer transition-all hover:bg-warning hover:text-void hover:shadow-glow-warning"
                >
                  Lock In
                </button>
              )}
              {lockedIn && (
                <span className="px-5 py-2 border border-txt-dim rounded font-heading font-bold text-xs uppercase tracking-wider text-txt-dim">
                  Locked In
                </span>
              )}
            </>
          )}
        </div>
      </div>

      {/* Game layout */}
      <div ref={layoutRef} className="flex flex-1 overflow-hidden min-h-0">
        {/* Problem panel */}
        <div style={{ width: `${problemWidth}%` }} className="shrink-0">
          <ProblemPanel />
        </div>

        {/* Vertical resize handle */}
        <div
          onMouseDown={onMouseDown('v')}
          className="w-1 cursor-col-resize bg-white/[0.04] hover:bg-accent/15 transition-colors z-10 shrink-0"
        />

        {/* Editor + Output */}
        <div ref={editorPanelRef} className="flex-1 flex flex-col overflow-hidden min-w-[200px]">
          <div style={{ height: showOutput ? `${editorHeightPercent}%` : '100%' }} className="min-h-[50px] shrink-0 overflow-hidden">
            <CodeEditor
              editorRef={editorRef}
              onCharCount={setCharCount}
              onSubmit={handleSubmit}
            />
          </div>

          {showOutput && (
            <>
              {/* Horizontal resize handle */}
              <div
                onMouseDown={onMouseDown('h')}
                className="h-1 cursor-row-resize bg-white/[0.04] hover:bg-accent/15 transition-colors z-10 shrink-0"
              />
              <div className="flex-1 min-h-[50px] overflow-hidden">
                <OutputPanel />
              </div>
            </>
          )}
        </div>
      </div>

      {/* Live scoreboard */}
      {scoreboard.length > 0 && !reviewMode && <Scoreboard rankings={scoreboard} />}
    </div>
  );
}
