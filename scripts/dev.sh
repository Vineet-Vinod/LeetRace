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

# PIDs of background processes
BACKEND_PID=""
FRONTEND_PID=""

# Function to clean up background processes on exit
cleanup() {
    echo ""
    echo "Stopping servers..."

    # Kill background processes if they exist and are still running
    if [ -n "$BACKEND_PID" ] && kill -0 $BACKEND_PID 2>/dev/null; then
        kill $BACKEND_PID 2>/dev/null
    fi
    if [ -n "$FRONTEND_PID" ] && kill -0 $FRONTEND_PID 2>/dev/null; then
        kill $FRONTEND_PID 2>/dev/null
    fi

    # Give processes a moment to terminate gracefully
    sleep 0.5

    # Force kill any remaining processes
    kill -9 $BACKEND_PID $FRONTEND_PID 2>/dev/null || true

    exit 0
}

# Set up trap to catch SIGINT (Ctrl+C) and SIGTERM
trap cleanup SIGINT SIGTERM

# Start backend
cd "$(dirname "$0")" || exit 1
BACKEND_PORT=$BACKEND_PORT uv run python main.py &
BACKEND_PID=$!

# Start frontend
(cd frontend && FRONTEND_PORT=$FRONTEND_PORT BACKEND_PORT=$BACKEND_PORT pnpm dev) &
FRONTEND_PID=$!

# Wait for either process to exit, then kill both
# This is done by waiting for each in a loop so we can respond to any exit
while true; do
    if ! kill -0 $BACKEND_PID 2>/dev/null; then
        # Backend process died
        echo "Backend process exited, shutting down frontend..."
        cleanup
    fi

    if ! kill -0 $FRONTEND_PID 2>/dev/null; then
        # Frontend process died
        echo "Frontend process exited, shutting down backend..."
        cleanup
    fi

    sleep 0.5
done
