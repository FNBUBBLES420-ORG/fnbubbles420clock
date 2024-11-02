import pygame
import sys
from datetime import datetime

def create_gradient(width, height, top_color, bottom_color):
    """Create a vertical gradient between two colors."""
    gradient_surface = pygame.Surface((width, height))
    top_r, top_g, top_b = top_color
    bottom_r, bottom_g, bottom_b = bottom_color
    for y in range(height):
        r = top_r + (bottom_r - top_r) * y // height
        g = top_g + (bottom_g - top_g) * y // height
        b = top_b + (bottom_b - top_b) * y // height
        pygame.draw.line(gradient_surface, (r, g, b), (0, y), (width, y))
    return gradient_surface

# Initialize Pygame
pygame.init()
pygame.display.set_caption("FNBUBBLES420 ORG - Official Clock")

# Set up display
width, height = 1000, 400
screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
font = pygame.font.SysFont('segoeui', 48)

# Define text color
text_color = (255, 255, 255)  # White text

# Clock setup
clock = pygame.time.Clock()

# Background colors and setup
background_color_1 = (30, 30, 30)  # Dark gray
background_color_2 = (15, 50, 80)  # Some shade of blue
current_background = create_gradient(width, height, background_color_1, background_color_2)

previous_time = previous_date = ""
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%A, %d %B %Y")

    if current_time != previous_time or current_date != previous_date:
        screen.blit(current_background, (0, 0))
        time_surface = font.render(current_time, True, text_color)
        date_surface = font.render(current_date, True, text_color)
        time_rect = time_surface.get_rect(center=(width // 2, height // 2 - 30))
        date_rect = date_surface.get_rect(center=(width // 2, height // 2 + 40))
        screen.blit(time_surface, time_rect)
        screen.blit(date_surface, date_rect)
        pygame.display.flip()
        previous_time = current_time
        previous_date = current_date

    # Change background color every minute for dynamic effect
    if datetime.now().second == 0:  # Change background at the start of each minute
        current_background = create_gradient(width, height, background_color_2, background_color_1)
        background_color_1, background_color_2 = background_color_2, background_color_1  # Swap colors

    clock.tick(10)  # Reduce the frame rate to reduce CPU load
