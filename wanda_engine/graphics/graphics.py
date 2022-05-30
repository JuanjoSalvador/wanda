import sdl2

class Graphics:
    def __init__(self, title, w_width, w_height, flags) -> None:
        self.window = sdl2.ext.Window(title, size=(w_width, w_height), flags=flags)
        sdl2.SDL_RaiseWindow(self.window.window)

        self.window.show()
        
        self.renderer = sdl2.ext.Renderer(self.window)
        self.factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=self.renderer)
        self.spriterenderer = self.factory.create_sprite_render_system(self.window)

    def present(self):
        sdl2.render.SDL_RenderPresent(self.spriterenderer.sdlrenderer)

    def render_sprite(self, sprite):
        self.spriterenderer.render(sprites=sprite)

    def load_sprite(self, sprite):
        return self.factory.from_image(sprite)

    def clear(self):
        return self.renderer.clear()