#!/bin/bash

# Load environment variables from .env if it exists
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Default ports
FRONTEND_PORT=${FRONTEND_PORT:-3000}
BACKEND_PORT=${BACKEND_PORT:-8000}

echo "Starting LeetRace development servers..."
echo "Frontend: http://localhost:${FRONTEND_PORT}"
echo "Backend:  http://localhost:${BACKEND_PORT}"
echo ""
echo "Press Ctrl+C to stop all servers"
echo ""

# Function to clean up background processes on exit
cleanup() {
    echo ""
    echo "Stopping servers..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}

trap cleanup SIGINT SIGTERM

# Start backend
cd "$(dirname "$0")" || exit 1
BACKEND_PORT=$BACKEND_PORT uv run python main.py &
BACKEND_PID=$!

# Start frontend
(cd frontend && FRONTEND_PORT=$FRONTEND_PORT BACKEND_PORT=$BACKEND_PORT pnpm dev) &
FRONTEND_PID=$!

# Wait for both processes
wait
