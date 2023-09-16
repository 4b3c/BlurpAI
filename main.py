import pygame as pyg
from Blurp import Blurp
import time, random

pyg.init()

window = pyg.display.set_mode((800, 500))
clock = pyg.time.Clock()

start_time = time.time()
brotein_shakes = [Blurp([random.randint(100, 700), random.randint(100, 400)]) for i in range(30)]

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
		# elif brodie.pos[0] < mouse_pos[0] and brodie.pos[0] + 30 > mouse_pos[0] and brodie.pos[1] < mouse_pos[1] and brodie.pos[1] + 30 > mouse_pos[1]:
		# 	print(brodie.displacement)


	pyg.display.update()
	clock.tick(60);

	if time.time() > start_time + 10:
		for brodie in brotein_shakes:
			# print(brodie.displacement)
			if brodie.displacement < 50:
				brotein_shakes.remove(brodie)

		brotein_shakes_fitness = [shake.fitness for shake in brotein_shakes]
		print("average fitness:", sum(brotein_shakes_fitness) / len(brotein_shakes_fitness))
		baby_brotein_shakes = [Blurp([random.randint(100, 700), random.randint(100, 400)], parents=[random.choices(brotein_shakes, weights=brotein_shakes_fitness)[0],\
		random.choices(brotein_shakes, weights=brotein_shakes_fitness)[0]]) for _ in range(30)]
		# for shake in brotein_shakes:
		# 	shake.start_time, shake.displacement = time.time(), 0
		# brotein_shakes = []
		brotein_shakes += baby_brotein_shakes
		start_time = time.time()


#KU_EBEMTMSXKWNV
#KU_EBEMVMSXPWNV
#FU_DEDMSMYSPYGV
#AY_IBEQYMRXAWMV
#AU_AEEYYCVTAWFV
#AY_EBLASMVTPWWV