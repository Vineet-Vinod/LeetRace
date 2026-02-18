import { useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useGame } from '../context/GameContext';

export default function FeedbackToast() {
  const { feedback, clearFeedback } = useGame();

  useEffect(() => {
    if (feedback) {
      const timer = setTimeout(clearFeedback, 5000);
      return () => clearTimeout(timer);
    }
  }, [feedback, clearFeedback]);

  return (
    <AnimatePresence>
      {feedback && (
        <motion.div
          initial={{ opacity: 0, y: 20, x: '-50%' }}
          animate={{ opacity: 1, y: 0, x: '-50%' }}
          exit={{ opacity: 0, y: 10, x: '-50%' }}
          transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }}
          className={`fixed bottom-8 left-1/2 px-6 py-2.5 rounded font-heading font-semibold text-sm z-[1000] pointer-events-none tracking-wider ${
            feedback.type === 'success'
              ? 'bg-success text-void shadow-glow-success'
              : 'bg-danger text-white shadow-glow-danger'
          }`}
        >
          {feedback.text}
        </motion.div>
      )}
    </AnimatePresence>
  );
}
