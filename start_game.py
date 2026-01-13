#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "math adventure"))

from UI import app

if __name__ == "__main__":
    print("\n✨ Starting Math Adventure Web Server...")
    print("📱 Open the Simple Browser and go to: http://localhost:5000\n")
    app.run(host='127.0.0.1', port=5000, debug=False)
