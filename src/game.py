import pygame

def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("A Night in Alderhall Manor")
    clock = pygame.time.Clock()
    # dt = 0
    resolution = (800, 600) 
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('Black')
        pygame.display.flip()
        # dt = clock.tick(12)
    pygame.quit()

if __name__ == "__main__":
    main()