"""Test the game class."""

import unittest
from game import Game


class TestGame(unittest.TestCase):
    """Test the game class."""

    def test_init_default_object(self):
        """Instantiate a object and test its class."""
        game = Game()
        self.assertIsInstance(game, Game)

    def test_switch_player(self):
        """Test so that the swtich player go back to 0 when reaching the highest index."""
        game = Game()
        player_list = ["player1", "player2"]
        game.start(player_list)
        game.switch_player()
        self.assertEqual(1, game.current_player)
        game.switch_player()
        self.assertEqual(0, game.current_player)

    def test_write_highscore(self):
        # pylint: disable=undefined-loop-variable
        """Tests that we save to the right file."""
        game = Game()
        msg = "test \n"
        game.write_highscore(msg)
        with open("highscore.txt", "r", encoding="utf-8") as file:
            for last_line in file:
                pass
        self.assertEqual(last_line, msg)
        file.close()

    def test_check_if_won(self):
        """Test so that it return true if over the max points to win."""
        game = Game()
        check = game.check_if_won(game.max_points + 5)
        self.assertTrue(check)
        check = game.check_if_won(game.max_points - 5)
        self.assertFalse(check)

    def test_start(self):
        """Checks so that the player get created correctly and started turns to true."""
        game = Game()
        player_names = ["test"]
        game.start(player_names)
        self.assertEqual(game.player_list[0].get_name(), "test")
        self.assertEqual(game.player_list[1].get_name(), "pc")
        self.assertTrue(game.started)

    def test_hold(self):
        # pylint: disable=unused-variable
        """Test so that the hold function return what it should."""
        game = Game()
        player_names = ["test"]
        game.start(player_names)
        game.points = 100
        check, msg = game.hold()
        self.assertTrue(check)
        game.points = 0
        check, msg = game.hold()
        self.assertFalse(check)

    def test_check_roll(self):
        """Test and se what roll we get and se what bool we get back."""
        game = Game()
        player_names = ["test"]
        game.start(player_names)

        roll = game.check_roll(1)
        self.assertFalse(roll)
        roll = game.check_roll(6)
        self.assertTrue(roll)
