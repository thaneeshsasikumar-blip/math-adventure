# 🎮 Math Adventure Quest - Browser Version

This is the web-based version of Math Adventure Quest! Play the game directly in your browser.

## 🚀 How to Run

### Method 1: Quick Start (Recommended)
```bash
cd /workspaces/math-adventure
python3 run_web.py
```

The server will start and automatically open the game in your browser at `http://localhost:5000`

### Method 2: Manual Start
```bash
# Install Flask if not already installed
pip install flask

# Navigate to the project
cd /workspaces/math-adventure

# Start the server
cd "math adventure"
python3 -c "from UI import app; app.run(host='0.0.0.0', port=5000, debug=True)"
```

Then open your browser and go to: `http://localhost:5000`

## 📋 Requirements

- Python 3.6+
- Flask (install with: `pip install flask`)

## 🎯 Game Features

- **5 Unique Regions**: Explore Algebra Plains, Radical Forest, Function Valley, Geometry Highlands, and Statistics Sands
- **Monster Battles**: Defeat monsters by answering 5 math questions correctly in a row
- **3 Character Classes**: Choose from Explorer, Scholar, or Strategist
- **Bonus Challenge**: Face the ultimate challenge after unlocking all regions
- **Beautiful UI**: Modern web interface with smooth animations

## 🎮 How to Play

1. **Start Game**: Click the start button on the welcome screen
2. **Choose Class**: Select your character class (Explorer, Scholar, or Strategist)
3. **Enter Name**: Give your adventurer a name
4. **Explore Regions**: Click on regions to:
   - Unlock locked regions by solving a puzzle
   - Answer NPC challenges for bonus coins
   - Fight monsters by answering 5 questions correctly
5. **Unlock All Regions**: Once all regions are unlocked, face the Ultimate Bonus Challenge
6. **Complete**: Finish the game and see your final score!

## 🔧 Troubleshooting

### "No module named 'flask'"
Install Flask with: `pip install flask`

### "Address already in use"
The port 5000 is already in use. Change the port in the launcher script or kill the process using that port.

### Browser doesn't open automatically
Manually open your browser and go to: `http://localhost:5000`

## 🎓 Math Topics Covered

- **Algebra**: Linear equations and inequalities
- **Radicals**: Square roots and exponents
- **Functions**: Function notation and graphs
- **Geometry**: Angles, areas, and the Pythagorean theorem
- **Statistics**: Mean, median, and data interpretation

Enjoy your Math Adventure! 🧮✨
