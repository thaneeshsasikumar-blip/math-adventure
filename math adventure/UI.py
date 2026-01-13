from flask import Flask, render_template, redirect, url_for, request, jsonify
import os
import sys
import shlex
import subprocess
from player import choose_class as terminal_choose_class
from world import regions
from problems import generate_problem
from monster import get_monster

pkg_dir = os.path.dirname(__file__)
template_dir = os.path.join(pkg_dir, "templates")

app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'math_adventure_secret'

# Store game state
game_state = {
    'player': None,
    'current_region': None,
    'stage': 'start'  # start, class_select, playing, bonus, finished
}


@app.route("/")
def index():
    return render_template("game.html")


@app.route("/api/start-game", methods=['POST'])
def start_game():
    game_state['stage'] = 'class_select'
    return jsonify({'status': 'ready'})


@app.route("/api/choose-class", methods=['POST'])
def choose_class():
    data = request.json
    player_class = data.get('class', 'Explorer')
    player_name = data.get('name', 'Adventurer')
    
    game_state['player'] = {
        'class': player_class,
        'name': player_name,
        'stats': {"Health": 100, "Focus": 50, "Knowledge Level": 1}
    }
    game_state['stage'] = 'playing'
    
    return jsonify({'status': 'success', 'player': game_state['player']})


@app.route("/api/regions")
def get_regions():
    region_data = []
    for idx, region in enumerate(regions):
        region_data.append({
            'id': idx,
            'name': region.name,
            'emoji': region.emoji,
            'description': region.description,
            'problem_type': region.problem_type,
            'locked': region.locked
        })
    return jsonify(region_data)


@app.route("/api/unlock-region", methods=['POST'])
def unlock_region():
    data = request.json
    region_id = data.get('region_id')
    user_answer = data.get('answer')
    
    region = regions[region_id]
    problem, answer = generate_problem(region.problem_type)
    
    is_correct = str(user_answer).strip() == str(answer)
    
    if is_correct:
        region.locked = False
        return jsonify({'success': True, 'message': 'Gate unlocked!'})
    else:
        return jsonify({'success': False, 'message': f'Incorrect. The answer was {answer}'})


@app.route("/api/npc-question", methods=['POST'])
def npc_question():
    data = request.json
    region_id = data.get('region_id')
    user_answer = data.get('answer')
    
    if user_answer is None:
        # Generate a new question
        problem, answer = generate_problem(regions[region_id].problem_type)
        return jsonify({
            'problem': problem,
            'answer': answer,  # Send to client for validation
            'region': regions[region_id].name
        })
    else:
        # Validate answer
        problem, answer = generate_problem(regions[region_id].problem_type)
        is_correct = str(user_answer).strip() == str(answer)
        return jsonify({'correct': is_correct, 'answer': answer})


@app.route("/api/monster-challenge", methods=['POST'])
def monster_challenge():
    data = request.json
    region_id = data.get('region_id')
    user_answer = data.get('answer')
    
    region = regions[region_id]
    monster = get_monster(region.problem_type)
    
    problem, answer = generate_problem(region.problem_type)
    is_correct = str(user_answer).strip() == str(answer)
    
    return jsonify({
        'problem': problem,
        'correct': is_correct,
        'answer': answer,
        'monster_name': monster.name if monster else 'Unknown Monster',
        'monster_desc': monster.description if monster else ''
    })


@app.route("/api/bonus-challenge", methods=['POST'])
def bonus_challenge():
    data = request.json
    question_index = data.get('question_index')
    user_answer = data.get('answer')
    
    region = regions[question_index]
    
    if user_answer is None:
        # Generate new question
        problem, answer = generate_problem(region.problem_type)
        return jsonify({
            'problem': problem,
            'answer': answer,
            'region': region.name,
            'emoji': region.emoji,
            'index': question_index
        })
    else:
        # Validate answer
        problem, answer = generate_problem(region.problem_type)
        is_correct = str(user_answer).strip() == str(answer)
        return jsonify({'correct': is_correct, 'answer': answer})


@app.route("/api/check-all-unlocked")
def check_all_unlocked():
    all_unlocked = all(not region.locked for region in regions)
    return jsonify({'all_unlocked': all_unlocked})


@app.route("/launch")
def launch():
    # Legacy terminal launcher
    script = os.path.join(pkg_dir, "main.py")
    python_exe = sys.executable or "/usr/bin/env python3"
    cmd = f"cd {shlex.quote(pkg_dir)} && {shlex.quote(python_exe)} {shlex.quote(script)}"
    applescript = f'tell application "Terminal" to do script "{cmd}"'
    try:
        subprocess.Popen(["osascript", "-e", applescript])
    except Exception:
        subprocess.Popen(cmd, shell=True)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port=5000, debug=True)
