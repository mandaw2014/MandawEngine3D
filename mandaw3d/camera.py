import raylibpy as rl

class Camera(object):
    def __init__(self, position = rl.Vector3(4, 2, 4), target = rl.Vector3(0, 1.8, 0), up = rl.Vector3(0, 1, 0), fovy = 60, projection = rl.CAMERA_PERSPECTIVE):
        self.FIRST_PERSON = rl.CAMERA_FIRST_PERSON
        self.PERSPECTIVE = rl.CAMERA_PERSPECTIVE

        self.cam = rl.Camera()
        self.cam.position = position
        self.cam.target = target
        self.cam.up = up
        self.cam.fovy = fovy
        self.cam.projection = self.PERSPECTIVE