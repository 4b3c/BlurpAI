import pygame as pyg
from Blurp import blurp

pyg.init()

window = pyg.display.set_mode((800, 500))
clock = pyg.time.Clock()

brodie = blurp("brodie", [200, 200])

while True:
	window.fill((10, 10, 40))

	for event in pyg.event.get():
		if event.type == pyg.QUIT:
			exit()

	keys = pyg.key.get_pressed()
	mouse_pos = pyg.mouse.get_pos()

	brodie.draw_blurp(window, keys[pyg.K_w], keys[pyg.K_s], (mouse_pos[0] - 400) / 400)

	pyg.display.update()
	clock.tick(60);