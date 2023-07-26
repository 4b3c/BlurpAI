import pygame as pyg
from Blurp import Blurp
import time

pyg.init()

window = pyg.display.set_mode((800, 500))
clock = pyg.time.Clock()

brotein_shakes = [Blurp([200, 200]) for i in range(30)]
start_time = time.time()
print(start_time)

while True:
	window.fill((10, 10, 40))

	for event in pyg.event.get():
		if event.type == pyg.QUIT:
			exit()

	keys = pyg.key.get_pressed()
	mouse_pos = pyg.mouse.get_pos()

	for brodie in brotein_shakes:
		brodie.draw_blurp(window)
		if brodie.pos[0] < 0 or brodie.pos[0] > 800 or brodie.pos[1] < 0 or brodie.pos[1] > 500:
			brotein_shakes.remove(brodie)

	pyg.display.update()
	clock.tick(60);