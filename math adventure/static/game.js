let gameState = {
    player: null,
    selectedClass: null,
    currentMode: null,
    monsterStreak: 0
};

function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(screen => {
        screen.classList.remove('active');
    });
    document.getElementById(screenId).classList.add('active');
}

async function startGame() {
    await fetch('/api/start-game', { method: 'POST' });
    showScreen('classScreen');
}

function selectClass(className) {
    gameState.selectedClass = className;
    document.querySelectorAll('.class-card').forEach(card => {
        card.style.border = '2px solid #ddd';
    });
    event.target.closest('.class-card').style.border = '3px solid #667eea';
}

async function startAdventure() {
    const playerName = document.getElementById('playerName').value || 'Adventurer';
    
    if (!gameState.selectedClass) {
        alert('Please select a class!');
        return;
    }

    const response = await fetch('/api/choose-class', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            class: gameState.selectedClass, 
            name: playerName 
        })
    });

    const data = await response.json();
    gameState.player = data.player;
    
    document.getElementById('playerInfo').textContent = 
        `You have chosen the ${gameState.player.class} class. Good luck, ${gameState.player.name}!`;
    
    loadRegions();
    showScreen('gameScreen');
}

async function loadRegions() {
    const response = await fetch('/api/regions');
    const regions = await response.json();
    
    const grid = document.getElementById('regionsGrid');
    grid.innerHTML = '';
    
    regions.forEach((region, idx) => {
        const card = document.createElement('div');
        card.className = `region-card ${region.locked ? 'locked' : ''}`;
        card.innerHTML = `
            <div class="emoji">${region.emoji}</div>
            <h4>${region.name}</h4>
            <p style="font-size: 0.9em; color: #666;">${region.problem_type}</p>
            <span class="status ${region.locked ? 'locked' : 'unlocked'}">
                ${region.locked ? '🔒 LOCKED' : '🔓 UNLOCKED'}
            </span>
        `;
        
        if (region.locked) {
            card.onclick = () => showUnlockChallenge(idx, region);
        } else {
            card.onclick = () => showNPCChallenge(idx, region);
        }
        
        grid.appendChild(card);
    });
}

async function showUnlockChallenge(regionId, region) {
    const response = await fetch('/api/npc-question', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ region_id: regionId })
    });

    const data = await response.json();
    
    gameState.currentMode = {
        type: 'unlock',
        regionId: regionId,
        correctAnswer: data.answer
    };

    document.getElementById('interactionTitle').textContent = 
        `🔐 To enter ${region.name}, solve this problem:`;
    document.getElementById('problemDisplay').textContent = data.problem;
    document.getElementById('interactionPanel').classList.remove('hidden');
    document.getElementById('answerInput').value = '';
    document.getElementById('answerInput').focus();
}

async function showNPCChallenge(regionId, region) {
    const response = await fetch('/api/npc-question', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ region_id: regionId })
    });

    const data = await response.json();
    
    gameState.currentMode = {
        type: 'npc',
        regionId: regionId,
        correctAnswer: data.answer
    };

    document.getElementById('interactionTitle').textContent = 
        `🔮 A wise NPC approaches in ${region.name}... The NPC shares an ancient math challenge:`;
    document.getElementById('problemDisplay').textContent = data.problem;
    document.getElementById('interactionPanel').classList.remove('hidden');
    document.getElementById('answerInput').value = '';
    document.getElementById('answerInput').focus();
}

async function submitAnswer() {
    const userAnswer = document.getElementById('answerInput').value;
    
    if (!userAnswer) {
        alert('Please enter an answer!');
        return;
    }

    if (gameState.currentMode.type === 'unlock') {
        await handleUnlockAnswer(userAnswer);
    } else if (gameState.currentMode.type === 'npc') {
        await handleNPCAnswer(userAnswer);
    } else if (gameState.currentMode.type === 'monster') {
        await handleMonsterAnswer(userAnswer);
    } else if (gameState.currentMode.type === 'bonus') {
        await handleBonusAnswer(userAnswer);
    }
}

async function handleUnlockAnswer(userAnswer) {
    const response = await fetch('/api/unlock-region', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            region_id: gameState.currentMode.regionId,
            answer: userAnswer
        })
    });

    const data = await response.json();
    
    if (data.success) {
        alert('✅ Correct! The gate unlocks.');
        closeInteraction();
        await startMonsterChallenge(gameState.currentMode.regionId);
    } else {
        alert(`❌ Incorrect! ${data.message}`);
    }
}

async function handleNPCAnswer(userAnswer) {
    if (String(userAnswer).trim() === String(gameState.currentMode.correctAnswer)) {
        alert('✅ Correct! You impress the NPC and gain a clue. 💰 + 200 COINS!');
        closeInteraction();
        await startMonsterChallenge(gameState.currentMode.regionId);
    } else {
        alert(`❌ Incorrect. The NPC gives you a hint: The answer was ${gameState.currentMode.correctAnswer}`);
        closeInteraction();
        await startMonsterChallenge(gameState.currentMode.regionId);
    }
}

