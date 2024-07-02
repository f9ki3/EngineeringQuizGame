import pygame
import sys

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
ORANGE = (255, 165, 0)  # Orange color RGB value

# Load background image
background_image = pygame.image.load('background.jpg')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Create a surface for dimming effect
dim_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
dim_surface.fill((0, 0, 0, 200))  # Adjust the alpha value (0-255) for dimming effect

# Font
title_font = pygame.font.Font(None, 72)  # Larger font size for the title
button_font = pygame.font.Font(None, 36)  # Font size for buttons

# Load and play track.mp3
pygame.mixer.music.load('track.mp3')
pygame.mixer.music.play(-1)  # -1 loops the music indefinitely

# Load sounds
click_sound = pygame.mixer.Sound('gamestart.mp3')

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.centerx = x
    textrect.top = y  # Adjusted to set the top position instead of centery
    surface.blit(textobj, textrect)

def draw_rounded_rect(surface, color, rect, radius=20):
    pygame.draw.rect(surface, color, rect, border_radius=radius)

def main_menu():
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
                    # Start button clicked
                    print("Start button clicked")
                    click_sound.play()  # Play the click sound
                elif sounds_button_rect.collidepoint(event.pos):
                    # Toggle sounds on/off (you can add functionality here)
                    print("Sounds button clicked")
                    click_sound.play() 
                elif exit_button_rect.collidepoint(event.pos):

                    pygame.quit()
                    sys.exit()

        screen.blit(background_image, (0, 0))
        screen.blit(dim_surface, (0, 0))  # Overlay dim surface onto the background

        # Draw title
        draw_text('Engineering Quizbee', title_font, ORANGE, screen, screen_width // 2, 150)  # Orange color for title

        # Draw buttons with rounded rectangles
        start_button_rect = pygame.Rect(screen_width // 2 - 100, 250, 200, 50)
        draw_rounded_rect(screen, ORANGE, start_button_rect)
        draw_text('Start', button_font, BLACK, screen, screen_width // 2, 265)

        sounds_button_rect = pygame.Rect(screen_width // 2 - 100, 320, 200, 50)
        draw_rounded_rect(screen, ORANGE, sounds_button_rect)
        draw_text('Sounds: On', button_font, BLACK, screen, screen_width // 2, 335)

        exit_button_rect = pygame.Rect(screen_width // 2 - 100, 390, 200, 50)
        draw_rounded_rect(screen, ORANGE, exit_button_rect)
        draw_text('Exit', button_font, BLACK, screen, screen_width // 2, 405)

        pygame.display.update()

if __name__ == '__main__':
    main_menu()
