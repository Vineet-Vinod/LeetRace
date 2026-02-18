import { createContext, useContext, useReducer, useCallback, useRef, useEffect } from 'react';

const GameContext = createContext(null);

const initialState = {
  screen: 'lobby',
  roomId: null,
  playerName: null,
  isHost: false,
  players: [],
  difficulty: null,
  timeLimit: 300,
  totalRounds: 1,
  currentRound: 0,
  problem: null,
  starterCode: '',
  userCode: '',
  timeLeft: 0,
  gameActive: false,
  lockedIn: false,
  submitCooldown: false,
  hasSolved: false,
  lastResult: null,
  scoreboard: [],
  finalRankings: [],
  isBreak: false,
  breakTimeLeft: 0,
  isGameOver: false,
  feedback: null,
  connected: false,
  reviewMode: false,
};

function gameReducer(state, action) {
  switch (action.type) {
    case 'ROOM_STATE':
      return {
        ...state,
        screen: 'lobby',
        players: action.data.players,
        isHost: action.data.host === state.playerName,
        difficulty: action.data.difficulty,
        timeLimit: action.data.time_limit,
        totalRounds: action.data.total_rounds,
        currentRound: action.data.current_round,
      };

    case 'GAME_START':
      return {
        ...state,
        screen: 'playing',
        gameActive: true,
        lockedIn: false,
        submitCooldown: false,
        hasSolved: false,
        reviewMode: false,
        problem: action.data.problem,
        starterCode: action.data.problem.starter_code,
        userCode: '',
        timeLeft: action.data.time_limit,
        totalRounds: action.data.total_rounds,
        currentRound: action.data.current_round,
        lastResult: null,
        scoreboard: [],
      };

    case 'TICK':
      return { ...state, timeLeft: action.remaining };

    case 'SUBMIT_RESULT':
      return {
        ...state,
        lastResult: action.data,
        hasSolved: action.data.solved ? true : state.hasSolved,
        feedback: action.data.solved
          ? { text: `Solved! ${action.data.char_count} chars in ${action.data.submit_time}s`, type: 'success' }
          : {
              text: action.data.error
                ? `${action.data.passed}/${action.data.total} tests — ${action.data.error}`
                : `${action.data.passed}/${action.data.total} tests passed`,
              type: 'fail',
            },
      };

    case 'SCOREBOARD':
      return { ...state, scoreboard: action.data.rankings };

    case 'LOCKED':
      return {
        ...state,
        lockedIn: true,
        feedback: { text: 'Locked in! Your solution is final.', type: 'success' },
      };

    case 'ROUND_OVER':
      return {
        ...state,
        screen: 'finished',
        gameActive: false,
        finalRankings: action.data.rankings,
        isBreak: true,
        breakTimeLeft: action.data.break_seconds || 30,
        isGameOver: false,
        currentRound: action.data.current_round,
        totalRounds: action.data.total_rounds,
      };

    case 'BREAK_TICK':
      return { ...state, breakTimeLeft: action.remaining };

    case 'GAME_OVER':
      return {
        ...state,
        screen: 'finished',
        gameActive: false,
        finalRankings: action.data.rankings,
        isBreak: false,
        isGameOver: true,
      };

    case 'SET_SUBMIT_COOLDOWN':
      return { ...state, submitCooldown: action.value };

    case 'SET_FEEDBACK':
      return { ...state, feedback: action.feedback };

    case 'SET_ERROR':
      return { ...state, feedback: { text: action.error, type: 'fail' } };

    case 'SET_CONNECTED':
      return { ...state, connected: action.value };

    case 'ENTER_REVIEW':
      return {
        ...state,
        reviewMode: true,
        screen: 'playing',
        userCode: action.code,
      };

    case 'EXIT_REVIEW':
      return {
        ...state,
        reviewMode: false,
        screen: 'finished',
      };

    case 'DISCONNECTED':
      return {
        ...state,
        connected: false,
        feedback: { text: 'Disconnected from server', type: 'fail' },
      };

    default:
      return state;
  }
}

