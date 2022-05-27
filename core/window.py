import sdl2.ext


class Window:
    width: int
    height: int

    def __init__(self, title, width, height, *args, **kwargs) -> None:
        sdl2.ext.init()
        self.window = sdl2.ext.Window(title, size=(width, height), **kwargs)

    def show(self):
        self.window.show()

    def refresh(self):
        self.window.refresh()
