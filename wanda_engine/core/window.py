import sdl2.ext


class Window:
    width: int
    height: int

    def __init__(self, title, width, height, *args, **kwargs) -> None:
        sdl2.ext.init()
        self.window = sdl2.ext.Window(title, size=(width, height), **kwargs)
        sdl2.SDL_RaiseWindow(self.window.window)

    def show(self):
        self.window.show()

    def refresh(self):
        self.window.refresh()
