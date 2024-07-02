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
correct_sound = pygame.mixer.Sound('correct.mp3')
fail_sound = pygame.mixer.Sound('fail.mp3')

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
    },
    {
        "question": "What is the purpose of a culvert in civil engineering?",
        "options": ["A. To filter pollutants from water", "B. To manage stormwater runoff",
                    "C. To purify groundwater", "D. To store agricultural runoff"],
        "correct_answer": "B"
    },
    {
        "question": "Which of the following is a commonly used construction material for building foundations?",
        "options": ["A. Steel", "B. Timber", "C. Concrete", "D. Plastic"],
        "correct_answer": "C"
    },
    {
        "question": "What is the function of a surveyor in civil engineering projects?",
        "options": ["A. Designing electrical systems", "B. Estimating project costs",
                    "C. Mapping land and measuring distances", "D. Programming software applications"],
        "correct_answer": "C"
    },
    {
        "question": "What does the term 'subgrade' refer to in road construction?",
        "options": ["A. Top layer of asphalt", "B. Soil beneath the pavement",
                    "C. Shoulder of the road", "D. Lane markings"],
        "correct_answer": "B"
    },
    {
        "question": "Which type of bridge is known for its arch shape?",
        "options": ["A. Suspension bridge", "B. Beam bridge", "C. Arch bridge", "D. Cable-stayed bridge"],
        "correct_answer": "C"
    },
    {
        "question": "What is the purpose of soil compaction in construction?",
        "options": ["A. To increase soil fertility", "B. To reduce soil erosion",
                    "C. To increase soil density and strength", "D. To filter water contaminants"],
        "correct_answer": "C"
    },
    {
        "question": "What does the term 'civil infrastructure' encompass?",
        "options": ["A. Residential buildings", "B. Transportation systems",
                    "C. Information technology networks", "D. Recreational facilities"],
        "correct_answer": "B"
    },
    {
        "question": "Which construction method involves pouring concrete into pre-made forms on-site?",
        "options": ["A. Prefabrication", "B. Cast-in-place", "C. Modular construction", "D. Steel framing"],
        "correct_answer": "B"
    },
    {
        "question": "What does the acronym 'HVAC' stand for in building systems?",
        "options": ["A. High-velocity air conditioning", "B. Heating, ventilation, and air conditioning",
                    "C. Home ventilation and cooling", "D. Hybrid vacuum air circulation"],
        "correct_answer": "B"
    },
    {
        "question": "Which environmental factor is crucial in designing bridges and tunnels?",
        "options": ["A. Noise pollution", "B. Light pollution", "C. Air quality", "D. Water quality"],
        "correct_answer": "A"
    },
    {
        "question": "What role does a civil engineer play in disaster management?",
        "options": ["A. Providing emergency medical care", "B. Assessing structural damage",
                    "C. Coordinating public transportation", "D. Restoring power lines"],
        "correct_answer": "B"
    },
    {
        "question": "Which engineering principle is fundamental to earthquake-resistant building design?",
        "options": ["A. Aerodynamics", "B. Seismic isolation", "C. Solar energy capture", "D. Tidal power generation"],
        "correct_answer": "B"
    },
    {
        "question": "What is the purpose of a stormwater management system in urban areas?",
        "options": ["A. To divert traffic flow during storms", "B. To prevent flooding",
                    "C. To control noise pollution", "D. To recycle wastewater"],
        "correct_answer": "B"
    },
    {
        "question": "Which type of foundation is suitable for buildings on soft soil?",
        "options": ["A. Pile foundation", "B. Raft foundation", "C. Strip foundation", "D. Spread footing"],
        "correct_answer": "A"
    },
    {
        "question": "What is the function of a traffic engineer in urban planning?",
        "options": ["A. Designing public parks", "B. Analyzing population growth",
                    "C. Optimizing traffic flow and signal timings", "D. Managing wildlife habitats"],
        "correct_answer": "C"
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
            display_final_score()  # Display final score and handle end game logic
            return  # Exit game loop
        
        # Clear the screen
        screen.blit(background_image, (0, 0))
        screen.blit(dim_surface, (0, 0))

        # Display current question and options
        display_question(quiz_questions[current_question])
        
        # Display score and lives
        display_stats()
        
        # Update the display
        pygame.display.update()

def display_final_score():
    global score
    
    # Play game over sound
    pygame.mixer.music.load('gameover.mp3')
    pygame.mixer.music.play()

    # Define button rectangles
    retry_button_rect = pygame.Rect(screen_width // 2 - 100, 300, 200, 50)
    menu_button_rect = pygame.Rect(screen_width // 2 - 100, 370, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.load('track.mp3')
                    pygame.mixer.music.play(-1) 
                    return  # Return to main menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button_rect.collidepoint(event.pos):
                    pygame.mixer.music.stop()  # Stop game over sound
                    pygame.mixer.music.load('track.mp3')
                    pygame.mixer.music.play(-1) 
                    start_game()  # Retry game
                elif menu_button_rect.collidepoint(event.pos):
                    pygame.mixer.music.stop()  # Stop game over sound
                    pygame.mixer.music.load('track.mp3')
                    pygame.mixer.music.play(-1) 
                    return  # Return to main menu
        
        # Clear the screen
        screen.blit(background_image, (0, 0))
        screen.blit(dim_surface, (0, 0))

        # Display final score higher on the screen
        final_score_text = f"Final Score: {score}"
        draw_text(final_score_text, menu_title_font, ORANGE, screen, screen_width // 2, 150)

        # Draw retry button
        draw_rounded_rect(screen, ORANGE, retry_button_rect)
        draw_text('Retry', menu_button_font, BLACK, screen, screen_width // 2, 315)

        # Draw menu button
        draw_rounded_rect(screen, ORANGE, menu_button_rect)
        draw_text('Menu', menu_button_font, BLACK, screen, screen_width // 2, 385)

        # Update the display
        pygame.display.update()

        # Control FPS
        pygame.time.Clock().tick(60)





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


# Inside check_answer_click() function
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
            correct_sound.play()  # Play correct sound
        else:
            lives -= 1
            fail_sound.play()  # Play fail sound
        
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
