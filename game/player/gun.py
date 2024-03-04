from utility.position import Position
from player import bullets


class Gun:
    _time: float = 1

    def __init__(self, fire_rate=3):
        self.fire_rate = fire_rate
        self.bullets: list[bullets.Bullet] = []

    def shoot(self, bullet_start_position: Position, speed: float) -> bool:
        if self.is_able_to_shoot():
            self.bullets.append(bullets.Bullet(bullet_start_position, add_speed=speed))
            self._time = 0


    def update(self, delta_time):
        self._time += delta_time
        for bullet in self.bullets:
            bullet.move(delta_time)

    def is_able_to_shoot(self):
        if self._time >= self.fire_rate:
            return True
        return False

