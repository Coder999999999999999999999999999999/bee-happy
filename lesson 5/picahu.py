import random

class Game:
    def __init__(self):
        self.ash_position = 0
        self.pikachu_position = random.randint(5, 10)
        self.is_game_over = False

    def print_intro(self):
        print("Welcome to the 'Ash Tries to Catch Pikachu' game!")
        print("Ash starts at position 0 and Pikachu is somewhere between position 5 and 10.")
        print("Try to catch Pikachu by moving forward!")

    def get_player_choice(self):
        choice = input("Do you want Ash to move forward? (yes/no): ").strip().lower()
        return choice

    def move_ash(self):
        move = random.randint(1, 3)
        self.ash_position += move
        print(f"Ash moves forward by {move} positions. Current position: {self.ash_position}")

    def check_game_over(self):
        if self.ash_position >= self.pikachu_position:
            self.is_game_over = True
            print("Congratulations! Ash caught Pikachu!")
        elif self.ash_position > self.pikachu_position:
            self.is_game_over = True
            print("Ash moved too far and missed Pikachu!")

    def play(self):
        self.print_intro()
        while not self.is_game_over:
            choice = self.get_player_choice()
            if choice == 'yes':
                self.move_ash()
                self.check_game_over()
            elif choice == 'no':
                print("Game over! Ash decided not to move.")
                self.is_game_over = True
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    game = Game()
    game.play()
