# Name: Jehan Kamilah M. Ortega
# Grade and Section: 9 - Argon
# Date: October 23, 2026

class SMP:
    def __init__(self, server_name: str):
        self.server_name = server_name

    def host_connection(self, username: str):
        print(f"Connecting {username} to {self.server_name}...")

class Player:
    def __init__(self, username: str):
        self.username = username

    # Player depends on an SMP object strictly during this call
    def log_in(self, target_server: SMP):
        target_server.host_connection(self.username)

# ----- Running the code -----
# 1. Instantiate the individual tool objects independently
bliss = SMP("Bliss SMP")
p1 = Player("Quakitus")

# 2. Execute the function call passing the required dependent object
p1.log_in(bliss)