export function GameProvider({ children, roomId, playerName }) {
  const [state, dispatch] = useReducer(gameReducer, {
    ...initialState,
    roomId,
    playerName,
  });

  const wsRef = useRef(null);
  const timerRef = useRef(null);
  const stateRef = useRef(state);
  const codeRef = useRef('');

  useEffect(() => {
    stateRef.current = state;
  }, [state]);

  useEffect(() => {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const ws = new WebSocket(`${protocol}//${window.location.host}/ws/${roomId}`);
    wsRef.current = ws;

    ws.onopen = () => {
      dispatch({ type: 'SET_CONNECTED', value: true });
      ws.send(JSON.stringify({ type: 'join', name: playerName }));
    };

    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);

      switch (msg.type) {
        case 'room_state':
          dispatch({ type: 'ROOM_STATE', data: msg });
          break;

        case 'game_start':
          codeRef.current = msg.problem.starter_code;
          dispatch({ type: 'GAME_START', data: msg });
          startClientTimer(msg.time_limit);
          break;

        case 'tick':
          syncTimer(msg.remaining);
          break;

        case 'submit_result':
          dispatch({ type: 'SUBMIT_RESULT', data: msg });
          break;

        case 'scoreboard':
          dispatch({ type: 'SCOREBOARD', data: msg });
          break;

        case 'locked':
          dispatch({ type: 'LOCKED' });
          break;

        case 'round_over':
          clearInterval(timerRef.current);
          dispatch({ type: 'ROUND_OVER', data: msg });
          break;

        case 'break_tick':
          dispatch({ type: 'BREAK_TICK', remaining: msg.remaining });
          break;

        case 'game_over':
          clearInterval(timerRef.current);
          dispatch({ type: 'GAME_OVER', data: msg });
          break;

        case 'error':
          dispatch({ type: 'SET_ERROR', error: msg.message });
          break;
      }
    };

    ws.onclose = () => {
      dispatch({ type: 'DISCONNECTED' });
    };

    return () => {
      clearInterval(timerRef.current);
      ws.close();
    };
  }, [roomId, playerName]);

  const remainingRef = useRef(0);

  function startClientTimer(seconds) {
    clearInterval(timerRef.current);
    remainingRef.current = seconds;
    dispatch({ type: 'TICK', remaining: seconds });

    timerRef.current = setInterval(() => {
      remainingRef.current = Math.max(0, remainingRef.current - 1);
      dispatch({ type: 'TICK', remaining: remainingRef.current });
      if (remainingRef.current <= 0) clearInterval(timerRef.current);
    }, 1000);
  }

  function syncTimer(serverRemaining) {
    remainingRef.current = serverRemaining;
  }

  // Track editor content via ref (no re-renders)
  const updateCode = useCallback((code) => {
    codeRef.current = code;
  }, []);

  const startGame = useCallback(() => {
    wsRef.current?.send(JSON.stringify({ type: 'start' }));
  }, []);

  const submitCode = useCallback((code) => {
    const s = stateRef.current;
    if (s.submitCooldown || s.lockedIn || !s.gameActive || s.reviewMode) return;
    if (!code.trim()) {
      dispatch({ type: 'SET_FEEDBACK', feedback: { text: 'Write some code first!', type: 'fail' } });
      return;
    }
    wsRef.current?.send(JSON.stringify({ type: 'submit', code }));
    dispatch({ type: 'SET_SUBMIT_COOLDOWN', value: true });
    setTimeout(() => dispatch({ type: 'SET_SUBMIT_COOLDOWN', value: false }), 1000);
  }, []);

  const lockIn = useCallback(() => {
    const s = stateRef.current;
    if (s.lockedIn || !s.gameActive) return;
    wsRef.current?.send(JSON.stringify({ type: 'lock' }));
  }, []);

  const restart = useCallback(() => {
    wsRef.current?.send(JSON.stringify({ type: 'restart' }));
  }, []);

  const enterReviewMode = useCallback(() => {
    dispatch({ type: 'ENTER_REVIEW', code: codeRef.current });
  }, []);

  const exitReviewMode = useCallback(() => {
    dispatch({ type: 'EXIT_REVIEW' });
  }, []);

  const clearFeedback = useCallback(() => {
    dispatch({ type: 'SET_FEEDBACK', feedback: null });
  }, []);

  return (
    <GameContext.Provider
      value={{
        ...state,
        startGame,
        submitCode,
        lockIn,
        restart,
        enterReviewMode,
        exitReviewMode,
        clearFeedback,
        updateCode,
      }}
    >
      {children}
    </GameContext.Provider>
  );
}

export function useGame() {
  const context = useContext(GameContext);
  if (!context) throw new Error('useGame must be used within GameProvider');
  return context;
}
