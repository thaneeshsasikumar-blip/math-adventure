try:
    from math_adventure.player import choose_class
    from math_adventure.world import explore_world, regions
    from math_adventure.problems import generate_problem
    from math_adventure.monster import get_monster
except Exception:
    from player import choose_class
    from world import explore_world, regions
    from problems import generate_problem
    from monster import get_monster


def monster_encounter(region):
    monster = get_monster(region.problem_type)
    print(f"\n🔥 A wild monster appears in {region.name}! 🔥")
    if monster:
        print(f"┌────────────────────────────────┐")
        print(f"│ It's the {monster.name}!")
        print(f"│ {monster.description}")
        print(f"└────────────────────────────────┘")
    print(f"To defeat it, answer 5 {region.problem_type}-themed questions correctly in a row.")
    correct_streak = 0
    attempt = 1
    while correct_streak < 5:
        problem, answer = generate_problem(region.problem_type)
        print(f"Monster challenge {correct_streak+1}/5: {problem}")
        user_answer = input("Your answer: ")
        if str(user_answer).strip() == str(answer):
            print("✅ Correct!")
            correct_streak += 1
            if correct_streak < 5:
                print(f"   {5-correct_streak} more to defeat the monster! Keep going!")
        else:
            print(f"❌ Incorrect! The monster laughs. The answer was {answer}.")
            print("   Don't give up! Try again from the beginning.")
            correct_streak = 0
            attempt += 1
    print(f"\n🎉 YOU DEFEATED THE MONSTER! 🎉")
    print(f"   Victory achieved after {attempt} attempt(s)!")
    print("   As the monster vanishes, you encounter tons of coins!")
    print("   You collect your reward and feel accomplished.\n")

def bonus_level():
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                                                            ║")
    print("║            ⭐ ULTIMATE BONUS CHALLENGE ⭐                  ║")
    print("║                                                            ║")
    print("║    You have unlocked all regions! Face the final test...   ║")
    print("║    Answer 1 question from each region to complete the game!║")
    print("║                                                            ║")
    print("╚════════════════════════════════════════════════════════════╝\n")
    
    input("Press Enter to begin the Ultimate Challenge...")
    print()
    
    bonus_regions = regions
    correct_count = 0
    
    for idx, region in enumerate(bonus_regions, 1):
        print(f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"Challenge {idx}/5: {region.emoji} {region.name}")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        problem, answer = generate_problem(region.problem_type)
        print(problem)
        user_answer = input("Your answer: ")
        
        if str(user_answer).strip() == str(answer):
            print(f"✅ Correct! +100 XP")
            correct_count += 1
        else:
            print(f"❌ Incorrect. The correct answer was {answer}.")
    
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print(f"║ FINAL SCORE: {correct_count}/5 QUESTIONS ANSWERED CORRECTLY      ║")
    print("╚════════════════════════════════════════════════════════════╝\n")
    
    if correct_count == 5:
        print("🏆🏆🏆 PERFECT! YOU ARE A MATH MASTER! 🏆🏆🏆")
        print("You have conquered all regions and proved your mathematical prowess!")
        print("The math dimension bows to your incredible skill!\n")
        print("╔════════════════════════════════════════════════════════════╗")
        print("║                                                            ║")
        print("║  With all your newfound knowledge and countless gold,      ║")
        print("║  you open a portal back to your own world...              ║")
        print("║                                                            ║")
        print("║  ✨ You return home as a MATH MASTER! ✨                  ║")
        print("║  💰 Carrying all the gold you collected on your journey! 💰 ║")
        print("║                                                            ║")
        print("╚════════════════════════════════════════════════════════════╝\n")
    elif correct_count >= 3:
        print("🎊 EXCELLENT WORK! You have completed the game! 🎊")
        print("You have proven yourself a worthy adventurer!\n")
    else:
        print("✨ You have completed the game! ✨")
        print("Keep practicing to master all the math regions!\n")

def main():
    # Display title banner
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                                                            ║")
    print("║               ✨ MATH ADVENTURE QUEST ✨                   ║")
    print("║                                                            ║")
    print("║        🧮  Solve math problems and defeat monsters!  🧮    ║")
    print("║                                                            ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print("\n")
    
    print("Welcome to Math Adventure!")
    player = choose_class()
    print(f"\n🌟 You have chosen the {player['class']} class. Good luck, {player['name']}! 🌟")
    print("You have been transported to the new dimension filled with 9th grade math!")
    print("="*62 + "\n")
    while True:
        region_idx = explore_world(player)
        # After entering a region, if it is unlocked, ask a follow-up question
        if region_idx is not None and not regions[region_idx].locked:
            print(f"\n🔮 A wise NPC approaches in {regions[region_idx].name}...")
            print("╔─────────────────────────────────────────────────────╗")
            print("║ The NPC shares an ancient math challenge...         ║")
            print("╚─────────────────────────────────────────────────────╝\n")
            problem, answer = generate_problem(regions[region_idx].problem_type)
            print("NPC asks:", problem)
            user_answer = input("Your answer: ")
            if str(user_answer).strip() == str(answer):
                print("✅ Correct! You impress the NPC and gain a clue.")
                print("💰 + 200 COINS! 💰\n")
            else:
                print(f"❌ Incorrect. The NPC gives you a hint: The answer was {answer}.")
            # Monster encounter after NPC
            monster_encounter(regions[region_idx])
        
        # Check if all regions are unlocked
        all_unlocked = all(not region.locked for region in regions)
        
        if all_unlocked:
            print("\n⭐ All regions have been unlocked! ⭐")
            cont = input("Face the Ultimate Bonus Challenge? (y/n): ")
            if cont.lower() == 'y':
                bonus_level()
                print("\n" + "="*62)
                print("Thanks for playing Math Adventure! 🎮 See you next time! 👋")
                print("="*62 + "\n")
                break
        else:
            cont = input("Explore another region? (y/n): ")
            if cont.lower() != 'y':
                print("\n" + "="*62)
                print("Thanks for playing Math Adventure! 🎮 See you next time! 👋")
                print("="*62 + "\n")
                break

if __name__ == "__main__":
    main()
