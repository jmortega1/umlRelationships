# Name: Jehan Kamilah M. Ortega
# Grade and Section: 9 - Argon
# Date: October 23, 2026

class Player:
    def __init__(self, username: str):
        self.username = username

# Trapper class inherits from Player class
class Trapper(Player):
    def trigger_trap(self):
        return f"🧨 {self.username} set off a redstone trap!"

# ----- Running the code -----
# 1. Instantiate a Trapper object with a username parameter passed to the Player parent
smp_member = Trapper("Judelow")

# 2. Invoke the unique subclass method using the inherited attribute
print(smp_member.trigger_trap())