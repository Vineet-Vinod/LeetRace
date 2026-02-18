import { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

const MAX_MESSAGES = 200;

export default function Chat({ messages, onSend, playerName }) {
  const [collapsed, setCollapsed] = useState(false);
  const [text, setText] = useState('');
  const [cooldown, setCooldown] = useState(false);
  const [hasUnread, setHasUnread] = useState(false);
  const messagesEndRef = useRef(null);

  // Auto-scroll to bottom on new messages (only when expanded)
  useEffect(() => {
    if (!collapsed) {
      messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
      setHasUnread(false);
    } else if (messages.length > 0) {
      setHasUnread(true);
    }
  }, [messages, collapsed]);

  // Clear unread on expand
  useEffect(() => {
    if (!collapsed) setHasUnread(false);
  }, [collapsed]);

  function handleSend() {
    const trimmed = text.trim();
    if (!trimmed || cooldown) return;

    onSend(trimmed);
    setText('');
    setCooldown(true);
    setTimeout(() => setCooldown(false), 500);
  }

  function handleKeyDown(e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      handleSend();
    }
  }

  // Only render the last MAX_MESSAGES
  const visibleMessages = messages.length > MAX_MESSAGES
    ? messages.slice(-MAX_MESSAGES)
    : messages;

  return (
    <div className="fixed bottom-0 right-5 w-[280px] z-[200] flex flex-col max-sm:right-2 max-sm:w-[calc(100vw-1rem)]">
      {/* Header */}
      <button
        onClick={() => setCollapsed(c => !c)}
        className="flex items-center justify-between px-3.5 py-2 bg-surface border border-b-0 border-brd rounded-t-lg cursor-pointer transition-colors duration-150 hover:bg-elevated"
        aria-label="Toggle chat"
      >
        <span className="font-display text-[0.7rem] font-semibold tracking-[0.12em] uppercase text-dim">
          Chat
          {hasUnread && (
            <span className="ml-1.5 inline-block w-1.5 h-1.5 rounded-full bg-primary animate-pulse" />
          )}
        </span>
        <span className="text-dim text-[0.72rem] transition-transform duration-200" style={{ transform: collapsed ? 'rotate(180deg)' : 'rotate(0)' }}>
          &#x25BC;
        </span>
      </button>

      {/* Body */}
      {!collapsed && (
        <div className="bg-base/95 border border-t-0 border-brd backdrop-blur-sm flex flex-col">
          {/* Messages */}
          <div
            className="h-[200px] overflow-y-auto px-3 py-2.5 flex flex-col gap-1.5"
            role="log"
            aria-live="polite"
          >
            {visibleMessages.length === 0 && (
              <p className="text-dim text-[0.72rem] font-body italic text-center mt-auto mb-auto">
                No messages yet
              </p>
            )}
            <AnimatePresence initial={false}>
              {visibleMessages.map((msg, i) => {
                const isSelf = msg.sender === playerName;
                return (
                  <motion.div
                    key={msg.id ?? i}
                    initial={{ opacity: 0, y: 6 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.15 }}
                    className={`flex flex-col ${isSelf ? 'items-end' : 'items-start'}`}
                  >
                    <span className={`font-display text-[0.6rem] tracking-[0.08em] uppercase mb-0.5 ${isSelf ? 'text-primary-dim' : 'text-dim'}`}>
                      {msg.sender}
                    </span>
                    <span className={`inline-block px-2.5 py-1.5 rounded-lg font-body text-[0.78rem] leading-snug max-w-[220px] break-words ${
                      isSelf
                        ? 'bg-primary/10 text-primary-bright border border-primary/15'
                        : 'bg-elevated text-light border border-brd'
                    }`}>
                      {msg.message}
                    </span>
                  </motion.div>
                );
              })}
            </AnimatePresence>
            <div ref={messagesEndRef} />
          </div>

          {/* Input */}
          <div className="flex gap-1.5 px-2.5 py-2 border-t border-brd">
            <input
              type="text"
              value={text}
              onChange={e => setText(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Say something..."
              maxLength={200}
              autoComplete="off"
              aria-label="Chat message"
              className="flex-1 min-w-0 bg-elevated border border-brd rounded px-2.5 py-1.5 font-body text-[0.78rem] text-light placeholder:text-dim outline-none focus:border-primary/40 transition-colors duration-150"
            />
            <button
              onClick={handleSend}
              disabled={cooldown || !text.trim()}
              className="px-3 py-1.5 bg-primary/10 text-primary font-display text-[0.68rem] font-semibold tracking-[0.08em] uppercase border border-primary/20 rounded transition-all duration-150 hover:bg-primary/20 disabled:opacity-30 disabled:cursor-not-allowed"
            >
              Send
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
