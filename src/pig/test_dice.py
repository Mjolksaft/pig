"""Test the dice class."""

import unittest
from dice import Dice


class TestDiceClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate a object and test its class."""
        die = Dice()
        self.assertIsInstance(die, Dice)
        res = die.faces
        exp = 6
        self.assertEqual(res, exp)

    def test_set_faces(self):
        """Check so that value is int."""
        die = Dice()
        die.set_faces(20)
        self.assertIsInstance(die.faces, int)

    def test_roll(self):
        """Test so that you cant roll outside of the bounds."""
        die = Dice()

        roll = die.roll()
        in_bounds = 1 <= roll <= die.faces
        self.assertTrue(in_bounds)
