import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("أول قاموس للأسئلة")

# Set up the colors
background_color = (255, 255, 255)
text_color = (0, 0, 0)

# Set up the fonts
font = pygame.font.Font(None, 32)

# Set up the buttons
continents = ["أوروبا", "أمريكا الشمالية", "أمريكا الجنوبية", "أفريقيا", "آسيا", "أستراليا"]
continent_buttons = []
question_buttons = []

# Set up the main menu
main_menu = True
selected_continent = None

# Create buttons for each continent
for i, continent in enumerate(continents):
    continent_button = pygame.Rect(50, 50 + (i * 50), 200, 40)
    continent_buttons.append(continent_button)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if main_menu:
                for i, button in enumerate(continent_buttons):
                    if button.collidepoint(mouse_pos):
                        selected_continent = continents[i]
                        main_menu = False
                        # Perform action when continent button is clicked
                        print("Continent selected:", selected_continent)
                        break
            else:
                # Perform action when question button is clicked
                for button in question_buttons:
                    if button.collidepoint(mouse_pos):
                        print("Question clicked")
                        break

    # Clear the screen
    screen.fill(background_color)

    if main_menu:
        # Draw the main menu
        for i, button in enumerate(continent_buttons):
            pygame.draw.rect(screen, text_color, button)
            rendered_text = font.render(continents[i], True, text_color)
            screen.blit(rendered_text, (button.x + 5, button.y + 10))
    else:
        # Draw the question menu
        question_buttons = []
        question_menu = ["سهلة", "متوسطة", "صعبة", "رجوع"]
        for i, option in enumerate(question_menu):
            button = pygame.Rect(50, 50 + (i * 50), 200, 40)
            question_buttons.append(button)
            pygame.draw.rect(screen, text_color, button)
            rendered_text = font.render(option, True, text_color)
            screen.blit(rendered_text, (button.x + 5, button.y + 10))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()