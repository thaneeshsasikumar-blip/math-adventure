#!/usr/bin/env python3
"""
Math Adventure Web Server Launcher
Run this to start the web game in VS Code's browser
"""

import sys
import os
import threading
import time
from pathlib import Path

# Add the math adventure folder to path
math_adventure_dir = Path(__file__).parent / "math adventure"
sys.path.insert(0, str(math_adventure_dir))

# Try to import Flask, if not installed, provide instructions
try:
    from UI import app
except ImportError as e:
    print("Error: Flask is not installed!")
    print("\nTo install Flask, run:")
    print("pip install flask")
    sys.exit(1)

if __name__ == "__main__":
    print("\n" + "="*60)
    print("✨ MATH ADVENTURE QUEST - WEB SERVER ✨")
    print("="*60)
    print("\n🚀 Starting server on http://localhost:5000")
    print("🎮 Game will open in VS Code's built-in browser...\n")
    
    # Start server in background thread
    def run_server():
        app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
    
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    
    # Wait for server to start
    time.sleep(2)
    
    print("✅ Server started! Opening game...\n")
    print("💡 Tip: You can also open http://localhost:5000 in any browser\n")
    
    # Keep the script running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for playing Math Adventure!")
        sys.exit(0)
