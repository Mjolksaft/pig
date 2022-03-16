"""Test the Player class."""

import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    """Player tests."""

    def test_init(self):
        """Check so that everything get init correctly."""
        player = Player("name")
        self.assertIsInstance(player, Player)
        self.assertIsInstance(player.score, int)

    def test_hold(self):
        """Test the hold function."""
        player = Player("name")
        points = 100
        player.hold(points)
        self.assertEqual(player.score, points)

    def test_set_name(self):
        """Test so that name gets changed correctly."""
        player = Player("name")
        new_name = "new_name"
        player.set_name("new_name")
        self.assertEqual(player.name, new_name)

    def test_get_score(self):
        """Test that we get the correct score."""
        player = Player("name")
        player.score = 100
        self.assertEqual(player.get_score(), 100)
