# Name: Jehan Kamilah M. Ortega
# Grade and Section: 9 - Argon
# Date: October 23, 2026

from abc import ABC, abstractmethod

class Craftable(ABC):
    @abstractmethod
    def craft(self, materials: list) -> bool:
        pass

# CraftingTable realizes/implements Craftable
class CraftingTable(Craftable):
    def craft(self, materials: list) -> bool:
        print(f"[Crafting Table] Combining materials: {', '.join(materials)}")
        print("Success! Created 1x Spyglass. It's all yours.")
        return True

# ----- Running the code -----
# 1. Instantiate the concrete implementation class
grid = CraftingTable()

# 2. Invoke the realized method
success = grid.craft(["Amethyst Shard", "Copper Ingot", "Copper Ingot"])
print(f"Crafting Status: {success}")
