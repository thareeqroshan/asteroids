import pygame
from constants import *
from player import Player 
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
import sys

def main():
	print("Starting asteroids!")
	print("Screen width: " + str(SCREEN_WIDTH))
	print("Screen height: " + str(SCREEN_HEIGHT))
	
	dt = 0
	x = SCREEN_WIDTH/2
	y = SCREEN_HEIGHT/2

	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	Shot.containers = (updatable, drawable, shots)
	AsteroidField.containers = (updatable)

	player = Player(x, y)
	asteroidField = AsteroidField()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		
		for object in updatable:
			object.update(dt)
		
		for asteroid in asteroids:
			if player.collides_with(asteroid):
				print("Game Over!")
				sys.exit()
			for shot in shots:
				if asteroid.collides_with(shot):
					asteroid.split()
					shot.kill()
					break
		
		for object in  drawable:
			object.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60)/1000

if __name__ == "__main__":
	main()
