# Name: Jehan Kamilah M. Ortega
# Grade and Section: 9 - Argon 
# Date: October 23, 2026

class Player:
    def __init__(self, name: str):
        self.name = name

    def __del__(self):
        print(f"Player '{self.name}' has been removed from memory.")

class Team:
    def __init__(self, team_name: str, players: list[Player]):
        self.team_name = team_name
        self.players = players # Accepts existing Player objects

    def __del__(self):
        print(f"Team '{self.team_name}' has been disbanded.")

# ----- Running the code -----
# 1. Players are created independently first
p1 = Player("Nufuli")
p2 = Player("Loonac")
p3 = Player("Dimofyy")

# 2. Passed into the container class
my_team = Team("Barrier Trio", [p1, p2, p3])
print(f"Team active with: {[p.name for p in my_team.players]}")

print("\nExecuting: del my_team")
del my_team # Wipes out the team container

print("\nChecking variable accessibility after container deletion:")
print(f"Still active in memory -> p1: {p1.name}")
print(f"Still active in memory -> p2: {p2.name}")
print(f"Still active in memory -> p3: {p3.name}")