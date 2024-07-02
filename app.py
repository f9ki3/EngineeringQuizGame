import pygame
import sys
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize mixer module for sound

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Engineering Quizbee')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)       # Orange color RGB value
LIGHT_ORANGE = (255, 200, 0)  # Lighter shade of orange for hover effect
GREEN = (0, 255, 0)           # Green color RGB value


# Load background image
background_image = pygame.image.load('background.jpg')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Load sound images
sound_on_image = pygame.image.load('sound_on.png')
sound_off_image = pygame.image.load('sound_off.png')
sound_on_image = pygame.transform.scale(sound_on_image, (40, 40))
sound_off_image = pygame.transform.scale(sound_off_image, (40, 40))

# Create a surface for dimming effect
dim_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
dim_surface.fill((0, 0, 0, 200))  # Adjust the alpha value (0-255) for dimming effect

# Font sizes
menu_title_font_size = 72
menu_button_font_size = 36
quiz_title_font_size = 28
quiz_button_font_size = 28

# Fonts
menu_title_font = pygame.font.Font(None, menu_title_font_size)  # Larger font size for the menu title
menu_button_font = pygame.font.Font(None, menu_button_font_size)  # Font size for menu buttons
quiz_title_font = pygame.font.Font(None, quiz_title_font_size)  # Font size for quiz questions
quiz_button_font = pygame.font.Font(None, quiz_button_font_size)  # Font size for quiz options

# Load and play track.mp3
pygame.mixer.music.load('track.mp3')
pygame.mixer.music.play(-1)  # -1 loops the music indefinitely

# Load sounds
click_sound = pygame.mixer.Sound('gamestart.mp3')

# Define quiz questions globally
quiz_questions = [
    {
        "question": "What is the purpose of a retaining wall in civil engineering?",
        "options": ["A. To prevent soil erosion", "B. To support vertical or near-vertical grade changes",
                    "C. To filter water contaminants", "D. To increase soil fertility"],
        "correct_answer": "B"
    },
    {
        "question": "Which material is commonly used as a binder in asphalt concrete?",
        "options": ["A. Cement", "B. Sand", "C. Bitumen", "D. Gravel"],
        "correct_answer": "C"
    },
    {
        "question": "What is the primary function of a geotechnical engineer?",
        "options": ["A. Designing bridges", "B. Analyzing traffic flow", "C. Assessing soil properties",
                    "D. Constructing buildings"],
        "correct_answer": "C"
    },
    {
        "question": "What does the term 'LEED' refer to in sustainable building practices?",
        "options": ["A. Low-energy environmental design", "B. Leadership in Energy and Environmental Design",
                    "C. Lean engineering and ecological development", "D. Long-term ecological efficiency design"],
        "correct_answer": "B"
    },
    {
        "question": "In reinforced concrete design, what does the term 'rebar' stand for?",
        "options": ["A. Retractable bar", "B. Reinforcing bar", "C. Resilient binder", "D. Reusable block"],
        "correct_answer": "B"
    }
]

# Game variables
score = 0
lives = 3
current_question = 0

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.centerx = x
    textrect.top = y  # Adjusted to set the top position instead of centery
    surface.blit(textobj, textrect)

