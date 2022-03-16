"""Test the computer class."""

import unittest
from computer import Computer


class TestComputer(unittest.TestCase):
    """Computer tests."""

    def test_init(self):
        """Check so that everything get init correctly."""
        computer = Computer("name")
        self.assertIsInstance(computer, Computer)
        self.assertIsInstance(computer.score, int)

    def test_hold(self):
        """Test the hold function."""
        computer = Computer("name")
        points = 100
        computer.hold(points)
        self.assertEqual(computer.score, points)

    def test_set_name(self):
        """Test so that name gets changed correctly."""
        computer = Computer("name")
        new_name = "new_name"
        computer.set_name("new_name")
        self.assertEqual(computer.name, new_name)

    def test_get_score(self):
        """Test that we get the correct score."""
        computer = Computer("name")
        computer.score = 100
        self.assertEqual(computer.get_score(), 100)
