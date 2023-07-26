import random
import string

letters = string.ascii_uppercase

class BlurpBrain:
	def __init__(self, parents=None):
		if parents == None:
			basics = ''.join(random.choice(letters) for _ in range(4))
			self.DNA = basics + '_'

	def add_rays(self, rays):
		self.rays = rays
		self.DNA += ''.join(random.choice(letters) for _ in range(rays * 2)) + '_'
		self.move = 0
		self.direction = 1

	def think(self, ray_det):
		for count, ray in enumerate(ray_det):
			ray_gene = (ord(self.DNA[4 + count]) - 65) / 6000
			self.move += int(ray) - 0.5 * ray_gene

		for count, ray in enumerate(ray_det):
			ray_gene = (ord(self.DNA[4 + self.rays + count]) - 65) / 6000
			self.direction += int(ray) - 0.5 * ray_gene

