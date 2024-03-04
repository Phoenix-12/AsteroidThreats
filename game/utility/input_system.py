from pynput import keyboard


class InputSystem:
    def __init__(self, on_press, on_release):
        keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        keyboard_listener.start()
