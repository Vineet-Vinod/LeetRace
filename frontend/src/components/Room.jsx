import { useReducer, useState, useRef, useEffect, useCallback } from 'react';
import { useSearchParams, Navigate } from 'react-router-dom';
import { AnimatePresence, motion } from 'framer-motion';
import useWebSocket from '../hooks/useWebSocket';
import Lobby from './Lobby';
import Playing from './Playing';
import Finished from './Finished';

const initialState = {
  roomState: null,
  roomInfo: null,
  problem: null,
  rankings: [],
  submitResult: null,
  locked: false,
  currentRound: 0,
  totalRounds: 1,
  breakRemaining: 0,
  roundOver: false,
  finalRankings: null,
};

function gameReducer(state, action) {
  switch (action.type) {
    case 'ROOM_STATE':
      return {
        ...state,
        roomInfo: action.payload,
        roomState: action.payload.state,
        currentRound: action.payload.current_round || state.currentRound,
        totalRounds: action.payload.total_rounds || state.totalRounds,
      };

    case 'GAME_START':
      return {
        ...state,
        problem: action.payload.problem,
        roomState: 'playing',
        locked: false,
        submitResult: null,
        rankings: [],
        roundOver: false,
        currentRound: action.payload.current_round,
        totalRounds: action.payload.total_rounds,
        breakRemaining: 0,
      };

    case 'SUBMIT_RESULT':
      return { ...state, submitResult: action.payload };

    case 'SCOREBOARD':
      return { ...state, rankings: action.payload.rankings };

    case 'LOCKED':
      return { ...state, locked: true };

    case 'ROUND_OVER':
      return {
        ...state,
        roomState: 'finished',
        roundOver: true,
        finalRankings: action.payload.rankings,
        breakRemaining: action.payload.break_seconds,
        currentRound: action.payload.current_round,
        totalRounds: action.payload.total_rounds,
      };

    case 'BREAK_TICK':
      return { ...state, breakRemaining: action.payload.remaining };

    case 'GAME_OVER':
      return {
        ...state,
        roomState: 'finished',
        roundOver: false,
        finalRankings: action.payload.rankings,
        breakRemaining: 0,
      };

    default:
      return state;
  }
}

