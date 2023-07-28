class Settings:
    """A class to store all the settings"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_colour = (230, 230, 230)
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (230, 0, 0)
        self.max_bullets = 3
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

