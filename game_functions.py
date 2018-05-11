import sys

import pygame
def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        def check_keydown_events(event, ship):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False


def update():
    """Update the ship's position based on the movement flag."""

    if self.moving_right and self.rect.right < self.screen_rect.right:
        self.center += self.ai_settings.ship_speed_factor
        self.rect.centerx += 1
    if self.moving_left and self.rect.left > 0:
        self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx -= 1
        # Update rect object from self.center.
        self.rect.centerx = self.center


def blitme(self):
    """Draw the ship at its current location."""
    self.screen.blit(self.image, self.rect)