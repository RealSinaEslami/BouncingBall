import random
import pygame

# Initialize pygame
pygame.init()

(width, height) = (640, 1000)
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))
pygame.display.flip()
clock = pygame.time.Clock()
fps = 60

title_font = pygame.font.SysFont('Arial', 60, bold=True)
subtitle_font = pygame.font.SysFont('Arial', 30)

class Ball:
    def __init__(self, radius):
        self.radius = radius
        self.x = random.randint(radius, width - radius)
        self.y = random.randint(radius, radius + 300)
        self.speed = random.randrange(2, 10)
        self.wind = random.randrange(2, 5)
        self.gravity = (1000 / 3600) * radius/30
        self.energy_loss = 0.75
        self.wind_loss = 0.003
        self.falling = True
        self.bouncing = True
        self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    
    def update(self):
        if self.falling:
            self.y += self.speed
            self.speed += self.gravity
        
        if self.bouncing:
            self.x += self.wind

        if self.wind < 0:
            self.wind += self.wind_loss
        elif self.wind > 0:
            self.wind -= self.wind_loss

        if abs(self.wind) <= 0.01:
            self.wind = 0
            self.bouncing = False

        if self.x > (width - self.radius):
            self.x = width - self.radius
            self.wind -= 0.2
            self.wind *= -1
            self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        
        if self.x < self.radius:
            self.x = self.radius
            self.wind += 0.2
            self.wind *= -1
            self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

        if self.y > (height - self.radius):
            self.y = height - self.radius
            self.speed = (self.speed * self.energy_loss) * (-1)
            if abs(self.speed) < 2:
                self.speed = 0
                self.falling = False
            self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Create balls
num_balls = 10
balls = [Ball(radius=random.randrange(10, 30)) for _ in range(num_balls)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Reset all balls
                balls = [Ball(radius=random.randrange(10, 30)) for _ in range(num_balls)]
            elif event.key == pygame.K_q:
                running = False
    
    screen.fill((255, 255, 255))
    
    # Update and draw all balls
    for ball in balls:
        ball.update()
        ball.draw()
        
    # Draw title text (behind the balls)
    title_text = title_font.render("Bouncing Balls!", True, (0, 0, 0))
    subtitle_text = subtitle_font.render("Press R to reset, Q to quit", True, (255, 0, 0))
    
    # Center the title text
    title_rect = title_text.get_rect(center=(width/2, height/3-200))
    subtitle_rect = subtitle_text.get_rect(center=(width/2, height/3 -140))
    
    screen.blit(title_text, title_rect)
    screen.blit(subtitle_text, subtitle_rect)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()