async function startMonsterChallenge(regionId) {
    const regions = await (await fetch('/api/regions')).json();
    const region = regions[regionId];
    
    gameState.currentMode = {
        type: 'monster',
        regionId: regionId,
        streak: 0
    };

    document.getElementById('interactionTitle').textContent = 
        `🔥 A wild monster appears in ${region.name}! 🔥`;
    document.getElementById('interactionText').textContent = 
        'Answer 5 questions correctly in a row to defeat it!';
    
    await loadNextMonsterQuestion();
    document.getElementById('interactionPanel').classList.remove('hidden');
}

async function loadNextMonsterQuestion() {
    const regionId = gameState.currentMode.regionId;
    const response = await fetch('/api/monster-challenge', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ region_id: regionId })
    });

    const data = await response.json();
    gameState.currentMode.correctAnswer = data.answer;
    
    document.getElementById('problemDisplay').innerHTML = `
        <strong>${data.monster_name}</strong><br>
        ${data.monster_desc}<br><br>
        Monster challenge ${gameState.currentMode.streak + 1}/5:<br>
        ${data.problem}
    `;
    
    document.getElementById('answerInput').value = '';
    document.getElementById('answerInput').focus();
}

async function handleMonsterAnswer(userAnswer) {
    const isCorrect = String(userAnswer).trim() === String(gameState.currentMode.correctAnswer);
    
    if (isCorrect) {
        gameState.currentMode.streak++;
        
        if (gameState.currentMode.streak < 5) {
            alert(`✅ Correct! ${5 - gameState.currentMode.streak} more to defeat the monster!`);
            await loadNextMonsterQuestion();
        } else {
            alert('🎉 YOU DEFEATED THE MONSTER! 🎉');
            closeInteraction();
            await loadRegions();
            await checkAllUnlocked();
        }
    } else {
        alert(`❌ Incorrect! The answer was ${gameState.currentMode.correctAnswer}. Streak reset!`);
        gameState.currentMode.streak = 0;
        await loadNextMonsterQuestion();
    }
}

async function checkAllUnlocked() {
    const response = await fetch('/api/check-all-unlocked');
    const data = await response.json();
    
    if (data.all_unlocked) {
        const proceed = confirm('⭐ All regions have been unlocked! Face the Ultimate Bonus Challenge?');
        if (proceed) {
            await startBonusChallenge();
        }
    }
}

async function startBonusChallenge() {
    gameState.currentMode = {
        type: 'bonus',
        questionIndex: 0,
        correct: 0
    };

    showScreen('bonusScreen');
    await loadNextBonusQuestion();
}

async function loadNextBonusQuestion() {
    if (gameState.currentMode.questionIndex >= 5) {
        endBonusChallenge();
        return;
    }

    const response = await fetch('/api/bonus-challenge', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question_index: gameState.currentMode.questionIndex })
    });

    const data = await response.json();
    gameState.currentMode.correctAnswer = data.answer;

    document.getElementById('bonusContent').innerHTML = `
        <div style="text-align: center; margin: 30px 0;">
            <div style="font-size: 2em; margin-bottom: 10px;">${data.emoji} ${data.region}</div>
            <div style="background: #f0f4ff; padding: 20px; border-radius: 8px; margin: 20px 0; font-size: 1.1em;">
                Challenge ${gameState.currentMode.questionIndex + 1}/5: ${data.problem}
            </div>
            <input type="text" id="bonusAnswerInput" placeholder="Your answer" onkeypress="if(event.key==='Enter') submitBonusAnswer()" autofocus>
            <button onclick="submitBonusAnswer()" class="btn">Submit Answer</button>
        </div>
    `;

    setTimeout(() => {
        document.getElementById('bonusAnswerInput').focus();
    }, 100);
}

async function submitBonusAnswer() {
    const userAnswer = document.getElementById('bonusAnswerInput').value;
    await handleBonusAnswer(userAnswer);
}

async function handleBonusAnswer(userAnswer) {
    if (String(userAnswer).trim() === String(gameState.currentMode.correctAnswer)) {
        alert('✅ Correct! +100 XP');
        gameState.currentMode.correct++;
    } else {
        alert(`❌ Incorrect. The correct answer was ${gameState.currentMode.correctAnswer}.`);
    }

    gameState.currentMode.questionIndex++;
    await loadNextBonusQuestion();
}

function endBonusChallenge() {
    const correct = gameState.currentMode.correct;
    let title, message;

    if (correct === 5) {
        title = '🏆🏆🏆 PERFECT! YOU ARE A MATH MASTER! 🏆🏆🏆';
        message = `You have conquered all regions and proved your mathematical prowess!<br>
                   The math dimension bows to your incredible skill!<br><br>
                   ✨ You return home as a MATH MASTER! ✨<br>
                   💰 Carrying all the gold you collected on your journey! 💰`;
    } else if (correct >= 3) {
        title = '🎊 EXCELLENT WORK! You have completed the game! 🎊';
        message = 'You have proven yourself a worthy adventurer!';
    } else {
        title = '✨ You have completed the game! ✨';
        message = 'Keep practicing to master all the math regions!';
    }

    document.getElementById('finishTitle').textContent = title;
    document.getElementById('finishMessage').innerHTML = message;
    showScreen('finishedScreen');
}

function closeInteraction() {
    document.getElementById('interactionPanel').classList.add('hidden');
}

function skipBonus() {
    endBonusChallenge();
}
