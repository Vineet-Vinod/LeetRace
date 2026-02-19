#!/bin/bash

# Load environment variables from .env if it exists
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Default ports
FRONTEND_PORT=${FRONTEND_PORT:-3000}
BACKEND_PORT=${BACKEND_PORT:-8000}

SESSION_NAME="leetrace"

# Kill any existing session
tmux kill-session -t $SESSION_NAME 2>/dev/null || true

echo "Frontend: http://localhost:${FRONTEND_PORT}"
echo "Backend:  http://localhost:${BACKEND_PORT}"
echo "Press Ctrl+C in either pane to stop all servers"
echo ""

# Create new session
tmux new-session -d -s $SESSION_NAME -x 200 -y 50 -c "$(pwd)"

# Each command chains "tmux kill-session" so that Ctrl-C in either pane kills everything
tmux send-keys -t $SESSION_NAME "BACKEND_PORT=$BACKEND_PORT uv run python main.py; tmux kill-session -t $SESSION_NAME" Enter

# Create second pane (frontend) with horizontal split
tmux split-window -t $SESSION_NAME -h -c "$(pwd)/frontend"
tmux send-keys -t $SESSION_NAME "FRONTEND_PORT=$FRONTEND_PORT BACKEND_PORT=$BACKEND_PORT pnpm dev; tmux kill-session -t $SESSION_NAME" Enter

# Balance the layout
tmux select-layout -t $SESSION_NAME even-horizontal

# Attach to session — returns when the session is killed
tmux attach-session -t $SESSION_NAME
