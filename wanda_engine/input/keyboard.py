from os import stat
import sdl2


class KeyboardController:
    key = None
    event = None

    @staticmethod
    def keyboard_input_listener(event):
        KeyboardController.event = event.type
        KeyboardController.key = KeyboardController.get_key(event.key.keysym.sym)
    
    @staticmethod
    def get_key(keycode):
        keymap = {
            sdl2.SDLK_UP: "up",
            sdl2.SDLK_DOWN: "down",
            sdl2.SDLK_RIGHT: "right",
            sdl2.SDLK_LEFT: "left",
            sdl2.SDLK_SPACE: "space",
        }

        try:
            return keymap[keycode]
        except KeyError:
            pass

def is_key_down(keypressed):
    if KeyboardController.event == sdl2.SDL_KEYDOWN:      
        return KeyboardController.key == keypressed

def is_key_up(keypressed):
    if KeyboardController.event == sdl2.SDL_KEYUP:        
        is_key_released = KeyboardController.key == keypressed
        KeyboardController.key = False
        return is_key_released
