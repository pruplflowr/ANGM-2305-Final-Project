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
        "options": ["Option 1", "Option 2"],
        "next_states": ["option_1", "option_2"]
    },
    "option_1": {
        "text": "This is the text for option 1.",
        "options": [],
        "next_states": []
    },
    "option_2": {
        "text": "This is the text for option 2.\nThis is testing a newline.\nAnd another.",
        "options": ["Option 1", "Option 2"],
        "next_states": []
    }
}

def display_story(state):
    scene1 = Scene("test_background1.jpg")
    scene2 = Scene("test_background2.jpg")
    scene = scene1
    font = pygame.font.SysFont('Cambria Math', 24)
    scene.draw(screen)

    text = font.render(story_states[state]["text"], True, 'White')
    screen.blit(text, (50, 50))

    options = story_states[state]["options"]
    y_offset = 150
    for i, option in enumerate(options):
        option_text = font.render(option, True, 'White')
        screen.blit(option_text, (50, y_offset + i * 50))

    pygame.display.flip()

def handle_input(current_state, story_states):
    options = story_states[current_state]["options"]
    next_states = story_states[current_state]["next_states"]

    selected_index = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_index = 0
                elif event.key == pygame.K_RIGHT:
                    selected_index = 1
                elif event.key == pygame.K_RETURN:
                    return update_story(selected_index, story_states, current_state)

        display_story(current_state)

def update_story(choice, story_states, current_state):
    state_info = story_states[current_state]

    if state_info["options"]:
        next_state = state_info["next_states"][choice]
        print(f"Player chose option {choice + 1}: {state_info['options'][choice]}")
        return next_state
    else:
        print("No further choices available.")
        return current_state

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            current_state = "start"
            while True:
                current_state = handle_input(current_state, story_states) # Displays the story
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()