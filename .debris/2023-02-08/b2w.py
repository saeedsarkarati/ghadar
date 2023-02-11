import pygame
from pygame.locals import *
pygame.init()
                               
# -----------------



import pygame
from pygame.locals import *
pygame.init()
s = pygame.image.load("por_aab_logo.png")
s.set_at((100,100), (255,255,255) )
for i in range(s.get_width() ):
	for j in range(s.get_height() ):
		r,g, b, z = s.get_at((i, j))
		if r<20 and g<20 and b<20:
			s.set_at((i, j), (255,255,255) )


pygame.image.save(s, "por_aab_logo_w.png")
print (type (s), s.get_width())

#
