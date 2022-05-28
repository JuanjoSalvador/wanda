from sys import flags
import sdl2

from wanda_engine.core.time import Clock
from wanda_engine.core.graphics import Graphics

import conf

class WandaGame():
    def __init__(self):
        self.title =conf.title or "Untitled game"
        self.w_width = conf.w_width or 640
        self.w_height = conf.w_height or 480
        self.flags = conf.flags or None

        sdl2.ext.init()

        self.window = sdl2.ext.Window(self.title, size=(self.w_width, self.w_height), flags=self.flags)
        sdl2.SDL_RaiseWindow(self.window.window)
        self.window.show()

        self.clock = Clock()
        self.graphics = Graphics(self.window)

        self.running = True

    def _load(self):
        pass

    def _update(self):
        pass

    def _draw(self):
        pass

    def sprite(self, sprites):
        self.spriterenderer.render(sprites)
        
    def _parse_events(self):
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                self.running = False
                break

    def run(self):
        self._load()
        while self.running:
            self.clock.tick(60)
            # Get system events and update the scene
            self._parse_events()
            self._update()

            # Get scene graphic changes and refresh the screen
            self._draw()
            self.graphics.refresh_screen()

        return sdl2.ext.quit()