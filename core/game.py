import sdl2

from core.time import Clock
from core.window import Window


class WandaGame:
    def __init__(self, title, w_width, w_height):
        self.window = Window(title, w_width, w_height)
        self.clock = Clock()

        self.window.show()
        self.running = True

    def _update(self):
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                self.running = False
                break

    def _draw(self):
        self.window.refresh()

    def run(self):
        """
        """

        while self.running:
            self.clock.tick(60)
            self._update()
            self._draw()

        return sdl2.ext.quit()
