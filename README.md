# Wanda
A very experimental Python and SDL2 game framework.

Wanda is an intended reference to Monty Python's movie, *A Fish Called Wanda*.

### Goal

The main goal of this project is to build a Python framework to write simple games using SDL2. Not a complete engine, just something I can use to write simple games by myself. This is not intended to be a large project or active, just a hobby. 

### How-to basic

There should be at least two files: `main.py` and a separate file for configuration, `conf.py`

#### Configuration file

```python
title = "Hello Wanda"
w_width = 640
w_height = 480
flags = None
```

#### Main game

```python
from wanda_engine.core.game import WandaGame

class Game(WandaGame):

    def _load():
        """
        Load all necesary data before running the game. Executed ONCE, at the game start.
        """
        print("Game loaded!")

    def _update(self):
        """
        Update method. Called on every frame, update the game status and variables
        """
        print("Frame updated!")

    def _draw(self):
        """
        Draw method. Called on every frame, draw the game scene.
        """
        print("Frame drawn!")

if __name__ == "__main__":
    Game().run()
```

Finally, to run your game, just

```shell
python your-game/src/main.py
```