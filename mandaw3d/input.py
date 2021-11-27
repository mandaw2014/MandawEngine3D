import raylibpy as rl

class Input(object):
    def __init__(self):
        self.keys = {
            "UP_ARROW":rl.KEY_UP, "DOWN_ARROW":rl.KEY_DOWN,
            "LEFT_ARROW":rl.KEY_LEFT, "RIGHT_ARROW":rl.KEY_RIGHT,

            "A":rl.KEY_A, "B":rl.KEY_B, "C":rl.KEY_C,
            "D":rl.KEY_D, "E":rl.KEY_E, "F":rl.KEY_F,
            "G":rl.KEY_G, "H":rl.KEY_H, "I":rl.KEY_I,
            "J":rl.KEY_J, "K":rl.KEY_K, "L":rl.KEY_L,
            "M":rl.KEY_M, "N":rl.KEY_N, "O":rl.KEY_O,
            "P":rl.KEY_P, "Q":rl.KEY_Q, "R":rl.KEY_R,
            "S":rl.KEY_S, "T":rl.KEY_T, "U":rl.KEY_U,
            "V":rl.KEY_V, "W":rl.KEY_W, "X":rl.KEY_X,
            "Y":rl.KEY_Y, "Z":rl.KEY_Z,

            "0":rl.KEY_ZERO, "1":rl.KEY_ONE,"2":rl.KEY_TWO,
            "3":rl.KEY_THREE, "4":rl.KEY_FOUR, "5":rl.KEY_FIVE,
            "6":rl.KEY_SIX, "7":rl.KEY_SEVEN, "8":rl.KEY_EIGHT,
            "9":rl.KEY_NINE,

            "F1":rl.KEY_F1, "F2":rl.KEY_F2, "F3":rl.KEY_F3,
            "F4":rl.KEY_F4, "F5":rl.KEY_F5, "F6":rl.KEY_F6,
            "F7":rl.KEY_F7, "F8":rl.KEY_F8, "F9":rl.KEY_F9,
            "F10":rl.KEY_F10, "F11":rl.KEY_F11, "F12":rl.KEY_F12,

            "LCTRL":rl.KEY_LEFT_CONTROL, "RCTRL":rl.KEY_RIGHT_CONTROL,
            "LSHIFT":rl.KEY_LEFT_SHIFT, "RSHIFT":rl.KEY_RIGHT_SHIFT,
            "LALT":rl.KEY_LEFT_ALT, "RALT":rl.KEY_RIGHT_ALT,

            "HOME":rl.KEY_HOME, "INSERT":rl.KEY_INSERT,
            "DELETE":rl.KEY_DELETE,
            "SPACE":rl.KEY_SPACE
        }

    def isKeyDown(self, key):
        return rl.is_key_down(key)
    
    def isKeyUp(self, key):
        return rl.is_key_up(key)