export default function Room() {
  const [searchParams] = useSearchParams();
  const roomId = searchParams.get('id');
  const playerName = searchParams.get('name');

  const [state, dispatch] = useReducer(gameReducer, initialState);
  const [code, setCode] = useState('');
  const [remaining, setRemaining] = useState(0);
  const remainingRef = useRef(0);
  const [reviewMode, setReviewMode] = useState(false);
  const [error, setError] = useState(null);
  const joinedRef = useRef(false);

  // Message handler
  const handleMessage = useCallback((msg) => {
    switch (msg.type) {
      case 'room_state':
        dispatch({ type: 'ROOM_STATE', payload: msg });
        break;

      case 'game_start':
        dispatch({ type: 'GAME_START', payload: msg });
        setCode(msg.problem.starter_code);
        remainingRef.current = msg.time_limit;
        setRemaining(msg.time_limit);
        setReviewMode(false);
        break;

      case 'tick':
        remainingRef.current = msg.remaining;
        setRemaining(msg.remaining);
        break;

      case 'submit_result':
        dispatch({ type: 'SUBMIT_RESULT', payload: msg });
        break;

      case 'scoreboard':
        dispatch({ type: 'SCOREBOARD', payload: msg });
        break;

      case 'locked':
        dispatch({ type: 'LOCKED' });
        break;

      case 'round_over':
        dispatch({ type: 'ROUND_OVER', payload: msg });
        break;

      case 'break_tick':
        dispatch({ type: 'BREAK_TICK', payload: msg });
        break;

      case 'game_over':
        dispatch({ type: 'GAME_OVER', payload: msg });
        break;

      case 'error':
        if (msg.message === 'Room not found') {
          // Room doesn't exist, redirect to home
          window.location.href = '/';
        } else {
          setError(msg.message);
          setTimeout(() => setError(null), 5000);
        }
        break;

      default:
        break;
    }
  }, []);

  const { send, connected } = useWebSocket(roomId, handleMessage);

  // Send join message when connected
  useEffect(() => {
    if (connected && playerName && !joinedRef.current) {
      send({ type: 'join', name: playerName });
      joinedRef.current = true;
    }
  }, [connected, playerName, send]);

  // Reset joined ref if disconnected
  useEffect(() => {
    if (!connected) joinedRef.current = false;
  }, [connected]);

  // Client-side timer countdown
  useEffect(() => {
    if (state.roomState !== 'playing') return;
    const interval = setInterval(() => {
      remainingRef.current = Math.max(0, remainingRef.current - 1);
      setRemaining(remainingRef.current);
    }, 1000);
    return () => clearInterval(interval);
  }, [state.roomState]);

  // Redirect if missing params
  if (!roomId || !playerName) return <Navigate to="/" replace />;

  const isHost = playerName === state.roomInfo?.host;

  // Error toast
  const errorToast = error && (
    <motion.div
      initial={{ opacity: 0, y: -10, x: 10 }}
      animate={{ opacity: 1, y: 0, x: 0 }}
      exit={{ opacity: 0, y: -10 }}
      className="fixed top-5 right-5 z-[9999] bg-err/12 border border-err/30 text-err px-5 py-3.5 rounded-lg font-body text-[0.88rem] backdrop-blur-xl max-w-[400px]"
      style={{ boxShadow: '0 4px 20px rgba(239,68,68,0.15)' }}
    >
      {error}
    </motion.div>
  );

  // Review mode: show Playing in read-only
  if (reviewMode && state.problem) {
    return (
      <div className="min-h-screen flex flex-col">
        <AnimatePresence>{errorToast}</AnimatePresence>
        <Playing
          problem={state.problem}
          remaining={0}
          rankings={[]}
          submitResult={state.submitResult}
          locked={false}
          isHost={isHost}
          playerName={playerName}
          onSubmit={() => {}}
          onLock={() => {}}
          code={code}
          setCode={() => {}}
          currentRound={state.currentRound}
          totalRounds={state.totalRounds}
          reviewMode={true}
          onExitReview={() => setReviewMode(false)}
        />
      </div>
    );
  }

  // Connecting state
  if (!state.roomState) {
    return (
      <div className="min-h-screen flex flex-col items-center justify-center gap-4">
        <AnimatePresence>{errorToast}</AnimatePresence>
        <div className="w-8 h-8 border-[3px] border-brd border-t-primary rounded-full animate-spin" />
        <p className="font-display text-[0.82rem] tracking-[0.1em] text-dim uppercase">
          {connected ? 'Joining room...' : 'Connecting...'}
        </p>
      </div>
    );
  }

  return (
    <div className="min-h-screen flex flex-col">
      <AnimatePresence>{errorToast}</AnimatePresence>

      {state.roomState === 'lobby' && (
        <Lobby
          roomInfo={state.roomInfo}
          playerName={playerName}
          onStart={() => send({ type: 'start' })}
        />
      )}

      {state.roomState === 'playing' && (
        <Playing
          problem={state.problem}
          remaining={remaining}
          rankings={state.rankings}
          submitResult={state.submitResult}
          locked={state.locked}
          isHost={isHost}
          playerName={playerName}
          onSubmit={(c) => send({ type: 'submit', code: c })}
          onLock={() => send({ type: 'lock' })}
          code={code}
          setCode={setCode}
          currentRound={state.currentRound}
          totalRounds={state.totalRounds}
          reviewMode={false}
          onExitReview={() => {}}
        />
      )}

      {state.roomState === 'finished' && (
        <Finished
          rankings={state.finalRankings}
          isHost={isHost}
          playerName={playerName}
          onRestart={() => send({ type: 'restart' })}
          onViewCode={() => setReviewMode(true)}
          breakRemaining={state.breakRemaining}
          currentRound={state.currentRound}
          totalRounds={state.totalRounds}
          roundOver={state.roundOver}
        />
      )}
    </div>
  );
}
