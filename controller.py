import pygame
from cat import Cat
from obstacle import Obstacle

class Controller:
    def __init__(self):
        """
        Initializes the Controller object
        """
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Cat Game")
        self.clock = pygame.time.Clock()

        self.cat = Cat(100, 300, "cat.png")
        self.obstacles = []

    def mainloop(self):
        """
        Main loop of the game
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.update_models()

            self.redraw()

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()

    def update_models(self):
        """
        Detects collisions and updates models
        """
        pass

    def redraw(self):
        """
        Redraws the next frame
        """
        pass

if __name__ == "__main__":
    controller = Controller()
    controller.mainloop()