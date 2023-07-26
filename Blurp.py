import pygame, math
from BlurpBrain import BlurpBrain

sprites = {
	"north": pygame.image.load("Sprites/Blurp/BlurpNorth.png"),
	"south": pygame.image.load("Sprites/Blurp/BlurpSouth.png"),
	"east": pygame.image.load("Sprites/Blurp/BlurpEast.png"),
	"west": pygame.image.load("Sprites/Blurp/BlurpWest.png")
}

GRAY = (100, 100, 100)
RED = (250, 0, 0)

class Blurp:
	def __init__(self, pos):
		self.pos = pos
		self.brain = BlurpBrain()
		self.facing = "south"
		self.sprite = sprites[self.facing]

		self.speed = (ord(self.brain.DNA[0]) - 65) / 2
		self.ray_len = (ord(self.brain.DNA[1]) - 65) / 2
		self.ray_sep = int((ord(self.brain.DNA[2]) - 63) / 2)
		self.ray_range = ord(self.brain.DNA[3]) - 65

		self.ray_det = [False for i in range(-self.ray_range, self.ray_range, self.ray_sep)]
		self.rays = len(self.ray_det)
		self.brain.add_rays(self.rays)


	def turn(self, direction):
		if direction != self.facing:
			self.facing = direction
			self.sprite = sprites[self.facing]

	def move(self, move, rotation):
		change_x = self.speed * math.sin(math.pi * rotation)
		change_y = self.speed * math.cos(math.pi * rotation)

		self.pos[0] += (change_x * move) - (change_x * -move)
		self.pos[1] += (change_y * move) - (change_y * -move)

		if rotation < -0.75:
			self.turn("north")
		elif rotation < -0.25:
			self.turn("west")
		elif rotation < 0.25:
			self.turn("south")
		elif rotation < 0.75:
			self.turn("east")
		elif rotation < 1:
			self.turn("north")

	def draw_blurp(self, window):
		ray_endpoint_pos = [[self.ray_len * math.sin(math.pi * (self.brain.direction + offset / 100)), self.ray_len * math.cos(math.pi * (self.brain.direction + offset / 100))]\
		 for offset in range(-self.ray_range, self.ray_range, self.ray_sep)]

		x_mid = self.pos[0] + 9
		y_mid = self.pos[1] + 13

		for count, end_point in enumerate(ray_endpoint_pos):
			if x_mid + end_point[0] * self.ray_len < 0 or x_mid + end_point[0] * self.ray_len > 800\
			or y_mid + end_point[1] * self.ray_len < 0 or y_mid + end_point[1] * self.ray_len > 500:
				color = RED
				self.ray_det[count] = True
			else:
				color = GRAY
				self.ray_det[count] = False
			pygame.draw.line(window, color, (x_mid, y_mid), (x_mid + end_point[0] * self.ray_len, y_mid + end_point[1] * self.ray_len))

		window.blit(self.sprite, self.pos)
		self.brain.think(self.ray_det)
		self.move(self.brain.move, self.brain.direction)