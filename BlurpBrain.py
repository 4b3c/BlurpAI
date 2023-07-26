import random
import string

class Blurp_brain:
	def __init__(self, parents=None):
		if parents == None:
			letters = string.ascii_uppercase
			self.DNA = ''.join(random.choice(letters) for _ in range(30))


brain = Blurp_brain()
print(brain.DNA)