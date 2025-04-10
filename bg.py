import pygame
pygame.init()
Width, Height = 500, 500

surface = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Adding bg image and image')

bg_image = pygame.transform.scale(pygame.image.load('bg.jpg').convert(), (Width, Height))

dog_image = pygame.transform.scale(pygame.image.load('dog.png')._alpha(), (200, 200))
dog_rect = dog_image.get_rect(center = (Width // 2, Height // 2 - 30))

text = pygame.font.Font(None, 36).render('Hello World!', True, pygame.color('black'))
text_rect = dog_image.get_rect(center = (Width // 2, Height // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        surface.blit(bg_image, (0, 0))
        surface.blit(dog_image, dog_rect)
        surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()