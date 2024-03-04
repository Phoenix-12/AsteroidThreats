
from player.Spaceship import *


from utility.position import *

FPS = 60
delta_time = 1 / FPS


class PlayerView:
    def __init__(self, height, root, canvas: tkinter.Canvas):
        self.HEIGHT = height
        self.root = root
        self.canvas = canvas
        #self.ship_png = tkinter.PhotoImage(file="./p",)
        #canvas.create_image(500, 500, image=self.ship_png)
        self.spaceship = Spaceship(self.canvas)
        self.position_UI = self.canvas.create_text(100, 100, text="---", fill="white")

        self.bullets = []



    def move(self, position: Position, radius, angle):
        self.canvas.delete(self.position_UI)
        self.position_UI = self.canvas.create_text(100, 100, text=f"{position}", fill="white")
        self.spaceship.set_spaceship(position, radius, angle)

    def start_view(self):
        #self.bg1 = tkinter.PhotoImage(file="Asteroids and the spaceship/asteroids/meteora.png", height=50, width=50)
        #self.canvas.create_image(500, 500, image=self.bg1)
        #self.spaceship.set_spaceship(Position(1, 1), 50, 1)
        pass

    def show_bullets(self, player_position, player_angle, bullets_data):
        while len(bullets_data) > len(self.bullets):
            self.bullets.append(self.canvas.create_oval(0,0,0,0, fill="white"))
        #while len(bullets_data) < len(self.bullets):
        #    self.canvas.delete(self.bullets[0])

        i = 0
        for bullet in bullets_data:
            self.set_position_bullet(player_position, player_angle, bullet.position, bullet.radius,
                                       self.bullets[i])
            i += 1

    def set_position_bullet(self, player_position, player_angle, position, radius, bullet):
        dist = position.get_distance(player_position)
        if dist == 0:
            dist = 1
        delta_x = (position.x - player_position.x)
        delta_y = (position.y - player_position.y)

        if delta_y > 0:
            position = Position(dist * cos(-pi / 2 - player_angle + acos(delta_x / dist)),
                                dist * sin(-pi / 2 - player_angle + acos(delta_x / dist)))
        elif delta_y <= 0:
            position = Position(dist * cos(-pi / 2 - player_angle - acos(delta_x / dist)),
                                dist * sin(-pi / 2 - player_angle - acos(delta_x / dist)))

        delta_view = self.HEIGHT / 2
        self.canvas.coords(bullet, position.x - radius + delta_view, position.y - radius + delta_view,
                           position.x + radius + delta_view, position.y + radius + delta_view)

#
# class AsteroidView:
#     def __init__(self, height, root, canvas: tkinter.Canvas):
#         self.HEIGHT = height
#         self.root = root
#         self.canvas = canvas
#         # self.meteora_pict = tkinter.Image()
#         #self.l = tkinter.Label(image=self.meteora_pict)
#         #self.l.grid(row=0, column=0)
#         self.view_asteroids = [canvas.create_oval(*[-1 for _ in range(4)], fill="red") for _ in range(50)]
#
#     def set_position(self, player_position, player_angle, asteroids):
#         i = 0
#         for asteroid in asteroids:
#             i += 1
#             self.set_position_asteroid(player_position, player_angle, asteroid.position, asteroid.radius,
#                                        self.view_asteroids[i])
#
#     def set_position_asteroid(self, player_position, player_angle, position, radius, view_asteroid):
#         dist = position.get_distance(player_position)
#         delta_x = (position.x - player_position.x)
#         delta_y = (position.y - player_position.y)
#
#         if delta_y > 0:
#             position = Position(dist * cos(-pi/2 - player_angle + acos(delta_x / dist)),
#                                 dist * sin(-pi/2 - player_angle + acos(delta_x / dist)))
#         elif delta_y <= 0:
#             position = Position(dist * cos(-pi / 2 - player_angle - acos(delta_x / dist)),
#                                 dist * sin(-pi / 2 - player_angle - acos(delta_x / dist)))
#
#         delta_view = self.HEIGHT / 2
#         self.canvas.coords(view_asteroid, position.x - radius + delta_view, position.y - radius + delta_view,
#                            position.x + radius + delta_view, position.y + radius + delta_view)