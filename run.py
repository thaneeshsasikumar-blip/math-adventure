#!/usr/bin/env python3
import sys
import os

# Add the math adventure folder to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "math adventure"))

# Now try to run main
try:
    from main import main
    main()
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
