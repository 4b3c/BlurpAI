import pygame
import numpy as np

def sigmoid(z):
	return 1.0/(1.0+np.exp(-z))

class Network:
	def __init__(self, size=[6, 4, 2]):
		self.weights = [np.random.randn(size[count], size[count + 1]) for count in range(len(size[1:]))]
		self.values = [np.zeros(row) for row in size]
		self.output = self.values[-1]

	def feedforward(self, _input):
		self.values[0] = _input
		for count, weights in enumerate(self.weights):
			new_value = np.dot(self.values[count], weights)
			clamped_value = sigmoid(new_value)
			self.values[count + 1] = clamped_value

		self.output = self.values[-1]




class Blurp:
	def __init__(self, pos, parents=None):
		pass






bean = Network()
# for weights in bean.weights:
# 	print(weights)

bean.feedforward([1, 1, 0, 0, 0, 0])

print(bean.output)