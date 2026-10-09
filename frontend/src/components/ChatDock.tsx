import { useEffect, useRef, useState, type FormEvent } from "react";
import type { RoomSnapshot } from "../api";
import type { PaneLayout } from "../hooks/usePaneLayout";
import { Box } from "./crt";

const MAX_MESSAGE = 200;

function ChatPanel({
  room,
  layout,
  onSend,
}: {
  room: RoomSnapshot;
  layout: PaneLayout;
  onSend: (message: string) => Promise<boolean>;
}) {
  const [text, setText] = useState("");
  const sending = useRef(false);
  const log = useRef<HTMLDivElement>(null);
  const count = room.messages.length;
  const open = layout.chatOpen;

  useEffect(() => {
    if (open && log.current) log.current.scrollTop = log.current.scrollHeight;
  }, [count, open]);

  async function send(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const message = text.trim();
    if (!message || sending.current) return;
    sending.current = true;
    if (await onSend(message)) setText("");
    sending.current = false;
  }

  return (
    <Box
      title={
        <>
          <span>[ #chat ]</span>
          <span className="font-normal text-ink-faint">{count} msg</span>
        </>
      }
      right={
        <button
          className="btn px-1 py-0 text-[0.625rem]"
          onClick={() => layout.toggleChat(false)}
          aria-label="Close chat"
          title="Close chat (Esc)"
        >
          Esc
        </button>
      }
      className="h-full"
    >
      <div
        ref={log}
        role="log"
        aria-live="polite"
        aria-label="Chat messages"
        className="flex min-h-0 flex-1 flex-col gap-1 overflow-y-auto px-3 pt-4 pb-2 text-[0.8125rem] leading-snug"
      >
        {count === 0 && (
          <p className="text-xs text-ink-faint">
            -- channel open, no traffic yet --
            <br />
            say hi to your rivals
            <span className="cursor-block" />
          </p>
        )}
        {room.messages.map((message) => {
          const mine = message.sender === room.me.name;
          return (
            <p
              key={message.id}
              className={`break-words px-1.5 py-0.5 ${mine ? "border-l-2 border-amber bg-amber/[0.07]" : "border-l-2 border-transparent"}`}
            >
              <span className={mine ? "text-amber-hi" : "text-ink-dim"}>
                &lt;{message.sender}&gt;
              </span>{" "}
              <span className={mine ? "text-amber-hi/90" : "text-ink"}>
                {message.message}
              </span>
            </p>
          );
        })}
      </div>
      <form
        onSubmit={(event) => void send(event)}
        className="flex flex-none items-center gap-2 border-t border-line px-3 pt-2"
      >
        <span aria-hidden="true" className="text-amber glow">
          &gt;
        </span>
        <input
          ref={layout.chatInputRef}
          aria-label="Chat message"
          className="field flex-1 text-[0.8125rem]"
          value={text}
          onChange={(event) => setText(event.target.value)}
          maxLength={MAX_MESSAGE}
          placeholder="message"
          autoComplete="off"
          spellCheck={false}
        />
      </form>
      <p className="flex flex-none justify-between px-3 pt-1 pb-2 text-[0.625rem] text-ink-faint">
        <span>⏎ send · Esc close · ^D toggle</span>
        <span
          className={`tabular-nums ${text.length >= MAX_MESSAGE ? "text-alarm" : ""}`}
        >
          {text.length}/{MAX_MESSAGE}
        </span>
      </p>
    </Box>
  );
}

function ChatRail({ layout, floating }: { layout: PaneLayout; floating: boolean }) {
  const unread = layout.unread;
  return (
    <button
      onClick={() => layout.toggleChat(true)}
      aria-label={`Open chat${unread ? ` (${unread} unread)` : ""}`}
      aria-expanded={false}
      aria-keyshortcuts="Control+D"
      title="Open chat (Ctrl+D)"
      className={
        floating
          ? "fixed right-3 bottom-9 z-40 flex items-center gap-2 border border-amber-lo bg-crt-1 px-3 py-1.5 text-xs tracking-[0.12em] text-amber uppercase shadow-[0_0_18px_rgb(0_0_0/0.6)] hover:bg-amber hover:text-crt-0"
          : "group ml-2 flex w-8 flex-none flex-col items-center gap-3 border border-line-hi bg-crt-1 py-3 text-amber hover:border-amber hover:bg-amber hover:text-crt-0"
      }
    >
      {floating ? (
        <>
          <span>[ chat ]</span>
          <span className="kbd">^D</span>
        </>
      ) : (
        <>
          <span className="kbd">^D</span>
          <span className="text-[0.6875rem] font-semibold tracking-[0.3em] uppercase [writing-mode:vertical-rl]">
            chat
          </span>
        </>
      )}
      {unread > 0 && (
        <span className="min-w-[1.4em] bg-amber px-1 text-center text-[0.625rem] font-bold text-crt-0 tabular-nums group-hover:bg-crt-0 group-hover:text-amber">
          {unread > 99 ? "99+" : unread}
        </span>
      )}
    </button>
  );
}

/** Right-side chat: an inline flex column on wide screens, a drawer otherwise. */
export function ChatDock({
  room,
  layout,
  onSend,
  resizable,
}: {
  room: RoomSnapshot;
  layout: PaneLayout;
  onSend: (message: string) => Promise<boolean>;
  resizable: boolean;
}) {
  const aside = useRef<HTMLElement>(null);
  const open = layout.chatOpen;
  useEffect(() => {
    if (aside.current) aside.current.inert = !open;
  }, [open]);

  if (!layout.wide)
    return (
      <>
        {!open && <ChatRail layout={layout} floating />}
        {open && (
          <div
            aria-hidden="true"
            className="fixed inset-0 z-30 bg-crt-0/60"
            onClick={() => layout.toggleChat(false)}
          />
        )}
        <aside
          ref={aside}
          aria-label="Room chat"
          className={`fixed top-0 right-0 bottom-6 z-40 bg-crt-0 px-3 pt-4 pb-3 shadow-[-12px_0_40px_rgb(0_0_0/0.7)] transition-transform duration-200 ${open ? "translate-x-0" : "pointer-events-none translate-x-full"}`}
          style={{ width: `min(${layout.chatWidth}px, 92vw)` }}
        >
          <ChatPanel room={room} layout={layout} onSend={onSend} />
        </aside>
      </>
    );

  return (
    <>
      {!open && <ChatRail layout={layout} floating={false} />}
      {open && resizable && (
        <div className="handle" {...layout.handleProps("chat")} />
      )}
      <aside
        ref={aside}
        aria-label="Room chat"
        className={`flex min-h-0 justify-end ${open && !resizable ? "ml-3" : ""}`}
        style={{
          flex: `0 0 ${open ? layout.chatWidth : 0}px`,
          minWidth: 0,
          overflowX: "clip",
          overflowY: "visible",
          transition: layout.dragging
            ? "none"
            : "flex-basis 220ms cubic-bezier(0.2, 0.7, 0.2, 1)",
        }}
      >
        <div className="h-full flex-none" style={{ width: layout.chatWidth }}>
          <ChatPanel room={room} layout={layout} onSend={onSend} />
        </div>
      </aside>
    </>
  );
}
