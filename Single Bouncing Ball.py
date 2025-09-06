import random
import pygame

(width, height) = (640, 1000)
screen = pygame.display.set_mode((width, height))
screen.fill((255,255,255))

pygame.display.flip()

clock = pygame.time.Clock()

radius = 30
balls = 10
fps = 60
gravity = 1000/3600 # pixels/fps^2

speed_flag = True
energy_loss = 0.75
wind_loss = 0.003
falling = True
bouncing = True
running = True

def initial_state():
    x = random.randint(radius, width-radius)
    y = random.randint(radius, radius+100)
    speed = random.randrange(2, 10)
    wind = random.randrange(2, 5)
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    return(x, y, speed, wind, color)

x, y, speed, wind, color = initial_state()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                x, y, speed, wind, color = initial_state()
                speed_flag = True
                energy_loss = 0.75
                wind_loss = 0.003
                falling = True
                bouncing = True
                running = True
            elif event.key == pygame.K_q:
                running = False
                
    screen.fill((255,255,255))
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.draw.circle(screen, color, (x, y), radius)
    
    if falling:
        y += speed
        speed += gravity
    
    if bouncing:
        x += wind

    if wind < 0:
        wind += wind_loss
    elif wind > 0:
        wind -= wind_loss

    if abs(wind) <= 0.01:
        wind = 0
        bouncing = False

    if int(x) > width-radius:
        x = width-radius
        wind -= 0.2
        wind *= -1
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    if  int(x) < radius:
        x = radius
        wind += 0.2
        wind *= -1
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))

    if int(y) > height-radius:
        y = height-radius
        speed = (speed*energy_loss)*(-1)
        if abs(speed) < 2:
            speed = 0
            falling = False
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))

    pygame.display.update()
    clock.tick(fps)

pygame.quit()