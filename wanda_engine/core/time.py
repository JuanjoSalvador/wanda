import math
from sdl2 import SDL_Delay, SDL_GetTicks


__all__ = ('Clock', 'wait', 'delay', 'get_time', 'get_delta')


def wait(milliseconds):
    start = SDL_GetTicks()
    SDL_Delay(int(milliseconds))
    return SDL_GetTicks() - start


def delay(milliseconds):
    return wait(milliseconds)


def get_time():
    return SDL_GetTicks()


def get_delta(t0):
    return SDL_GetTicks() - t0


class Clock:

    def __init__(self):
        self.last = SDL_GetTicks()
        self.last_frames = []
        self.frametime = 0
        self.raw_frametime = 0

    def tick(self, framerate=0):
        now = SDL_GetTicks()
        self.raw_frametime = now - self.last
        while len(self.last_frames) > 9:
            self.last_frames.pop(0)
        if framerate == 0:
            self.last = now
            self.last_frames.append(self.raw_frametime)
            return self.raw_frametime
        frame_duration = 1.0 / framerate * 1000
        if self.raw_frametime < frame_duration:
            delay(frame_duration - self.raw_frametime)
        now = SDL_GetTicks()
        self.frametime = now - self.last
        self.last = now
        self.last_frames.append(self.frametime)
        return self.frametime

    def tick_busy_loop(self, framerate=0):
        return self.tick(framerate)

    def get_time(self):
        return self.frametime

    def get_rawtime(self):
        return self.raw_frametime

    def get_fps(self):
        total_time = sum(self.last_frames)
        average_time = total_time / 1000.0 / len(self.last_frames)
        average_fps = 1.0 / average_time
        return 0 if math.isnan(average_fps) else average_fps
