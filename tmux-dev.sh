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
echo "Press Ctrl+C to stop all servers"
echo ""

# Create new session
tmux new-session -d -s $SESSION_NAME -x 200 -y 50
tmux send-keys -t $SESSION_NAME "cd $(pwd) && BACKEND_PORT=$BACKEND_PORT uv run python main.py" Enter
tmux split-window -t $SESSION_NAME -h
tmux send-keys -t $SESSION_NAME "cd $(pwd)/frontend && FRONTEND_PORT=$FRONTEND_PORT BACKEND_PORT=$BACKEND_PORT pnpm dev" Enter
tmux select-layout -t $SESSION_NAME even-horizontal

# Attach and clean up on exit
tmux attach-session -t $SESSION_NAME
tmux kill-session -t $SESSION_NAME 2>/dev/null || true
