#!/bin/sh
cd "$(dirname "$0")"
echo "Open http://localhost:8000/templates/login.html (phone: use your computer's IP instead of localhost)"
python3 -m http.server 8000
