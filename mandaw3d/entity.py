import raylibpy as rl
from mandaw3d.math import Vector3, Vector2
from mandaw3d.color import Color 

class Entity(object):
    def __init__(self, window, model = "cube", width = 1, height = 1, length = 1, x = 0, y = 0, z = 0, color = Color(255, 255, 255, 255)):
        self.window = window
        self.model = model
        self.width = width
        self.height = height
        self.length = length
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.position = Vector3(self.x, self.y, self.z)

    def draw(self):
        if self.model == "cube":
            rl.draw_cube(self.position, self.width, self.height, self.length, self.color)
        if self.model == "plane":
            rl.draw_plane(self.position, Vector2(self.width, self.length), self.color)