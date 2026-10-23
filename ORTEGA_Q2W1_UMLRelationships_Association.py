# Name: Jehan Kamilah M. Ortega
# Grade and Section: 9 - Argon
# Date: October 23, 2026

class SMP:
    def __init__(self, server_name: str):
        self.server_name = server_name
        self.connected_players = []  # Keeps track of players connected to this server

class Player:
    def __init__(self, username: str, role: str):
        self.username = username
        self.role = role  # Establishes a standard role for the player
        self.current_server = None  

    def join_server(self, server: SMP):
        self.current_server = server
        server.connected_players.append(self)

# ----- Running the code -----
# 1. Instantiate the SMP server independent of players
unstable = SMP("Unstable Universe")

# 2. Instantiate individual players independently
p1 = Player("Spoke_Is_Here", "The Emperor of The End")
p2 = Player("FlameFrags", "The Combat Grandmaster")
p3 = Player("Wemmbu", "The Invisible Knight")
p4 = Player("ParrotX2", "The Fallen King")

# 3. Establish the association via an interaction
p1.join_server(unstable)
p2.join_server(unstable)
p3.join_server(unstable)
p4.join_server(unstable)

# 4. Verify the cross-referencing capabilities
print(f"Server Profile: {unstable.server_name}")
print("Active player connection list tracked via Association:")
for p in unstable.connected_players:
    print(f"  - Player: {p.username} | Role: {p.role}")

print(f"\nPlayer lookup -> {p1.username} currently visiting: {p1.current_server.server_name}")