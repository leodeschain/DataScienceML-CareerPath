#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Create a timestamp
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Define the log file
LOG_FILE="debug.txt"

# Start logging
echo "--- Log started at $TIMESTAMP ---" > $LOG_FILE

# --- Environment Setup ---
echo "--- Setting up Python virtual environment ---" | tee -a $LOG_FILE
python3 -m venv .venv
echo "--- Activating virtual environment ---" | tee -a $LOG_FILE
source .venv/bin/activate
echo "--- Installing dependencies from requirements.txt ---" | tee -a $LOG_FILE
pip install -r requirements.txt | tee -a $LOG_FILE

# --- Linting and Testing ---
echo "--- Running linter (flake8) ---" | tee -a $LOG_FILE
flake8 . --exclude .venv --count --select=E9,F63,F7,F82 --show-source --statistics | tee -a $LOG_FILE
echo "--- Running tests (pytest) ---" | tee -a $LOG_FILE
pytest --maxfail=1 --disable-warnings | tee -a $LOG_FILE

# --- Finalization ---
echo "--- Setup script finished successfully ---" | tee -a $LOG_FILE
TIMESTAMP_END=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
echo "--- Log finished at $TIMESTAMP_END ---" >> $LOG_FILE

exit 0
