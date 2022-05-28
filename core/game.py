import sdl2

from core.time import Clock
from core.graphics import Graphics

class WandaGame():
    def __init__(self, title, w_width, w_height, *args, **kwargs):
        sdl2.ext.init()

        self.window = sdl2.ext.Window(title, size=(w_width, w_height), **kwargs)
        sdl2.SDL_RaiseWindow(self.window.window)
        self.window.show()

        self.clock = Clock()
        self.graphics = Graphics(self.window)

        self.running = True

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
        while self.running:
            self.clock.tick(60)
            # Get system events and update the scene
            self._parse_events()
            self._update()

            # Get scene graphic changes and refresh the screen
            self._draw()
            self.graphics.refresh_screen()

        return sdl2.ext.quit()
