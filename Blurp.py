import pygame, math

sprites = {
	"north": pygame.image.load("Sprites/Blurp/BlurpNorth.png"),
	"south": pygame.image.load("Sprites/Blurp/BlurpSouth.png"),
	"east": pygame.image.load("Sprites/Blurp/BlurpEast.png"),
	"west": pygame.image.load("Sprites/Blurp/BlurpWest.png")
}

GRAY = (100, 100, 100)

class blurp:
	def __init__(self, name, pos):
		self.name = name
		self.pos = pos
		self.facing = "south"
		self.sprite = sprites[self.facing]
		self.speed = 2
		self.ray_len = 9


	def turn(self, direction):
		if direction != self.facing:
			self.facing = direction
			self.sprite = sprites[self.facing]


	def move_with_directions(self, north, south, east, west):
		if north:
			self.pos[1] -= self.speed
			self.turn("north")
		if south:
			self.pos[1] += self.speed
			self.turn("south")
		if east:
			self.pos[0] += self.speed
			self.turn("east")
		if west:
			self.pos[0] -= self.speed
			self.turn("west")


	def move_with_rotation(self, move, rotation):
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

	def draw_blurp(self, window, speed, rotation):
		self.move_with_rotation(speed, rotation)

		ray_endpoint_pos = [[self.ray_len * math.sin(math.pi * (rotation + offset / 100)), self.ray_len * math.cos(math.pi * (rotation + offset / 100))] for offset in range(-18, 18, 4)]

		x_mid = self.pos[0] + 9
		y_mid = self.pos[1] + 13

		for end_point in ray_endpoint_pos:
			pygame.draw.line(window, GRAY, (x_mid, y_mid), (x_mid + end_point[0] * self.ray_len, y_mid + end_point[1] * self.ray_len))

		window.blit(self.sprite, self.pos)