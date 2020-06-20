from noise import snoise2
import pygame

width = 1280
height = 720
window = pygame.display.set_mode((width, height))


class GameMap(object):
    def __init__(self, map_width, map_height):
        self.block_size = 8
        self.map_height = map_height // self.block_size
        self.map_width = map_width // self.block_size
        self.scl = 0.1

    def create(self):
        f = open('game.txt', 'w')
        xcor = []
        for y in range(self.map_height):
            ycor = []
            for x in range(self.map_width):
                val = int(abs(snoise2(x * self.scl, y * self.scl) * 255))
                ycor.append(val)
            xcor.append(ycor)
        f.write(str(xcor))
        f.close()
        return xcor

    def draw(self, garr):
        xcor = 0
        for x in garr:
            ycor = 0
            for y in x:
                if 0 <= int(y) <= 50:  # water
                    pygame.draw.rect(window, (0, 0, 255),
                                     (xcor, ycor, self.block_size, self.block_size))
                elif 50 < int(y) <= 100:  # sand
                    pygame.draw.rect(window, (255, 255, 154),
                                     (xcor, ycor, self.block_size, self.block_size))
                elif 100 < int(y) <= 150:  # grass
                    pygame.draw.rect(window, (0, 255, 0),
                                     (xcor, ycor, self.block_size, self.block_size))
                elif 150 < int(y) <= 200:  # stone
                    pygame.draw.rect(window, (int(y), int(y), int(y)),
                                     (xcor, ycor, self.block_size, self.block_size))
                elif 200 < int(y) <= 255:  # snow
                    pygame.draw.rect(window, (255, 255, 255),
                                     (xcor, ycor, self.block_size, self.block_size))
                ycor += self.block_size
            xcor += self.block_size


game_map = GameMap(height, width)
gmap = game_map.create()

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
            quit()

    game_map.draw(gmap)
    pygame.display.update()
