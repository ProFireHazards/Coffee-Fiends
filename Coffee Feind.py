# Import the necessary modules
import pygame
import random
import time
from pygame.locals import *
import subprocess
import multiprocessing
def wait():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_f:
                return

# Initialize the game engine
pygame.init()
clockobject = pygame.time.Clock()
# Define some colors
BLUE = (175, 88, 37)
BLACK = (200, 200, 200)
WHITE = (175, 88, 37)
RED = (252, 83, 83)
pygame.mixer.init()
slurp = pygame.mixer.Sound("gulp.mp3")
angy = pygame.mixer.Sound("angy.mp3")
slurp.play()
# Set the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Create the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
# Set the title of the window
pygame.display.set_caption('Coffee Feind')
image = pygame.image.load("player.png")
imagea = pygame.image.load("c.png")
my_list = ["enemy.png"]
en = random.choice(my_list)
image2 = pygame.image.load(en)
en = random.choice(my_list)
image3 = pygame.image.load("goal.png")
# Create a player object
player = pygame.Rect(1000, 550, 80, 80)
coffee = pygame.Rect(400, 550, 80, 80)
# Create a variable to control the player's speed
player_speed = 3

# Create a list to store the player's bullets
# Create a list to store the enemies
enemies = []
temps = []
c = 0
d = 0
# Create a variable to control the enemies' speed
enemy_speed = 2
cap = enemy_speed
# Create a variable to control the rate at which enemies are spawned
spawn_rate = 30
choui = [f"{image2}"]
# Create a variable to keep track of the game clock
clock = pygame.time.Clock()
death = "n"
# Define the game loop
done = False
score=0
a = 0
# Get the list of events from the event queue
events = pygame.event.get()

# Iterate over the events
for event in events:
    # Check if the event is the QUIT event
    if event.type == pygame.QUIT:
        # If it is, set done to True to exit the game loop
        done = True

# Get the current state of the keyboard
keys = pygame.key.get_pressed()
font = pygame.font.Font("Retro Gaming.ttf", 22)
text = font.render("Press F to begin force feeding angry people coffee", True, (255, 255, 0))
screen.blit(text, [50, 50])
pygame.display.update()
wait()
def background_task(temps):
    global enemy, temp, death, enemies, enemy_speed, cap, pp, d
    for enemy in enemies:
        pygame.draw.rect(screen, BLUE, enemy)
        screen.blit(image2, enemy)
    if player.colliderect(enemy):
        death = "y"
    if coffee.colliderect(enemy):
        temps = temps
        temp = pygame.Rect(enemy.x, enemy.y, 80, 80)
        temps.append(temp)
        pygame.draw.rect(screen, WHITE, temp)
        enemies.remove(enemy)
        pp = 1
        screen.blit(imagea, temp)
        slurp.play()
        for i in range(SCREEN_WIDTH):
            clock.tick()
            screen.fill(BLUE)
            cap=cap+100
            temp.x += -1
            screen.blit(imagea, temp)
            screen.blit(image, player)
            screen.blit(image3, coffee)
            for enemy in enemies:
                screen.blit(image2, enemy)
                if enemy_speed < cap:
                    enemy_speed = enemy_speed
                if enemy.x > SCREEN_WIDTH:
                    d = d + 1
                    enemies.remove(enemy)
            pygame.display.update()
            if c is 1 or 2 or 3 or 4:
                score=score+1
            temps.remove(temp)
while not done:
    cap=cap-0.0000000000000000000000000000000000001
    epp = random.choice(choui)
    # Get the list of events from the event queue
    events = pygame.event.get()

    # Iterate over the events
    for event in events:
        # Check if the event is the QUIT event
        if event.type == pygame.QUIT:
            # If it is, set done to True to exit the game loop
            done = True

    # Get the current state of the keyboard
    keys = pygame.key.get_pressed()

    # Update the player's position based on the keys pressed
    if keys[ord('a')]:
        player.x -= player_speed
    if keys[ord('d')]:
        player.x += player_speed
    if keys[ord('w')]:
        player.y -= player_speed
    if keys[ord('s')]:
        player.y += player_speed

    # Check if the player is trying to shoot
    if keys[pygame.K_LEFT]:
        c = 1
    if keys[pygame.K_UP]:
        c = 2
    if keys[pygame.K_RIGHT]:
        c = 3
    if keys[pygame.K_DOWN]:
        c = 4
    # Check if the spawn rate counter has reached zero
    if spawn_rate == 0:
        # If so, reset the counter and spawn a new enemy
        spawn_rate = 50
        angy.play()
        enemies.append(pygame.Rect(1,random.randint(0, SCREEN_HEIGHT - 40), 80, 80))

    # Update the spawn rate counter
    spawn_rate -= 1

    # Iterate over the enemies
    for enemy in enemies:
        # Update the enemy's position
        if enemy_speed < cap:
            enemy_speed = enemy_speed
        enemy.x += enemy_speed
        if enemy.x > SCREEN_WIDTH:
            d = d + 1
            enemies.remove(enemy)

        # Check if the bullet has hit any enemies
    if d is 3:
        death = "y"
    # Fill the screen with blue
    screen.fill(BLUE)

# Draw the player on the screen
    pygame.draw.rect(screen, WHITE, coffee)
    pygame.draw.rect(screen, WHITE, player)
    screen.blit(image, player)
    screen.blit(image3, coffee)
    if c is 1:
        a = -128 + random.randint(-10, 10)
        coffee.y = player.y
        coffee.x = player.x + a
    elif c is 2:
        a = -128 + random.randint(-10, 10)
        coffee.y = player.y + a
        coffee.x = player.x
    elif c is 3:
        a = -128 + random.randint(-10, 10)
        coffee.y = player.y 
        coffee.x = player.x -a
    elif c is 4:
        a = -128 + random.randint(-10, 10)
        coffee.y = player.y - a
        coffee.x = player.x
    else:
        a = 0 + random.randint(-1, 1)
        coffee.x = player.x + a
        coffee.y = player.y + a
    # Create the process
    daemon_process = multiprocessing.Process(target=background_task)

    # Set the process as a daemon (so it will exit when the main program exits)
    daemon_process.daemon = True

    # Start the daemon process
    daemon_process.start()
# Draw the enemies on the screen
    for enemy in enemies:
        pygame.draw.rect(screen, BLUE, enemy)
        screen.blit(image2, enemy)
    font = pygame.font.Font("Retro Gaming.ttf", 22)
    text = font.render("Score: " + str(score), True, (255, 255, 0))
    if "y" in death:
        d = 0
        a = 0
        enemy_speed = 2
        cap = enemy_speed
        image2 = pygame.image.load(en)
        bullets = []
        temps = []
        enemies = []
        font = pygame.font.Font("Retro Gaming.ttf", 30)
        text = font.render("Game Over, Press F, Score: " + str(score), True, (255, 255, 0))
        screen.blit(text, [50, 50])
        pygame.display.update()
        time.sleep(2)
        bullets = []
        enemies = []
        angy.play()
        wait()
        score = 0
        player.x = 1000
        player.y = 550
        death = "n"
    screen.blit(text, [10, 10])
    pygame.display.update()
# Update the screen
    pygame.display.flip()
    c = 0
# Limit the game to 60 frames per second
    clock.tick(60)
    enemy_speed = 2
# Close the game window
pygame.quit()