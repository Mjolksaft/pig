"""
Player class which holds the player score and name.

the class also has the functions to alter name and change the score.
"""


class Player:
    """Player class."""

    name = "none"

    def __init__(self, name):
        """Init the variables."""
        self.score = 0
        self.name = name

    def hold(self, points):
        """Ads the argument to the score when called."""
        self.score += points

    def set_name(self, new_name):
        """Change the name."""
        self.name = new_name

    def get_name(self):
        """Get the name of the object."""
        return self.name

    def get_score(self):
        """Get the score of the object."""
        return self.score
