
from cocos.text import Label
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.director import director
from pyglet.window import key
# from collections import defaultdict


class KeyDisplay(Layer):
    is_event_handler = True

    def __init__(self):
        super(KeyDisplay, self).__init__()

        self.text = Label("", x=100, y=280 )

        # To keep track of which keys are pressed:
        self.keys_pressed = set()
        self.update_text()
        self.add(self.text)

    def on_key_press (self, key, modifiers):
        """This function is called when a key is pressed.
        'key' is a constant indicating which key was pressed.
        'modifiers' is a bitwise or of several constants indicating which
            modifiers are active at the time of the press (ctrl, shift, capslock, etc.)
        """

        self.keys_pressed.add (key)
        self.update_text()

    def on_key_release (self, key, modifiers):
        """This function is called when a key is released.

        'key' is a constant indicating which key was pressed.
        'modifiers' is a bitwise or of several constants indicating which
            modifiers are active at the time of the press (ctrl, shift, capslock, etc.)

        Constants are the ones from pyglet.window.key
        """

        self.keys_pressed.remove (key)
        self.update_text()

    def update_text(self):
        key_names = [key.symbol_string(k) for k in self.keys_pressed]
        text = 'Keys: '+','.join(key_names)
        # Update self.text
        self.text.element.text = text


class Game(Layer):
    # is_event_handler = True

    def __init__(self):
        super(Game, self).__init__()

    #     self.schedule(self.update)
    #     self.pressed = defaultdict(int)

    # def on_key_press(self, k, m):
    #     self.pressed[k] = 1
    #     print('Pressed', key.symbol_string(k))

    # def on_key_release(self, k, m):
    #     self.pressed[k] = 0
    #     print('Released', key.symbol_string(k))

    # def update(self, dt):
    #     x = self.pressed[key.RIGHT] - self.pressed[key.LEFT]
    #     print(x)


director.init(caption='Hello, Cocos',
              resizable=True,
              width=800,
              height=600)
director.run(Scene(Game(), KeyDisplay()))
