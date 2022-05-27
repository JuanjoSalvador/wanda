from core.game import WandaGame

class Game(WandaGame):

    def __init__(self):
        self.title = "Hello Wanda"
        self.width = 640
        self.height = 480

        super(Game, self).__init__(self.title, self.width, self.height)

    def _update(self):
        return super()._update()

    def _draw(self):
        return super()._draw()

if __name__ == "__main__":
    Game().run()