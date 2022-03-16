"""Used to interact with the user."""
import random
import cmd
import game
import computer
import dice


class Command(cmd.Cmd):
    """Shell class."""

    intro = "Type help or ? to list commands.\n"
    prompt = "(Game) "

    def __init__(self):
        """Init the objects."""
        super().__init__()
        self.die = dice.Dice()
        self.game = game.Game()

    def do_start(self, players):
        """Start Name Name to select how many player and what their name is if only one name is entered an ai will take their place."""
        msg = "Missing argument on how many players you want."
        if not players:  # if thre is not any arguments there print message
            print(msg)
            return

        player_names = str(players).split(' ')
        self.game.start(player_names)
        player = self.game.player_list[self.game.current_player]
        self.prompt = f"({player.get_name()}) "

    def do_roll(self, _):
        """Roll the dice."""
        if self.game.started:
            roll = self.die.roll()
            succeded_roll = self.game.check_roll(roll)

            if not succeded_roll:
                print(f"unlucky {self.game.player_list[self.game.current_player].get_name()} rolled a 1! \n")
                self.prompt = self.game.switch_player()
                if isinstance(self.game.player_list[self.game.current_player], computer.Computer):
                    self.computer_turn()
            else:
                player_name = self.game.player_list[self.game.current_player].get_name()
                print(f"{player_name} rolled a [{roll}]")
        else:
            print("need to start first")

    def do_hold(self, _):
        """Hold the points."""
        if self.game.started:
            succeded_hold, msg = self.game.hold()
            print(msg)

            if self.game.check_if_won(self.game.player_list[self.game.current_player].get_score()):
                msg = ""
                players = len(self.game.player_list)
                for player in range(players):
                    msg += f"name: {self.game.player_list[player].get_name()} "
                    msg += f"score: {self.game.player_list[player].get_score()} "
                    if player != len(self.game.player_list) - 1:
                        msg += "vs "
                    else:
                        msg += f"to {self.game.max_points }\n"

                self.game.write_highscore(msg)
                print(f"congratulation {self.game.player_list[self.game.current_player].get_name()}")
                print("to start again write start")
                self.prompt = "(game) "
                return

            if succeded_hold:
                self.prompt = self.game.switch_player()
                if isinstance(self.game.player_list[self.game.current_player], computer.Computer):
                    self.computer_turn()
        else:
            print("need to start first")

    def do_change_name(self, new_name):
        """Change_name new_name to change the name of the current player."""
        if self.game.started:
            msg = "Missing argument on what name you want, write changeName NAME."
            if not new_name:  # if thre is not any arguments there print message
                print(msg)
                return

            try:
                player = self.game.player_list[self.game.current_player]
                player.set_name(new_name)
                self.prompt = f"({new_name}) "
                print(f"you changed name to {new_name}")
            except (AttributeError, IndexError) as error:
                print(error)
        else:
            print("need to start first")

    def do_restart(self, players):
        """Start the game again."""
        return self.do_start(players)

    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Leave the game."""
        print("Bye bye")
        return True

    def do_cheat(self, points):
        """Cheat amount_of_points gives the player the amount of points they enter."""
        msg = "Missing argument on how many points you want."
        if not points:  # if thre is not any arguments there print message
            print(msg)
            return
        try:
            if self.game.started:
                self.game.points += int(points)
            else:
                print("you need to start the game first")
        except ValueError as error:
            print(error)

    def computer_turn(self):
        """Plays the computers turn by getting a random number and doing that many rolls."""
        rolls = random.randint(1, 5)
        roll = 0
        while roll <= rolls:
            if isinstance(self.game.player_list[self.game.current_player], computer.Computer):
                self.do_roll("_")
            roll += 1

        if isinstance(self.game.player_list[self.game.current_player], computer.Computer):
            self.do_hold("_")
