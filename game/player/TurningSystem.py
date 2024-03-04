class TurningSystem:
    _direction = 0
    is_left = False
    is_right = False
    is_braking = False

    def get_direction(self):
        return self._direction

    def press_left(self):
        if not self.is_left:
            self._direction -= 1
            self.is_left = True

    def press_right(self):
        if not self.is_right:
            self._direction += 1
            self.is_right = True

    def press_brake(self):
        self.is_braking = True

    def release_brake(self):
        self.is_braking = False

    def release_left(self):
        self.is_left = False
        self._direction += 1

    def release_right(self):
        self.is_right = False
        self._direction -= 1
