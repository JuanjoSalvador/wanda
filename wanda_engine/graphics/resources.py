import os
import sdl2.ext

class Resources:

    def __init__(self, resources_directory) -> None:
        self.resources = sdl2.ext.Resources(os.path.join(os.path.dirname(__file__), resources_directory))

    def get(self, file):
        return self.resources.get(file)

    def get_path(self, file):
        return self.resources.get_path(file)
