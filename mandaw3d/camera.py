import raylibpy as rl

class Camera(object):
    def __init__(self, position = rl.Vector3(4, 2, 4), target = rl.Vector3(0, 1.8, 0), up = rl.Vector3(0, 1, 0), fovy = 60, projection = rl.CAMERA_PERSPECTIVE):
        self.FIRST_PERSON = rl.CAMERA_FIRST_PERSON
        self.PERSPECTIVE = rl.CAMERA_PERSPECTIVE

        self.camera = rl.Camera3D(rl.Vector3(0, 0, 0))
        self.camera.position = position
        self.camera.target = target
        self.camera.up = up
        self.camera.fovy = fovy
        self.camera.projection = self.PERSPECTIVE