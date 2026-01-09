import random

class RPSGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_score = 0
        self.computer_score = 0

    def play_round(self):
        choices = ["rock", "paper", "scissors"]

        player_move = input("Enter your move (rock/paper/scissors): ").lower()
        computer_move = random.choice(choices)

        print(f"Computer chose: {computer_move}")

        if player_move == computer_move:
            print("Result: Draw")

        elif (
            (player_move == "rock" and computer_move == "scissors") or
            (player_move == "paper" and computer_move == "rock") or
            (player_move == "scissors" and computer_move == "paper")
        ):
            print("Result: You Win")
            self.player_score += 1

        else:
            print("Result: You Lose")
            self.computer_score += 1

    def show_score(self):
        print("\n--- SCOREBOARD ---")
        print(f"{self.player_name} : {self.player_score}")
        print(f"Computer : {self.computer_score}")


# -------- Run the Game --------
player_name = input("Enter player name: ")
rounds = int(input("Enter number of rounds: "))

game = RPSGame(player_name)

for _ in range(rounds):
    game.play_round()

game.show_score()