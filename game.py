import pygame
import player
import animations
import map
import island

pygame.font.init()

display_width = 800
display_height = 600
dimensions = (display_width, display_height)
display = pygame.display.set_mode(dimensions)
center = (display_width/2, display_height/2)

water_blue = (173, 216, 230)

clock = pygame.time.Clock()

done = False

target_x = 300
target_y = 500

map_size = 50

i = island.Island(3, 1)

p = player.Player()
current_island_x = i.size/2
current_island_y = i.size/2
m = i.maps[current_island_x][current_island_y]

p.set_map(m)
p.forbidden_blocks = [0]

#put the player in the center of the map
p.x = map_size*m.pixels_per_block()/2
p.y = map_size*m.pixels_per_block()/2
p.update()

#move the player so they don't spawn in water
while p.current_block() ==0:
	p.y -= m.pixels_per_block()
	p.update()

while not done:
	caught = False
	display.fill(water_blue)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			target_x = pygame.mouse.get_pos()[0]
			target_y = pygame.mouse.get_pos()[1]
		if event.type == pygame.KEYDOWN:
			p.key_down(event)
		if event.type == pygame.KEYUP:
			p.key_up(event)


	p.update()
	
	m.draw(display, (center[0]-p.x,center[1]-p.y))
	p.draw(display, center)

	# print(p.fishing_time)
	if p.fishing_time and not p.fishing:
		animations.press_f_to_fish(display, center)
	elif p.fishing:
		animations.draw_fishing(p, display, center)

	#transport player to new map on island
	if p.transporting:
		last_x = current_island_x
		last_y = current_island_y
		current_island_x += p.next_map[0]
		current_island_y += p.next_map[1]
		m = i.maps[current_island_x][current_island_y]
		p.set_map(m)

		#move the player to the opposite side when they transport
		if p.next_map[0] == 1 or p.next_map[0] == -1:
			p.x = m.width_in_pixels()-p.x
		elif p.next_map[1] == 1 or p.next_map[1] == -1:
			p.y = m.width_in_pixels()-p.y
			if p.next_map[1] == 1:
				p.y += m.pixels_per_block()
			if p.next_map[1] == -1:
				p.y -= m.pixels_per_block()

		#correct the player's position after they transport
		while p.x >= m.width_in_pixels():
			p.x -= m.pixels_per_block()
			P.update()
		while p.y >= m.width_in_pixels():
			p.y -= m.pixels_per_block()
			p.update()
		while p.x <= 0:
			p.x += m.pixels_per_block()
			p.update()
		while p.y <= 0:
			p.y += m.pixels_per_block()
			p.update()

		#done transporting
		p.transporting = False

	if p.at_edge:
		animations.press_space_to_transport(display, center)

	# if p.fishing

	pygame.display.update()
	clock.tick(60)

pygame.quit()