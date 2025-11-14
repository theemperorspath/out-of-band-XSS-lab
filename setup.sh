#!/bin/bash

echo "[*] Setting up Blind XSS Lab..."

# Update system
sudo apt update

# Install chromium + driver
echo "[*] Installing Chromium + Chromedriver..."
sudo apt install -y chromium chromium-driver

# Make venv
echo "[*] Creating Python virtual environment..."
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Install Python deps
echo "[*] Installing Python dependencies..."
pip install -r requirements.txt --break-system-packages

echo ""
echo "===================================================="
echo "✔ Setup complete!"
echo "To start the lab:"
echo ""
echo "    source venv/bin/activate"
echo "    python3 app.py"
echo ""
echo "Lab running at: http://127.0.0.1:5000"
echo "===================================================="
