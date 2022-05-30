import sdl2
import sdl2.ext
import conf

from wanda_engine.core.time import Clock
from wanda_engine.graphics import Graphics
from wanda_engine.input.keyboard import KeyboardController


class Wanda():
    running: bool = True

    def __init__(self) -> None:
        sdl2.ext.init()
        self.clock = Clock()

        self.title = conf.title or "Untitled game"
        self.w_width = conf.w_width or 640
        self.w_height = conf.w_height or 480
        self.flags = conf.flags or None

        Wanda.graphics = Graphics(
            self.title, self.w_width, self.w_height, self.flags)

    @staticmethod
    def parse_events():
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                Wanda.running = False
                break

            if event.type in (sdl2.SDL_KEYDOWN, sdl2.SDL_KEYUP):
                KeyboardController.keyboard_input_listener(event)


class WandaGame(Wanda):

    def load(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        self.load()
        while self.running:
            self.clock.tick(60)
            # Get system events and update the scene
            Wanda.parse_events()
            self.update()

            # Get scene graphic changes and refresh the screen
            Wanda.graphics.clear()
            self.draw()

        return sdl2.ext.quit()
