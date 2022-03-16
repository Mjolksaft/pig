"""Module doc string."""

import player
import computer


class Game:
    """Class doc string."""

    file_path = "highscore.txt"

    def __init__(self):
        """Init the class variables."""
        self.max_points = 20
        self.current_player = 0
        self.started = False
        self.player_list = []
        self.points = 0

    def start(self, players):
        """Start creates player and computer objects based on how many names where entered."""
        try:
            self.player_list.clear()
            self.current_player = 0

            times = len(players)
            for value in range(times):
                character = player.Player(players[value])
                self.player_list.append(character)
            if times == 1:
                bot = computer.Computer("pc")
                self.player_list.append(bot)
            self.started = True
            return
        except ValueError as error:
            print(error)

    def check_roll(self, roll):
        """Return true or false if roll is over 1."""
        if roll != 1:
            self.points += roll
            return True

        self.points = 0
        return False

    def hold(self):
        """Hold the points."""
        try:
            if self.points != 0:
                self.player_list[self.current_player].hold(self.points)
                player_score = self.player_list[self.current_player].get_score()
                player_name = self.player_list[self.current_player].get_name()
                hold_amount = f"{player_name} hold {self.points} points \n"
                current_holding = f"{player_name} currently have {player_score} score \n "
                msg = hold_amount + current_holding
                self.points = 0
                return True, msg
        except (AttributeError, IndexError) as error:
            print(error)

        msg = "you cant hold 0 points"
        return False, msg

    def switch_player(self):
        """Switch wich player is currently playing."""
        if self.current_player >= len(self.player_list) - 1:
            self.current_player = 0
        else:
            self.current_player += 1

        msg = f"({self.player_list[self.current_player].get_name()}) "
        return msg

    def write_highscore(self, msg):
        """Open and write to the file highscore.txt."""
        try:
            with open(self.file_path, "a", encoding="utf-8") as file:
                file.write(str(msg))
                file.close()
        except FileNotFoundError as error:
            print(error)

    def check_if_won(self, player_score):
        """Return True if the player has won or not by checking the score with the maxPoints."""
        if player_score >= self.max_points:
            self.started = False
            return True
        return False
