import { useCallback, useEffect, useRef, useState } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import {
  api,
  errorMessage,
  sessionToken,
  type RoomSnapshot,
  type Submission,
} from "../api";

export type Ranking = RoomSnapshot["rankings"][number];

export function formatTimer(seconds: number) {
  const rounded = Math.max(0, Math.ceil(seconds));
  return `${Math.floor(rounded / 60)}:${String(rounded % 60).padStart(2, "0")}`;
}

function copySelection(text: string) {
  const focused = document.activeElement;
  const input = document.createElement("textarea");
  input.value = text;
  input.readOnly = true;
  input.tabIndex = -1;
  input.setAttribute("aria-hidden", "true");
  input.style.cssText = "position:fixed;top:0;left:0;opacity:0";
  document.body.append(input);
  try {
    input.select();
    if (!document.execCommand("copy")) throw new Error("Copy blocked");
  } finally {
    input.remove();
    if (focused instanceof HTMLElement) focused.focus({ preventScroll: true });
  }
}

export function useRoom() {
  const [params] = useSearchParams();
  const roomId = params.get("id") ?? "";
  const token = sessionToken(roomId);
  const navigate = useNavigate();
  const [room, setRoom] = useState<RoomSnapshot | null>(null);
  const [connected, setConnected] = useState(false);
  const [error, setError] = useState("");
  const [pending, setPending] = useState(false);
  const pendingRef = useRef(false);
  const [code, setCode] = useState("");
  const [result, setResult] = useState<Submission | null>(null);
  const [review, setReview] = useState<{ name: string; code: string } | null>(
    null,
  );
  const [copied, setCopied] = useState<"code" | "link" | null>(null);
  const copyTimer = useRef<ReturnType<typeof setTimeout>>();

  useEffect(() => () => clearTimeout(copyTimer.current), []);

  useEffect(() => {
    for (const key of Object.keys(sessionStorage)) {
      if (key.startsWith("leetrace:draft:")) sessionStorage.removeItem(key);
    }
  }, []);

  useEffect(() => {
    if (!roomId || !token) return;
    const subscription = api.roomUpdates.subscribe(
      { roomId, token },
      {
        onStarted() {
          setConnected(true);
          setError("");
        },
        onConnectionStateChange(state) {
          setConnected(state.state === "pending");
        },
        onData(snapshot) {
          setRoom(snapshot);
          setConnected(true);
        },
        onError(error) {
          setConnected(false);
          setError(errorMessage(error));
        },
      },
    );
    return () => subscription.unsubscribe();
  }, [roomId, token]);

  const starterCode = room?.problem?.starterCode;
  const roundId = room?.roundId;
  useEffect(() => {
    setCode(starterCode ?? "");
    setResult(null);
    setReview(null);
  }, [roomId, roundId, starterCode]);

  const perform = useCallback(async (action: () => Promise<unknown>) => {
    if (pendingRef.current) return false;
    pendingRef.current = true;
    setPending(true);
    setError("");
    try {
      await action();
      return true;
    } catch (error) {
      setError(errorMessage(error));
      return false;
    } finally {
      pendingRef.current = false;
      setPending(false);
    }
  }, []);

  const finished = room ? room.me.locked || room.me.resigned : false;
  const readOnly =
    !room || room.state !== "playing" || finished || review !== null;
  const canAct = connected && !pending;

  function submit() {
    if (readOnly || !connected) return;
    void perform(async () => {
      setResult(await api.submit.mutate({ roomId, code }));
    });
  }

  async function leave() {
    if (await perform(() => api.leave.mutate({ roomId }))) {
      sessionStorage.removeItem(`leetrace:${roomId}`);
      navigate("/");
    }
  }

  async function copyRoom(kind: "code" | "link" = "code") {
    const text = kind === "link" ? `https://terse.codes/join/${roomId}` : roomId;
    try {
      if (navigator.clipboard) {
        try {
          await navigator.clipboard.writeText(text);
        } catch {
          copySelection(text);
        }
      } else {
        copySelection(text);
      }
      setError("");
      setCopied(kind);
      clearTimeout(copyTimer.current);
      copyTimer.current = setTimeout(() => setCopied(null), 2000);
    } catch {
      setError(`Couldn't copy the ${kind}. Copy it manually: ${text}`);
    }
  }

  const me = room?.rankings.find((player) => player.name === room.me.name);
  const waitingOn =
    room?.state === "playing"
      ? room.rankings
          .filter(
            (player) =>
              !player.resigned && player.lockedAt === null && !player.away,
          )
          .map((player) => player.name)
      : [];

  return {
    roomId,
    token,
    room,
    connected,
    error,
    setError,
    pending,
    canAct,
    code,
    changeCode: setCode,
    result: result ?? room?.me.submission ?? null,
    review,
    setReview,
    copied,
    copyRoom,
    me,
    isHost: room ? room.host === room.me.name : false,
    finished,
    readOnly,
    waitingOn,
    submit,
    leave,
    start: () => perform(() => api.start.mutate({ roomId })),
    lock: () => perform(() => api.lock.mutate({ roomId })),
    resign: () => perform(() => api.resign.mutate({ roomId })),
    advance: () =>
      perform(() =>
        room?.breakRemaining !== null
          ? api.skipBreak.mutate({ roomId })
          : api.restart.mutate({ roomId }),
      ),
    sendChat: async (message: string) => {
      try {
        await api.chat.mutate({ roomId, message });
        return true;
      } catch (error) {
        setError(errorMessage(error));
        return false;
      }
    },
  };
}

export type RoomState = ReturnType<typeof useRoom>;
