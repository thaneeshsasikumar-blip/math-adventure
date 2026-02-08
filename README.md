# 🎮 Math Adventure Quest

A fun interactive math game built with Python Flask and web technologies!

## 🚀 Play (Local)

If you're running the game locally, open the game in your browser here after starting the server:

**[Open at mathadventure.com](http://localhost:5000)** (start the server first)

## 🎯 Features

- 🗺️ **5 Unique Regions**: Algebra, Radicals, Functions, Geometry, Statistics
- 🐉 **Monster Battles**: Defeat monsters by solving math problems
- 🎓 **3 Character Classes**: Explorer, Scholar, Strategist
- ⭐ **Bonus Challenge**: Ultimate test for true math masters
- 🎨 **Beautiful UI**: Modern web interface with animations

## 📋 How to Play

1. Choose your character class
2. Explore different math regions
3. Unlock regions by solving puzzles
4. Answer NPC challenges for rewards
5. Defeat monsters by getting 5 answers correct in a row
6. Complete the bonus challenge after unlocking all regions

## 🛠️ Setup & Run Locally

### Requirements
- Python 3.6+
- Flask

### Installation

1. Clone the repository:
```bash
git clone https://github.com/thaneeshsasikumar-blip/math-adventure.git
cd math-adventure
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python3 start_game.py
```

4. Open your browser and go to:
```
http://localhost:5000
```

## 🎓 Math Topics

- **Algebra**: Linear equations, inequalities
- **Radicals**: Square roots, exponents, scientific notation
- **Functions**: Function notation, graphs
- **Geometry**: Angles, areas, volumes, Pythagorean theorem
- **Statistics**: Mean, median, data interpretation

## 📁 Project Structure

```
math-adventure/
├── math adventure/
│   ├── main.py          # Terminal version
│   ├── UI.py            # Flask backend
│   ├── player.py        # Player class logic
│   ├── world.py         # Region definitions
│   ├── problems.py      # Math problem generator
│   ├── monster.py       # Monster definitions
│   ├── templates/       # HTML files
│   └── static/          # CSS and JavaScript
├── start_game.py        # Web launcher
└── requirements.txt     # Python dependencies
```

## 🌐 Deployment

### Deploy to Heroku

```bash
heroku login
heroku create your-app-name
git push heroku main
heroku open
```

### Deploy to Render.com

1. Push to GitHub
2. Go to [render.com](https://render.com)
3. Create new Web Service
4. Connect your GitHub repository
5. Deploy!

## 🎮 Terminal Version

You can also play in the terminal:
```bash
cd "math adventure"
python3 main.py
```

## 👨‍💻 Author

Created by Thaneesh Sasikumar

## 📄 License

MIT License

## 🤝 Contributing

Feel free to fork and submit pull requests!

---

**Have fun solving math problems!** 🧮✨
