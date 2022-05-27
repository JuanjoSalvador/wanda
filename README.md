# Wanda
A very experimental Python and SDL2 game framework.

Wanda is an intended reference to Monty Python's movie, *A Fish Called Wanda*.

### Goal

The main goal of this project is to build a Python framework to write simple games using SDL2. Not a complete engine, just something I can use to write simple games by myself. This is not intended to be a large project or active, just a hobby. 

### Example

```python
from core.game import WandaGame

class Game(WandaGame):

    def __init__(self):
        self.title = "Hello Wanda"
        self.width = 640
        self.height = 480

        super(Game, self).__init__(self.title, self.width, self.height)

    def _update(self):
        """
        Update method. Called on every frame, update the game status and variables
        """
        print("Frame updated!")
        super()._update()

    def _draw(self):
        """
        Draw method. Called on every frame, draw the game scene.
        """
        print("Frame drawn!")
        super()._draw()

if __name__ == "__main__":
    Game().run()
```