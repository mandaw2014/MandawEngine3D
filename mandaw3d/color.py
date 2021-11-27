import raylibpy as rl

class Color(rl.Color):
    def __init__(self, r, g, b, a = 255):
        super().__init__(
            r, g, b, a
        )