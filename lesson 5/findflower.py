import pygame
from random import randint

# Initialize pygame
pygame.init()

# Set up display
WIDTH = 600
HEIGHT = 400
TITLE = "BumbleBee and Flower"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Colors
black = (0, 0, 0)

# Load images
bee_img = pygame.image.load("images/bee.png")
flower_img = pygame.image.load("images/flower.png")
background_img = pygame.image.load("C:/Users/rmeri/OneDrive/Documents/python game develpoment 1/lesson 5/images/backround.png")

# Define game variables
score = 0
gameover = False

# Bee and Flower positions
bee_x, bee_y = 100, 100
flower_x, flower_y = 200, 200

# Clock to control the frame rate
clock = pygame.time.Clock()

def place_flower():
    global flower_x, flower_y
    flower_x = randint(70, WIDTH - 70)
    flower_y = randint(70, HEIGHT - 70)

def times_up():
    global gameover
    gameover = True

def draw():
    global gameover, score, bee_x, bee_y, flower_x, flower_y

    screen.blit(background_img, (0, 0))
    
    screen.blit(bee_img, (bee_x, bee_y))
    screen.blit(flower_img, (flower_x, flower_y))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    if gameover:
        gameover_text = font.render(f"Time's up, Your Final Score Is {score}", True, (0, 255, 0))
        screen.fill((255, 0, 0))  
        screen.blit(gameover_text, (WIDTH // 2 - gameover_text.get_width() // 2, HEIGHT // 2 - 20))
        pygame.display.update()  
        pygame.time.delay(3000)  
        pygame.quit()  

def update():
    global bee_x, bee_y, score, flower_x, flower_y

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        bee_x -= 2
    if keys[pygame.K_RIGHT]:
        bee_x += 2
    if keys[pygame.K_UP]:
        bee_y -= 2
    if keys[pygame.K_DOWN]:
        bee_y += 2

    if (bee_x < flower_x + 50 and bee_x + 50 > flower_x) and (bee_y < flower_y + 50 and bee_y + 50 > flower_y):
        score += 10
        place_flower()

def main():
    global gameover
    start_ticks = pygame.time.get_ticks() 
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
        update()
        draw()
        if pygame.time.get_ticks() - start_ticks > 60000:  # 60 seconds = 60000 milliseconds
            times_up()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
