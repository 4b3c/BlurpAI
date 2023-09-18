import pygame, random, time, math
import numpy as np

sprites = {
	"north": pygame.image.load("Sprites/Blurp/BlurpNorth.png"),
	"south": pygame.image.load("Sprites/Blurp/BlurpSouth.png"),
	"east": pygame.image.load("Sprites/Blurp/BlurpEast.png"),
	"west": pygame.image.load("Sprites/Blurp/BlurpWest.png")
}

GRAY = (100, 100, 100)
RED = (250, 0, 0)


def sigmoid(z):
	return 1.0/(1.0+np.exp(-z))


class Network:
	def __init__(self, parents=None, size=[6, 4, 4]):
		self.weights = [np.random.randn(size[count], size[count + 1]) for count in range(len(size[1:]))]
		self.values = [np.zeros(row) for row in size]
		self.output = self.values[-1]

		if parents != None:
			for row in range(len(self.weights)):
				for x in range(len(self.weights[row])):
					parent_for_gene = parents[random.randint(0, 1)]
					self.weights[row][x] = parent_for_gene.genes.weights[row][x] + random.uniform(-0.05, 0.05)

	def feedforward(self, _input):
		self.values[0] = _input
		for count, weights in enumerate(self.weights):
			new_value = np.dot(self.values[count], weights)
			clamped_value = sigmoid(new_value)
			self.values[count + 1] = clamped_value

		self.output = self.values[-1]


class Blurp:
	def __init__(self, pos, parents=None):
		self.pos = pos
		self.velocity = 0
		self.direction = 1
		self.facing = "south"
		self.sprite = sprites[self.facing]
		self.ray_range = 60
		self.ray_sep = 10
		self.ray_det = [1 for i in range(6)]
		self.start_time = time.time()
		self.displacement = 0
		self.survival_time = 0
		self.fitness = 0

		self.genes = Network(parents)
	
		self.speed = 3
		self.ray_len = 10

	def turn(self, direction):
		if direction != self.facing:
			self.facing = direction
			self.sprite = sprites[self.facing]

	def move(self):
		change_x = self.speed * math.sin(math.pi * self.direction)
		change_y = self.speed * math.cos(math.pi * self.direction)
		real_change_x = (change_x * self.velocity) - (change_x * -self.velocity)
		real_change_y = (change_y * self.velocity) - (change_y * -self.velocity)
		
		self.displacement += math.sqrt(real_change_x**2 + real_change_y**2)
		self.survival_time = time.time() - self.start_time
		self.fitness = (self.displacement / 100) * (self.survival_time / 10)

		self.pos[0] += real_change_x
		self.pos[1] += real_change_y

		if self.direction < -0.75:
			self.turn("north")
		elif self.direction < -0.25:
			self.turn("west")
		elif self.direction < 0.25:
			self.turn("south")
		elif self.direction < 0.75:
			self.turn("east")
		elif self.direction < 1:
			self.turn("north")

	def think(self):
		self.genes.feedforward(self.ray_det)
		self.velocity = self.genes.output[0]
		self.direction = self.genes.output[1]

	def draw_blurp(self, window):
		ray_endpoint_pos = [[self.ray_len * math.sin(math.pi * (self.direction + offset / 100)), \
		self.ray_len * math.cos(math.pi * (self.direction + offset / 100))] for offset in range(0, 60, 10)]

		x_mid = self.pos[0] + 9
		y_mid = self.pos[1] + 13

		for count, end_point in enumerate(ray_endpoint_pos):
			if x_mid + end_point[0] * self.ray_len < 0 or x_mid + end_point[0] * self.ray_len > 800\
			or y_mid + end_point[1] * self.ray_len < 0 or y_mid + end_point[1] * self.ray_len > 500:
				color = RED
				self.ray_det[count] = 0
			else:
				color = GRAY
				self.ray_det[count] = 1
			pygame.draw.line(window, color, (x_mid, y_mid), (x_mid + end_point[0] * self.ray_len, y_mid + end_point[1] * self.ray_len))

		window.blit(self.sprite, self.pos)
		self.think()
		self.move()