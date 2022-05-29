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
        return KeyboardController.key == keypressed

    # if event.type == sdl2.SDL_KEYDOWN:
    #     if event.key.keysym.sym == sdl2.SDLK_UP:
    #     elif event.key.keysym.sym == sdl2.SDLK_DOWN:
    # elif event.type == sdl2.SDL_KEYUP:
    #     if event.key.keysym.sym in (sdl2.SDLK_UP, sdl2.SDLK_DOWN):