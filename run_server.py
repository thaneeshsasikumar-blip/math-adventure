#!/usr/bin/env python3
"""
Math Adventure Quest - Web Launcher
This file is used for deployment on services like Heroku, Render, etc.
"""

import sys
import os
import subprocess

# Add the math adventure folder to path
math_adventure_dir = os.path.join(os.path.dirname(__file__), "math adventure")
sys.path.insert(0, math_adventure_dir)

# Try to import Flask
try:
    from UI import app
except ImportError:
    print("Error: Flask is not installed!")
    sys.exit(1)

if __name__ == "__main__":
    # Get port from environment or use default
    port = int(os.environ.get('PORT', 5000))
    host = '0.0.0.0'  # Listen on all interfaces for deployment
    
    print(f"\n✨ Math Adventure Quest - Web Server")
    print(f"🚀 Starting on {host}:{port}\n")
    
    # Run the Flask app
    app.run(host=host, port=port, debug=False)
