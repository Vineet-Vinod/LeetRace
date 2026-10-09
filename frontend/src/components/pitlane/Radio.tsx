import { useEffect, useRef, useState, type FormEvent } from "react";
import type { RoomSnapshot } from "../../api";
import type { PaneLayout } from "../../hooks/usePaneLayout";
import { driverCode, livery } from "./livery";

export const RAIL_WIDTH = 44;

function Bars({ live }: { live: boolean }) {
  return (
    <span className="flex items-center gap-[2px] h-4" aria-hidden>
      {[0, 1, 2, 3].map((bar) => (
        <span
          key={bar}
          className={`w-[3px] h-full origin-bottom ${live ? "bg-signal animate-radio" : "bg-ink-dim"}`}
          style={{
            animationDelay: `${bar * 0.15}s`,
            transform: live ? undefined : `scaleY(${0.35 + bar * 0.2})`,
          }}
        />
      ))}
    </span>
  );
}

/** Team radio: collapsed rail on the right edge, expands into the chat pane. */
export default function Radio({
  room,
  layout,
  onSend,
}: {
  room: RoomSnapshot;
  layout: PaneLayout;
  onSend: (message: string) => Promise<boolean>;
}) {
  const [text, setText] = useState("");
  const [sending, setSending] = useState(false);
  const log = useRef<HTMLDivElement>(null);
  const { chatOpen, chatWidth, wide, dragging } = layout;

  useEffect(() => {
    if (chatOpen) log.current?.scrollTo({ top: log.current.scrollHeight });
  }, [room.messages.length, chatOpen]);

  async function send(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const message = text.trim();
    if (!message || sending) return;
    setSending(true);
    if (await onSend(message)) setText("");
    setSending(false);
  }

  const width = chatOpen ? (wide ? chatWidth : Math.min(360, window.innerWidth)) : RAIL_WIDTH;

  return (
    <aside
      aria-label="Team radio"
      className={`shrink-0 overflow-hidden bg-panel border-l border-line ${
        wide
          ? "relative"
          : chatOpen
            ? "fixed inset-y-0 right-0 z-40 shadow-2xl"
            : "fixed bottom-4 right-4 z-40 border"
      }`}
      style={{
        width,
        height: wide || chatOpen ? undefined : RAIL_WIDTH * 2,
        transition: dragging ? "none" : "width 240ms cubic-bezier(0.16, 1, 0.3, 1)",
      }}
    >
      {!chatOpen && (
        <button
          onClick={() => layout.toggleChat(true)}
          aria-label={`Open team radio${layout.unread ? `, ${layout.unread} unread` : ""}`}
          aria-expanded={false}
          className="absolute inset-0 flex flex-col items-center gap-4 pt-4 text-ink-muted hover:text-ink hover:bg-raised transition-colors"
        >
          <Bars live={layout.unread > 0} />
          {layout.unread > 0 && (
            <span className="min-w-5 h-5 px-1 grid place-items-center bg-signal text-white font-mono text-[11px] font-semibold">
              {layout.unread > 99 ? "99+" : layout.unread}
            </span>
          )}
          {wide && (
            <>
              <span className="font-display text-xs font-semibold uppercase tracking-[0.3em] italic [writing-mode:vertical-rl] rotate-180">
                Team radio
              </span>
              <span className="mt-auto mb-4 flex flex-col items-center gap-1">
                <span className="kbd">Ctrl</span>
                <span className="kbd">D</span>
              </span>
            </>
          )}
        </button>
      )}
      {chatOpen && (
        <div className="h-full flex flex-col" style={{ width }}>
          <header className="flex items-center gap-3 h-11 px-4 border-b border-line">
            <Bars live />
            <span className="font-display text-sm font-semibold uppercase italic tracking-[0.2em]">
              Team radio
            </span>
            <span className="ml-auto flex items-center gap-1 text-ink-dim">
              <span className="kbd">Ctrl</span>
              <span className="kbd">D</span>
            </span>
            <button
              onClick={() => layout.toggleChat(false)}
              aria-label="Close team radio"
              className="size-7 grid place-items-center text-ink-muted hover:text-ink hover:bg-raised"
            >
              ✕
            </button>
          </header>
          <div
            ref={log}
            role="log"
            aria-live="polite"
            className="flex-1 overflow-y-auto px-4 py-3 flex flex-col gap-3"
          >
            {room.messages.length === 0 && (
              <p className="m-auto text-center text-ink-dim text-sm">
                Radio is quiet.
                <br />
                Say something to the grid.
              </p>
            )}
            {room.messages.map((message) => {
              const mine = message.sender === room.me.name;
              return (
                <div
                  key={message.id}
                  className={`flex flex-col gap-1 max-w-[88%] ${mine ? "self-end items-end" : "items-start"}`}
                >
                  <span className="flex items-center gap-1.5 label">
                    <span
                      className="w-[3px] h-3"
                      style={{ background: livery(message.sender) }}
                    />
                    {mine ? "You" : driverCode(message.sender)}
                  </span>
                  <p
                    className={`px-3 py-2 text-sm leading-snug break-words ${mine ? "bg-signal/15 border-r-2 border-signal" : "bg-raised border-l-2"}`}
                    style={mine ? undefined : { borderColor: livery(message.sender) }}
                  >
                    {message.message}
                  </p>
                </div>
              );
            })}
          </div>
          <form onSubmit={(event) => void send(event)} className="flex gap-2 p-3 border-t border-line">
            <input
              ref={layout.chatInputRef}
              aria-label="Radio message"
              value={text}
              onChange={(event) => setText(event.target.value)}
              maxLength={200}
              placeholder="Box, box…"
              className="field h-10 flex-1 min-w-0 text-sm"
            />
            <button
              disabled={sending || !text.trim()}
              className="btn btn-go h-10 px-4 text-xs"
            >
              Send
            </button>
          </form>
        </div>
      )}
    </aside>
  );
}
