from problems import generate_problem

class Region:
    def __init__(self, name, description, problem_type, emoji=None):
        self.name = name
        self.description = description
        self.problem_type = problem_type
        self.locked = True
        self.emoji = emoji or "📍"

    def try_unlock(self):
        print(f"\n🔐 To enter {self.name}, solve this problem:")
        problem, answer = generate_problem(self.problem_type)
        print(problem)
        user_answer = input("Your answer: ")
        if str(user_answer).strip() == str(answer):
            print("✅ Correct! The gate unlocks.")
            self.locked = False
            return True
        else:
            print(f"❌ Incorrect. The gate remains locked. (Correct answer: {answer})")
            return False

regions = [
    Region("Algebra Plains", "Linear equations, inequalities, systems", "algebra", "📐"),
    Region("Radical Forest", "Square roots, exponents, scientific notation", "radical", "🌲"),
    Region("Function Valley", "Function notation, tables, graphs", "function", "🏔️"),
    Region("Geometry Highlands", "Angle relationships, area, volume, Pythagorean theorem", "geometry", "⛰️"),
    Region("Statistics Sands", "Mean, median, data interpretation", "statistics", "🏜️"),
]

def explore_world(player):
    print("\n" + "="*70)
    print("🗺️  AVAILABLE REGIONS 🗺️")
    print("="*70 + "\n")
    
    region_boxes = []
    for idx, region in enumerate(regions):
        status = "🔓 UNLOCKED" if not region.locked else "🔒 LOCKED"
        
        # Create a formatted box for each region
        print(f"┌─────────────────────────────────────────────────────────────────┐")
        print(f"│ {idx+1}. {region.emoji}  {region.name:<45} {status:>12} │")
        print(f"├─────────────────────────────────────────────────────────────────┤")
        print(f"│    {region.description:<62} │")
        print(f"│    Problem Type: {region.problem_type.upper():<46} │")
        print(f"└─────────────────────────────────────────────────────────────────┘\n")
    
    choice = input("Choose a region to enter (1-5): ")
    try:
        idx = int(choice) - 1
        region = regions[idx]
        if region.locked:
            unlocked = region.try_unlock()
            if not unlocked:
                return None
        print(f"\n🌟 You enter {region.emoji} {region.name}")
        print(f"═" * 70)
        print(f"{region.description}")
        print(f"═" * 70 + "\n")
        # Placeholder for region-specific events
        return idx
    except (ValueError, IndexError):
        print("❌ Invalid region choice.")
        return None
