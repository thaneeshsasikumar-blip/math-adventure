class Monster:
    def __init__(self, name, description, region_type):
        self.name = name
        self.description = description
        self.region_type = region_type

monsters_by_region = {
    "algebra": Monster("Linear Lurker", "Attacks using two-step equations.", "algebra"),
    "radical": Monster("Radiclaw Beast", "Uses square root and exponent challenges.", "radical"),
    "function": Monster("Graph Golem", "Players must identify slope or intercepts.", "function"),
    "geometry": Monster("Angle Guardian", "Requires angle relationships to block attacks.", "geometry"),
    "statistics": Monster("Data Djinn", "Challenges with mean, median, and data interpretation.", "statistics"),
}

def get_monster(region_type):
    return monsters_by_region.get(region_type)