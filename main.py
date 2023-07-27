import pygame as pyg
from Blurp import Blurp
import time, random

pyg.init()

window = pyg.display.set_mode((800, 500))
clock = pyg.time.Clock()

start_time = time.time()
brotein_shakes = [Blurp([200, 200], time.time()) for i in range(30)]

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
			print(time.time() - brodie.start_time, brodie.brain.DNA)
			brotein_shakes.remove(brodie)


	pyg.display.update()
	clock.tick(60);

	if time.time() > start_time + 5:
		for brodie in brotein_shakes:
			if abs(brodie.pos[0] - 200) < 10 and abs(brodie.pos[1] - 200) < 10:
				brotein_shakes.remove(brodie)
			# elif abs(brodie.pos[0] - brodie.last_pos[0]) < 0.01 and abs(brodie.pos[1] - brodie.last_pos[1]) < 0.01:
			# 	brotein_shakes.remove(brodie)
			else:
				brodie.last_pos = brodie.pos

		baby_brotein_shakes = [Blurp([200, 200], time.time(), parents=[random.choice(brotein_shakes).brain, \
			random.choice(brotein_shakes).brain]) for _ in range(30 - len(brotein_shakes))]
		brotein_shakes += baby_brotein_shakes
		start_time = time.time()


#KU_EBEMTMSXKWNV
#KU_EBEMVMSXPWNV
#FU_DEDMSMYSPYGV
#AY_IBEQYMRXAWMV
#AU_AEEYYCVTAWFV
#AY_EBLASMVTPWWV