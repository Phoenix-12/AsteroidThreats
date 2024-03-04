from utility.position import *
from player.bullets import Bullet
from asteroids.asteroid import Asteroid


class CollisionSystem:
    def is_collision_player_with_asteroids(self, player_radius, player_position: Position, asteroids):
        for asteroid in asteroids:
            if player_radius + asteroid.radius > player_position.get_distance(asteroid.position):
                return True
        return False

    def is_collision_bullets_with_asteroids(self, bullets: list[Bullet], asteroids: list[Asteroid]):
        for bullet in bullets:
            for asteroid in asteroids:
                if bullet.radius + asteroid.radius > bullet.position.get_distance(asteroid.position):
                    return asteroid, bullet
        return None, None
