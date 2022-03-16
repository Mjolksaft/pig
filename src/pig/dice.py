"""Used for getting a random value."""
import random


class Dice:
    """Dice class."""

    def __init__(self):
        """Init the class variables."""
        self.faces = 6
        self.value = 0

    def roll(self):
        """Roll the dice and save the value."""
        roll = random.randint(1, self.faces)
        return roll

    def set_faces(self, faces):
        """Set the faces on the dice."""
        self.faces = faces
