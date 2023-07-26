import random
import string

letters = string.ascii_uppercase

class BlurpBrain:
	def __init__(self, parents=None):
		if parents == None:
			basics = ''.join(random.choice(letters) for _ in range(4))
			self.DNA = basics + '_'
		else:
			self.DNA = ''.join(random.choice(parents[0].DNA[i] + parents[1].DNA[i] for i in range(4)))
			self.DNA += '_'
			self.DNA += ''.join(random.choice(parents[0].DNA[i] + parents[1].DNA[i] for i in range(5, len(parents[0].DNA))))


	def add_rays(self, rays):
		self.rays = rays
		self.DNA += ''.join(random.choice(letters) for _ in range(rays * 2))
		self.move = 0
		self.direction = 1

	def think(self, ray_det):
		for count, ray in enumerate(ray_det):
			ray_gene = (ord(self.DNA[4 + count]) - 65) / 6000
			self.move += int(ray) - 0.5 * ray_gene

		for count, ray in enumerate(ray_det):
			ray_gene = (ord(self.DNA[4 + self.rays + count]) - 65) / 6000
			self.direction += int(ray) - 0.5 * ray_gene

