import pygame
import sys

pygame.init()
pygame.font.init()
pygame.display.set_caption("A Night in Alderhall Manor")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Cambria Math', 16)
resolution = (800, 600) 
screen = pygame.display.set_mode(resolution)

def display_text(text, x, y, font, color='Black'):
    lines = text.split('\n')
    y_offset = 0

    for line in lines:
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (x, y + y_offset))
        y_offset += text_surface.get_height()

def show_dialogue(dialogue_list, font, color='Black'):
    index = 0
    while index < len(dialogue_list):
        screen.fill('Black')
        draw_text_box(50)
        display_text(dialogue_list[index], 25, resolution[1] - 100, font, color)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or pygame.K_GREATER:
                    index += 1
                    break


def draw_text_box(y_offset, width=resolution[0]-40, height=55, color='White'):
    pygame.draw.rect(screen, color, pygame.Rect(20, resolution[1] - y_offset - height, width, height))


story = [
    "This is a short line of text.",
    "This is a longer line of text, which may have to appear as two lines on the dialogue box.",
    "This is an even longer line of text. This the maximum of how long of a text one dialogue box should contain.\nThis is testing a new line."
    ]

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        show_dialogue(story, font, 'Black')
    pygame.quit()

if __name__ == "__main__":
    main()