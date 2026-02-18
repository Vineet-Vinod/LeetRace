import { useSearchParams, Navigate } from 'react-router-dom';
import { GameProvider, useGame } from '../context/GameContext';
import Lobby from '../components/Lobby';
import Playing from '../components/Playing';
import Finished from '../components/Finished';
import FeedbackToast from '../components/FeedbackToast';

function RoomContent() {
  const { screen } = useGame();

  switch (screen) {
    case 'lobby':
      return <Lobby />;
    case 'playing':
      return <Playing />;
    case 'finished':
      return <Finished />;
    default:
      return <Lobby />;
  }
}

export default function Room() {
  const [params] = useSearchParams();
  const roomId = params.get('id');
  const playerName = params.get('name');

  if (!roomId || !playerName) {
    return <Navigate to="/" replace />;
  }

  return (
    <GameProvider roomId={roomId} playerName={playerName}>
      <RoomContent />
      <FeedbackToast />
    </GameProvider>
  );
}
