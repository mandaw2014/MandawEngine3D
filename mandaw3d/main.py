from mandaw3d.input import Input
from mandaw3d.camera import Camera
import raylibpy as rl

class Mandaw(object):
    def __init__(self, title = "Mandaw!", width = 800, height = 600, bg_color = (0, 0, 0, 255)):
        self.title = title.encode()
        self.width = width
        self.height = height
        self.bg_color = bg_color

        self.running = True

        self.fps = 60
        self.dt = rl.get_frame_time()

        rl.init_window(self.width, self.height, self.title)
        rl.set_target_fps(self.fps)

        self.draw_handlers = []
        self.update_handlers = []

        self.input = Input()

        self.camera = Camera()
        self.camera.projection = rl.CAMERA_FIRST_PERSON

        rl.set_camera_mode(self.camera.cam, rl.CAMERA_PERSPECTIVE)

    def _update(self, dt):
        for update in self.update_handlers:
            update(dt)

    def _draw(self):
        for draw in self.draw_handlers:
            draw()

    def loop(self):
        while not rl.window_should_close():
            self.dt = rl.get_frame_time()
            self._update(self.dt)
            self.dt = rl.get_frame_time()
            rl.update_camera(self.camera.cam)
            rl.begin_drawing()
            rl.clear_background((self.bg_color[0], self.bg_color[1], self.bg_color[2], self.bg_color[3]))
            rl.begin_mode3d(self.camera.cam)
            self._draw()
            rl.end_mode3d()
            rl.end_drawing()

        rl.close_window()

    def quit(self):
        self.running = False

    def update(self, fn):
        self.update_handlers.append(fn)
        return fn

    def draw(self, fn):
        self.draw_handlers.append(fn)
        return fn
