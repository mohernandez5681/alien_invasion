class Settings:
    """A class to store all settings for the game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 700
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Raindrop settings
        self.raindrop_speed = 0.5