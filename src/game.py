import pygame
import sys

pygame.init()
pygame.font.init()
pygame.display.set_caption("A Night in Alderhall Manor")
clock = pygame.time.Clock()
resolution = (800, 600) 
screen = pygame.display.set_mode(resolution)

class Scene:
    def __init__(self, background_path):
        self.background = pygame.image.load(background_path)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

story_states = {
    "start": {
        "text": "This is the starting scene.",
        "options": ["Go left", "Go right"],
        "next_states": ["start_goleft", "start_goright"],
        "background": "scene1"
    },
    "start_goleft": {
        "text": "You have chosen to go left!",
        "options": ["Look to the left", "Look to the right"],
        "next_states": ["goleft_lookleft", "goleft_lookright"],
        "background": "scene1"
    },
    "start_goright": {
        "text": "You have chosen to go right!\nThis is a bonus message!",
        "options": ["Look to the left", "Look to the right"],
        "next_states": ["goright_lookleft", "goright_lookright"],
        "background": "scene2"
    }
}

backgrounds = {
    "scene1": Scene("test_background1.jpg"),
    "scene2": Scene("test_background2.jpg")
}

def display_story(state):
    # screen.fill('Black')
    font = pygame.font.SysFont('Cambria Math', 24)
    text = font.render(story_states[state]["text"], True, 'White')
    screen.blit(text, (50, 50))

    options = story_states[state]["options"]
    y_offset = 150
    for i, option in enumerate(options):
        option_text = font.render(option, True, 'White')
        screen.blit(option_text, (50, y_offset + i * 50))

    pygame.display.flip()

def update_story(choice, story_states, current_state):
    state_info = story_states[current_state]
    if state_info["options"]:
        next_state = state_info["next_states"][choice]
        background = backgrounds[state_info["background"]]
        print(f"Player chose option {choice + 1}: {state_info['options'][choice]}")
        return(next_state, background)
    else:
        print("No further choices available.")
        return current_state

def main():
    running = True
    selected_index = 0
    current_state = "start"
    background = backgrounds["scene1"]
    
    while running:
        for event in pygame.event.get():
            options = story_states[current_state]["options"]
            next_states = story_states[current_state]["next_states"]
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_index = 0
                elif event.key == pygame.K_RIGHT:
                    selected_index = 1
                elif event.key == pygame.K_RETURN:
                    current_state = next_states[selected_index]
                    new_background = update_story(selected_index, story_states, current_state)
                    background = new_background[1]
        background.draw(screen)
        display_story(current_state)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()