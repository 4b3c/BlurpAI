import pygame, math

sprites = {
	"north": pygame.image.load("Sprites/Blurp/BlurpNorth.png"),
	"south": pygame.image.load("Sprites/Blurp/BlurpSouth.png"),
	"east": pygame.image.load("Sprites/Blurp/BlurpEast.png"),
	"west": pygame.image.load("Sprites/Blurp/BlurpWest.png")
}

class blurp:
	def __init__(self, name, pos):
		self.name = name
		self.pos = pos
		self.facing = "south"
		self.sprite = sprites[self.facing]
		self.speed = 5

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

	def move_with_rotation(self, forward, backward, rotation):
qqqqq
		self.pos[1] += self.speed * forward * math.cos(math.pi * rotation)
		self.pos[0] += self.speed * forward * math.sin(math.pi * rotation)


	def draw_blurp(self, window, forward, backward, rotation):
		self.move_with_rotation(int(forward), int(backward), rotation)

		window.blit(self.sprite, self.pos)