def draw_rounded_rect(surface, color, rect, radius=20, image=None):
    pygame.draw.rect(surface, color, rect, border_radius=radius)
    if image:
        surface.blit(image, (rect.x + rect.width // 2 - image.get_width() // 2, rect.y + rect.height // 2 - image.get_height() // 2))

def check_button_hover(button_rect):
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        return True
    return False

def start_game():
    global score, lives, current_question
    
    # Reset game variables
    score = 0
    lives = 3
    current_question = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Return to main menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button click
                    # Check if an option was clicked
                    check_answer_click()

        # Check if game over
        if lives <= 0 or current_question >= len(quiz_questions):
            return  # Return to main menu
        
        # Clear the screen
        screen.blit(background_image, (0, 0))
        screen.blit(dim_surface, (0, 0))

        # Display current question and options
        display_question(quiz_questions[current_question])
        
        # Display score and lives
        display_stats()
        
        # Update the display
        pygame.display.update()

def display_question(question_data):
    question_text = question_data["question"]
    options = question_data["options"]
    
    # Calculate maximum width for text wrapping
    max_width = 600  # Maximum width before wrapping
    wrapped_lines = []
    font = quiz_title_font
    words = question_text.split()
    accumulated_width = 0
    current_line = []
    
    # Split text into lines based on max_width
    for word in words:
        word_surface = font.render(word, True, WHITE)  # Render in white color
        word_width = word_surface.get_width()
        
        if accumulated_width + word_width <= max_width:
            current_line.append(word)
            accumulated_width += word_width + font.size(" ")[0]  # Add space width
        else:
            wrapped_lines.append(" ".join(current_line))
            current_line = [word]
            accumulated_width = word_width + font.size(" ")[0]  # Add space width
    
    # Append the last line
    if current_line:
        wrapped_lines.append(" ".join(current_line))
    
    # Calculate box size and position
    box_padding = 20
    line_height = font.get_linesize()
    box_width = max_width + box_padding * 2
    box_height = len(wrapped_lines) * line_height + box_padding * 2
    box_x = (screen_width - box_width) // 2
    box_y = 120 - box_padding  # Offset to center vertically with padding
    
    # Draw rounded rectangle background
    pygame.draw.rect(screen, ORANGE, (box_x, box_y, box_width, box_height), border_radius=20)
    
    # Render wrapped lines
    y = box_y + box_padding
    for line in wrapped_lines:
        draw_text(line, quiz_title_font, WHITE, screen, screen_width // 2, y)
        y += line_height
    
    # Render options as clickable buttons
    option_y = screen_height // 2
    option_offset = 40
    for option in options:
        option_render = quiz_button_font.render(option, True, ORANGE)  # Default color is orange
        option_rect = option_render.get_rect(center=(screen_width // 2, option_y))
        
        # Check if mouse is hovering over the option
        if option_rect.collidepoint(pygame.mouse.get_pos()):
            option_render = quiz_button_font.render(option, True, GREEN)  # Change color to green when hovering
        
        screen.blit(option_render, option_rect)
        option_y += option_offset


def check_answer_click():
    global score, lives, current_question
    
    mouse_pos = pygame.mouse.get_pos()
    clicked_option = None
    
    # Check which option was clicked
    option_y = screen_height // 2
    option_offset = 40
    for i, option in enumerate(quiz_questions[current_question]["options"]):
        option_rect = pygame.Rect(screen_width // 2 - 150, option_y - 20, 300, 30)
        if option_rect.collidepoint(mouse_pos):
            clicked_option = option
            break
        option_y += option_offset
    
    if clicked_option is not None:
        # Check if the clicked answer is correct
        if clicked_option.startswith(quiz_questions[current_question]["correct_answer"]):
            score += 1
        else:
            lives -= 1
        
        # Move to the next question
        current_question += 1

def display_stats():
    score_text = f"Score: {score}"
    lives_text = f"Lives: {lives}"
    
    score_render = menu_button_font.render(score_text, True, ORANGE)  # Render in orange color
    lives_render = menu_button_font.render(lives_text, True, ORANGE)  # Render in orange color
    
    screen.blit(score_render, (20, 20))
    screen.blit(lives_render, (screen_width - 120, 20))


def main_menu():
    # Initialize sound state
    sound_on = True
    
    # Define button rectangles
    start_button_rect = pygame.Rect(screen_width // 2 - 100, 250, 200, 50)
    sounds_button_rect = pygame.Rect(screen_width // 2 - 100, 320, 200, 50)
    exit_button_rect = pygame.Rect(screen_width // 2 - 100, 390, 200, 50)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    click_sound.play()
                    start_game()
                elif sounds_button_rect.collidepoint(event.pos):
                    sound_on = not sound_on  # Toggle sound state
                    if sound_on:
                        pygame.mixer.music.unpause()  # Turn on the music
                    else:
                        pygame.mixer.music.pause()  # Turn off the music
                    click_sound.play()
                elif exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(background_image, (0, 0))
        screen.blit(dim_surface, (0, 0))

        draw_text('Engineering Quizbee', menu_title_font, ORANGE, screen, screen_width // 2, 150)

        draw_rounded_rect(screen, ORANGE, start_button_rect)
        draw_text('Start', menu_button_font, BLACK, screen, screen_width // 2, 265)

        draw_rounded_rect(screen, ORANGE, sounds_button_rect)
        if sound_on:
            draw_rounded_rect(screen, ORANGE, sounds_button_rect, image=sound_on_image)
        else:
            draw_rounded_rect(screen, ORANGE, sounds_button_rect, image=sound_off_image)

        draw_rounded_rect(screen, ORANGE, exit_button_rect)
        draw_text('Exit', menu_button_font, BLACK, screen, screen_width // 2, 405)

        pygame.display.update()

if __name__ == '__main__':
    main_menu()
