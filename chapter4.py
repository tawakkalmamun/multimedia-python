import pygame
pygame.init()

# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")
image = pygame.image.load('wan.png')

# Loop utama permainan
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            screen.blit(image, (100, 100))

        sound = pygame.mixer.Sound('example.wav')

        # Memutar suara
        sound.play()

    # Memperbarui tampilan
    pygame.display.flip()

    