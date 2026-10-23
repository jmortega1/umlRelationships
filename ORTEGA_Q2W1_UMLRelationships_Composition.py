# Name: Jehan Kamilah M. Ortega
# Grade and Section: 9 - Argon
# Date: October 23, 2026

class Biome:
    def __init__(self, name: str):
        self.name = name

class World:
    def __init__(self):
        # The World creates and owns these Biome objects directly
        self.biomes = [Biome("Nether"), Biome("End")]

# ----- Running the code -----
# 1. Instantiate the parent object (World)
smp_world = World()

# 2. Access the Biome objects through the World object
for biome in smp_world.biomes:
    print(f"The {biome.name} is a biome in the world.")