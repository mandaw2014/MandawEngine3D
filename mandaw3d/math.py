from raylibpy import Vector3, Vector2

class Vector3(Vector3):
    def __init__(self, value_1, value_2, value_3):
        super().__init__(
            value_1,
            value_2,
            value_3
        )

class Vector2(Vector2):
    def __init__(self, value_1, value_2):
        super().__init__(
            value_1,
            value_2
        )