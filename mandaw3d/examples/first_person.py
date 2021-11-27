import raylibpy
from mandaw3d import *

mandaw = Mandaw(title = "Mandaw!", width = 800, height = 600, bg_color = (245, 245, 245, 255))

mandaw.camera.type = raylibpy.CAMERA_FIRST_PERSON

ground = Entity(mandaw, model = "plane", width = 32, height = 0, length = 32, x = 0, y = 0, z = 0, color = Color(200, 200, 200, 255))

cube1 = Entity(mandaw, model = "cube", width = 1, height = 5, length = 32, x = -16, y = 2.5, z = 0, color = Color(0, 0, 255, 255))
cube2 = Entity(mandaw, model = "cube", width = 1, height = 5, length = 32, x = 16, y = 2.6, z = 0, color = Color(0, 158, 47, 255))
cube3 = Entity(mandaw, model = "cube", width = 32, height = 5, length = 1, x = 0, y = 2.5, z = 16, color = Color(255, 203, 0, 255))
cube4 = Entity(mandaw, model = "cube", width = 32, height = 5, length = 1, x = 0, y = 2.5, z = -16, color = Color(255, 0, 0, 255))

cube5 = Entity(mandaw, model = "cube", width = 1, height = 2, length = 1, x = 0, y = 1, z = 0, color = Color(0, 255, 0, 255))

@mandaw.draw
def draw():
    ground.draw()
    
    cube1.draw()
    cube2.draw()
    cube3.draw()
    cube4.draw()
    cube5.draw()

mandaw.loop()
