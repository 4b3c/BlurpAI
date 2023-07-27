import random
import string

letters = string.ascii_uppercase

class BlurpBrain:
	def __init__(self, parents=None):
		if parents == None:
			basics = ''.join(random.choice(letters) for _ in range(2))
			responses = ''.join(random.choice(letters) for _ in range(12))
		else:
			basics = ''.join(random.choice(parents[0].DNA[i] + parents[1].DNA[i] + parents[0].DNA[i] + parents[1].DNA[i] + parents[0].DNA[i] + parents[1].DNA[i] + \
				random.choice(letters)) for i in range(2))
			responses = ''.join(random.choice(parents[0].DNA[i] + parents[1].DNA[i] + parents[0].DNA[i] + parents[1].DNA[i] + parents[0].DNA[i] + parents[1].DNA[i] + \
				random.choice(letters)) for i in range(3, 15))

		self.DNA = basics + '_' + responses
		self.move = 0
		self.direction = 1

	def think(self, ray_det):
		for count, ray in enumerate(ray_det):
			ray_gene = (ord(self.DNA[2 + count]) - 65 - 13) / 10000
			self.move += (int(ray) - 0.5) * ray_gene

		for count, ray in enumerate(ray_det):
			ray_gene = (ord(self.DNA[2 + 6 + count]) - 65 - 13) / 10000
			self.direction += (int(ray) - 0.5) * ray_gene


# mom = BlurpBrain()
# dad = BlurpBrain()

# child = BlurpBrain([mom, dad])

# print(mom.DNA)
# print(dad.DNA)
# print(child.DNA)

# child.think([False, False, False, True, False, True])
# print(child.move, child.direction)