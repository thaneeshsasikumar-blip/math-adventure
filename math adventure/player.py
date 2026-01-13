def choose_class():
    print("\n" + "="*60)
    print("⚔️  CHOOSE YOUR CLASS  ⚔️")
    print("="*60 + "\n")
    
    print("┌─────────────────────────────────────────────────────────┐")
    print("│ 1. 🗺️  EXPLORER                                          │")
    print("│    Agile and quick. Bonus movement speed!               │")
    print("├─────────────────────────────────────────────────────────┤")
    print("│ 2. 📚 SCHOLAR                                           │")
    print("│    Wise and knowledgeable. Bonus accuracy!              │")
    print("├─────────────────────────────────────────────────────────┤")
    print("│ 3. 🧠 STRATEGIST                                        │")
    print("│    Clever and tactical. Better problem-solving!         │")
    print("└─────────────────────────────────────────────────────────┘\n")
    
    choice = input("Enter 1, 2, or 3: ")
    classes = {"1": "Explorer", "2": "Scholar", "3": "Strategist"}
    player_class = classes.get(choice, "Explorer")
    
    print(f"\n✨ You have chosen the {player_class}! ✨\n")
    name = input("Enter your character's name: ")
    stats = {"Health": 100, "Focus": 50, "Knowledge Level": 1}
    return {"class": player_class, "name": name, "stats": stats}
