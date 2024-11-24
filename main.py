import pygame, sys, random
#from background import Background


def lose():
	global ball_speed_x, ball_speed_y, player_score, hit_sound, ball_colour, movement_multiplier
	ball_start()
	player_score -= 1
	if player_score <= 0:
		sys.exit()
		pygame.quit()

def ball_animation():
	# Ball Physics
	global ball_speed_x, ball_speed_y, player_score, hit_sound, ball_colour, movement_multiplier
	
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y *= -1	

	if ball.left <= 0: 
		lose()
		
	if ball.right >= screen_width:
		lose()

	if ball.colliderect(player) or ball.colliderect(opponent):
		if ball_colour == player_colour:
			ball_speed_x += movement_multiplier 
			ball_speed_x *= -1
			movement_multiplier -= 0.5
			print(ball_speed_x)
			hit_sound.play()
			ball_colour = random.choice([white, blue, red, green])
		else:
			lose()


def player_animation():
	opponent.y += opponent_speed
	player.y += player_speed

	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height
	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height

def ball_start():
	global ball_speed_x, ball_speed_y

	ball.center = (screen_width/2, screen_height/2)
	ball_speed_y *= random.choice([1,-1])
	ball_speed_x ==5 
	ball_speed_x *= random.choice([1,-1])


# General setup
pygame.mixer.init()
pygame.init()
clock = pygame.time.Clock()


# Main Window
screen_width = 900
screen_height = 520
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')
#BackGround = Background('background_image.png', [0,0]) 

# Colors
light_grey = (200,200,200)
white = (255,255,255)
blue = (0,0,255)
red = (255, 0, 0)
green = (0,255,0)
bg_color = pygame.Color('grey12')

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 23, 23)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,115)
opponent = pygame.Rect(10, screen_height / 2, 10,115)

# Game Variables
ball_speed_x = 5 * random.choice((1,-1))
ball_speed_y = 5 * random.choice((1,-1))
ball_colour = random.choice([white, blue, red, green])
player_colour = white
player_speed = 0
opponent_speed = 0
hit_sound = pygame.mixer.Sound('ball_hit.wav')
movement_multiplier = 0

# Score Text
player_score = 5
basic_font = pygame.font.Font('freesansbold.ttf', 32)

#Background Music
pygame.mixer.music.load("Menu Music.wav")
pygame.mixer.music.play(-1)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				player_colour = white
			if event.key == pygame.K_2:
				player_colour = blue
			if event.key == pygame.K_3:
				player_colour = red
			if event.key == pygame.K_4:
				player_colour = green
			if event.key == pygame.K_UP:
				player_speed -= 6
				opponent_speed -= 6
			if event.key == pygame.K_DOWN:
				opponent_speed += 6
				player_speed += 6
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				opponent_speed += 6
				player_speed += 6
			if event.key == pygame.K_DOWN:
				opponent_speed -= 6
				player_speed -= 6
	
	#Game Logic
	ball_animation()
	player_animation()

	# Visuals 
	screen.fill(bg_color)
	#screen.blit(BackGround.image, BackGround.rect)
	pygame.draw.rect(screen, player_colour, player)
	pygame.draw.rect(screen, player_colour, opponent)
	pygame.draw.ellipse(screen, ball_colour, ball)
	pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))

	player_text = basic_font.render(f'{player_score}',False,light_grey)
	screen.blit(player_text,(screen_width/2, 470/2))

	pygame.display.flip()
	clock.tick(100)