import sdl2

class Graphics:
    def __init__(self, window) -> None:
        self.renderer = sdl2.ext.Renderer(window)
        self.factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=self.renderer)
        self.spriterenderer = self.factory.create_sprite_render_system(window)

    def refresh_screen(self):
        self.renderer.clear()
        sdl2.render.SDL_RenderPresent(self.spriterenderer.sdlrenderer)

    def render_sprite(self, sprite):
        return self.spriterenderer.render(sprites=sprite)